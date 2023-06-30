# Use of Complex Networks to analyze international strade data
## Advanced Data Science - Network Science project

Author: *Emanuele Lena*
Year: *2022/23* 

## Project description 

This project aims to use Complex Networks techniques and tools (graph analysis, centrality measures, community detection, etc.) to analyze an international trade dataset. The dataset used is the FAO Trade Network, which contains data about international trade of food products between countries. The dataset is available at https://networks.skewed.de/net/fao_trade.

In this project we will try to apply Complex Networks techniques to answer some questions about the dataset, such as:

- Which are the most central countries in the network? (according to various centrality measures)
- How are centrality measures correlated in this network?
- What kind of network model fits better to this graph? Which properties seems to be "explained by randomness"?
- What meso-scale structures are present in the network? (communities, cliques, core-perphery structures, etc.)
- How does the different layers relate? 

To do that, we will use the Python graph library `networkx`, together with some "from sketch" implementations of some algorithms.

Some used techniques and tools are:

- various centralities measures, such as degree, strenght, closeness, betweenness, eigenvector, Katz and PageRank
- clustering coefficients (Watts-Strogartz and Newmann)
- K-Core algorithm
- Newmann and Girvan modularity, Louvain community detection algorithm
- Pearson coefficient as a tool to measure similarity between centrality measures and communities
- Erdos-Renyi random graph model properties
- Fasino and Rinaldi algorithm to detect core-periphery structures

NOTE:

> The focus on this work is actually on applying Complex Networks techniques to the dataset, rather than really answering exaustively to the questions above. This is an university exam project, not a research paper or a real exaustive analysis.

## How run the project

### Requirements 

- Python 3.11
- Poetry as virtual enviroment manager (optional)

Used libraries and tools:

- `pandas`
- `numpy`
- `scipy`
- `networkx`
- `matplotlib`
- `seaborn`
- `jupyter`

### How to run the project


- open a terminal in the project folder
- if you want to use Poetry as virtual enviroment manager:
  - ensure you have Poetry installed on your system
  - run `poetry shell` to activate the virtual enviroment
  - run `poetry install` to install all dependencies

  else, you can always manage your virtual enviroment as you prefer. Just ensure you have all the required libraries installed (see `pyproject.toml` file).

- Project is a Jupyter Notebook, so you can run it with your favourite IDE or with the command line: `jupyter notebook fao_trade.ipynb`

## Further notes

### Data gathering

This project uses data from https://networks.skewed.de/net/fao_trade. The notebook implements procedures to download and save locally the data. See the notebook for more details.



