# TODO: (maybe) implement it

def layer_entropy(layer_g: nx.Graph):
    """Von Neumann entropy of a single layer"""

    layer_m = nx.adjacency_matrix(layer_g).todense() 

    # compute the Laplacian matrix, rescalated by the sum of the matrix
    D = (np.diag(np.sum(layer_m, axis=1)) + np.diag(np.sum(layer_m, axis=0)))/2
    c = 1 / np.sum(layer_m)
    Lg = c * (D - layer_m)

    # compute eigenvalues
    eig = np.linalg.eig(Lg).eigenvalues

    # compute entropy on the eigenvalues
    return - np.sum(np.multiply(eig, np.log2(eig)))

def multi_layer_entropy(multi_layer: Dict[str, nx.Graph]): 
    """Von Neumann entropy of a multilayer network. 
    It returns a tuple with a all-layer entropy + 
    a dict with the entropies of the single layers"""
    
    h = {}
    H = 0
    for layer in multi_layer.keys():
        h[layer] = layer_entropy(multi_layer[layer])
        H += h[layer]

    H /= len(multi_layer.keys())
    return (H, h)

def layer_hierarchical_clustering(multi_layer: Dict[str, np.ndarray], previous_h=None) \
    -> List[Tuple[Dict[str, np.ndarray], Dict[str, float], float]]: 
    """Make hierarchcal clustering on network layers, returning a list of tuples with 
    - the layers matricies 
    - the entropy of the networks
    - the Jensen-Shannon divergence on this step"""

    # BASE CASE: if there is only one layer, return it
    if len(multi_layer.keys()) == 1:
        return [(multi_layer, previous_h, None)]
    
    # calculate initials layers entropy + multi-layer entropy
    if previous_h is None:
        _, h = multi_layer_entropy(multi_layer)

    # calculate all possible pairs
    names = list(multi_layer.keys())
    pairs = [(a,b) for idx,a in enumerate(names) for b in names[idx + 1:]]

    # try aggregate all pairs and calculate resulting entropy
    # we wanna found the one that has smaller Jensen-Shannon divergence
    min_jsd = math.inf
    min_jsd_pair = None
    min_jsd_aggr_g = None

    print("Calculating JSD for all pairs..., Number of pairs:", len(pairs))
    i = 0

    for (a,b) in pairs:

        i += 1
        if i % 1000 == 0:
            print(f"JSD for pair {i} of {len(pairs)}")


        # aggregate the two layers
        aggr_g = combine_graphs(multi_layer[a], multi_layer[b])

        # calculate the entropy of the aggregation
        H_ab = layer_entropy(aggr_g)

        # calculate the Jensen-Shannon divergence
        jsd = H_ab - (h[a] + h[b])/2

        if jsd < min_jsd:
            min_jsd = jsd
            min_jsd_pair = (a,b)
            min_jsd_aggr_g = aggr_g

    # merge layers and remove the old ones
    a, b = min_jsd_pair[0], min_jsd_pair[1]

    new_ml = multi_layer.copy()
    del new_ml[a]
    del new_ml[b]
    new_ml[f"{a}+{b}"] = min_jsd_aggr_g

    # add new entropy to the dict
    new_h = h.copy()
    del new_h[a]
    del new_h[b]
    new_h[f"{a}+{b}"] = min_jsd

    print(f"Aggregating {a} and {b} with JSD {min_jsd}. Remaining layers: {len(new_ml.keys())}")
    
    # return this step of the clustering and make a recursive call
    return [(new_ml, new_h, jsd)] + layer_hierarchical_clustering(new_ml, new_h)
