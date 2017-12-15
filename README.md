# Pyfinace

python program for gatherign tickers, stock data aggregation, and machine learning

## Getting Started

### Prerequisites

```
Python 3
Pip 
Virtualenv
```

### Installing

Setup virtual environment with python 3 flagged

```
virtualenv -p python3 pyfinance
```

Change directory into virtual environment and activate

```
cd pyfinance/ && source bin/activate
```

Clone repo into virtual environment

```
git clone https://github.com/CCecilia/pyfinance.git
```

Change to root project directory

```
cd pyfinance
```

Install dependencies from requirements.txt

```
pip install -r requirements.txt
```

Gather ticker data

```
python pyfinance_data_gathering.py
```

Gather company  data and generate heat map

```
pyfinance_data_visualizing.py
```

Train maching and test

```
pyfinance_machine_learning.py
```

## Authors

* **Christian Cecilia** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [SentDex](https://www.youtube.com/watch?v=2BrpKpWwT2A&list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ) for making an amazing tutorials 
