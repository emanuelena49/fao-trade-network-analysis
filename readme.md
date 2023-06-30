# Use of complex networks to analyze international strade data
## Advanced Data Science - Network Science project

Author: *Emanuele Lena*
Year: *2022/23* 

## Summary 

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



