# How to Backtest Project using using Lean-CLI

# prerequisites- 
1. You need to have python installed on your pc
2. You need to have docker installed on your pc
3. You need to have pip installed 


# In the projects root run-
1. Once pip is installed, run:
    pip install venv quant
2. Command in no. 1 above creates a virtual environment called quant
3. Activate virtual environment by running one of the following, depending on your Operating System:
- Windows: quant\Scripts\activate
- Linux/Mac: source/quant/bin/activate

# To install lean-CLI open a terminal and run:
pip install lean

# To run the backtest run:
lean backtest yahoo_data
