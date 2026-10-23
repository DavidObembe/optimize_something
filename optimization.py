""""""  		  	   		 		  		  		  		    	 		 		   		 		  
"""MC1-P2: Optimize a portfolio.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 		  		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 		  		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 		  		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 		  		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 		  		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 		  		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 		  		  		  		    	 		 		   		 		  
or edited.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 		  		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 		  		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 		  		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
Student Name: David Obembe (replace with your name)  		  	   		 		  		  		  		    	 		 		   		 		  
GT User ID: dobembe3 (replace with your User ID)  		  	   		 		  		  		  		    	 		 		   		 		  
GT ID: 904262729 (replace with your GT ID)  		  	   		 		  		  		  		    	 		 		   		 		  
"""  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		 		  		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 		  		  		  		    	 		 		   		 		  
from util import get_data, plot_data  
from scipy.optimize import minimize

OUTPUT_DIRECTORY = "images"

def author():  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    return "dobembe3"  # replace tb34 with your Georgia Tech username.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
def gtid():  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    return 904262729  # replace with your GT ID number  

def study_group():
    """"
    Returns
        A comma separated string of GT_Name of each member of your study group
        # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone

    Return type
        str	  	
    """
    return "dobembe3"  		
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		  	   		 		  		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		  	   		 		  		  		  		    	 		 		   		 		  
def optimize_portfolio(  		  	   		 		  		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		 		  		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		 		  		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 		  		  		  		    	 		 		   		 		  
    gen_plot=True,  		  	   		 		  		  		  		    	 		 		   		 		
):  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 		  		  		  		    	 		 		   		 		  
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 		  		  		  		    	 		 		   		 		  
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 		  		  		  		    	 		 		   		 		  
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 		  		  		  		    	 		 		   		 		  
    statistics.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 		  		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		 		  		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 		  		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		 		  		  		  		    	 		 		   		 		  
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 		  		  		  		    	 		 		   		 		  
        symbol in the data directory)  		  	   		 		  		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		 		  		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 		  		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		 		  		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 		  		  		  		    	 		 		   		 		  
        standard deviation of daily returns, and Sharpe ratio  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		  	   		 		  		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		  	   		 		  		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY 
    print("result of prices_all:")
    print(prices_all)
    prices = prices_all[syms]  # only portfolio symbols  	
    print("result of prices: ")	  
    print(prices)		   		 		  		  		  		    	 		 		   		 		  
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # find the allocations for the optimal portfolio  		  	   		 		  		  		  		    	 		 		   		 		  
    normed = normalize_portfolio(prices)
    print("result of normed:")
    print(normed)

    number_of_assets = len(syms)

    # Use a uniform allocation of 1/n to each of the n assets as the initial guess
    initial_allocs = np.ones(number_of_assets) / number_of_assets
    print("result of initial_allocs:")
    print(initial_allocs)

    # Long positions only: each allocation must be between 0.0 and 1.0
    bounds = [(0.0, 1.0)] * number_of_assets

    def eq_constraint(allocs):
        return np.sum(allocs) - 1.0

    # Allocations must sum to 1.0
    constraints = ({"type": "eq", "fun": eq_constraint},)

    rfr = 0.0
    sf = 252

    def negative_sharpe_ratio(allocs):
        alloced = alloced_portfolio(normed, allocs)
        port_val = calculate_portfolio_value(alloced)
        daily_returns = port_val.pct_change().dropna()
        adr = daily_returns.mean()
        sddr = daily_returns.std()
        sr = (adr - rfr) / sddr * np.sqrt(sf)
        return -sr

    result = minimize(
        negative_sharpe_ratio,
        initial_allocs,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )
    allocs = result.x

    alloced = alloced_portfolio(normed, allocs)
    print("result of alloced:")
    print(alloced)

    # Get daily portfolio value  
    port_val = calculate_portfolio_value(alloced)
    print("result of port_val:")
    print(port_val)

    daily_returns = port_val.pct_change().dropna()

    # add code here to compute stats  	
    #cr -> cumulative return, adr -> average daily return, sddr -> standard deviation of daily return, sr -> Sharpe ratio
    #sf is sampling frequency stated to be 252 trading days in a year.
    #rfr is risk-free rate stated to be zero in instructions.
    cr = (port_val.iloc[-1] / port_val.iloc[0]) - 1
    adr = daily_returns.mean()
    sddr = daily_returns.std()

    sr = (adr - rfr) / sddr * np.sqrt(sf)  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 				  	   		 		  		  		  		    	 		 		   		 		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		 		  		  		  		    	 		 		   		 		  
    if gen_plot:  		  	   		 		  		  		  		    	 		 		   		 		  
        # add code to plot here
        normalized_portfolio = normalize_portfolio(port_val) 		 
        normalized_SPY = normalize_portfolio(prices_SPY)

        plt.plot(normalized_portfolio.index, normalized_portfolio.values, label="Portfolio")
        plt.plot(normalized_SPY.index, normalized_SPY.values, label="SPY")
        plt.title("Daily Portfolio Value and SPY Comparison")
        plt.xlabel("Date")
        plt.ylabel("Normalized Price")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(OUTPUT_DIRECTORY + "/Figure1.png")	  	   		 		  		  		  		    	 		 		   		 		  
        pass  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    return allocs, cr, adr, sddr, sr  	


#STEP 1: Normalise the prices
def normalize_portfolio(prices):
    return prices / prices.iloc[0]

#STEP 2: allocate the normalized prices according to portfolio allocations
def alloced_portfolio(normed, allocs):
    return normed * allocs


#STEP 3: calculate the Portfolio Value
def calculate_portfolio_value(pos_val):
    return pos_val.sum(axis=1)

#Pulled from assess portfolio project
def assess_portfolio(  		  	   		 		  		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		 		  		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		 		  		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 		  		  		  		    	 		 		   		 		  
    allocs=[0.1, 0.2, 0.3, 0.4],  		  	   		 		  		  		  		    	 		 		   		 		  
    sv=1000000,  		  	   		 		  		  		  		    	 		 		   		 		  
    rfr=0.0,  		  	   		 		  		  		  		    	 		 		   		 		  
    sf=252.0,  		  	   		 		  		  		  		    	 		 		   		 		  
    gen_plot=False,  		  	   		 		  		  		  		    	 		 		   		 		  
):  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    Estimate a set of test points given the model we built.  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 		  		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		 		  		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 		  		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		 		  		  		  		    	 		 		   		 		  
    :param syms: A list of 2 or more symbols that make up the portfolio (note that your code should support any symbol in the data directory)  		  	   		 		  		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		 		  		  		  		    	 		 		   		 		  
    :param allocs:  A list of 2 or more allocations to the stocks, must sum to 1.0  		  	   		 		  		  		  		    	 		 		   		 		  
    :type allocs: list  		  	   		 		  		  		  		    	 		 		   		 		  
    :param sv: The starting value of the portfolio  		  	   		 		  		  		  		    	 		 		   		 		  
    :type sv: int  		  	   		 		  		  		  		    	 		 		   		 		  
    :param rfr: The risk free return per sample period that does not change for the entire date range (a single number, not an array)  		  	   		 		  		  		  		    	 		 		   		 		  
    :type rfr: float  		  	   		 		  		  		  		    	 		 		   		 		  
    :param sf: Sampling frequency per year  		  	   		 		  		  		  		    	 		 		   		 		  
    :type sf: float  		  	   		 		  		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 		  		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		 		  		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		 		  		  		  		    	 		 		   		 		  
    :return: A tuple containing the cumulative return, average daily returns,  		  	   		 		  		  		  		    	 		 		   		 		  
        standard deviation of daily returns, Sharpe ratio and end value  		  	   		 		  		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		  	   		 		  		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		  	   		 		  		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		 		  		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		  	   		 		  		  		  		    	 		 		   		 		  
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Get daily portfolio value  		  	   		 		  		  		  		    	 		 		   		 		  
    port_val = prices_SPY  # add code here to compute daily portfolio values  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Get portfolio statistics (note: std_daily_ret = volatility)  		  	   		 		  		  		  		    	 		 		   		 		  
    cr, adr, sddr, sr = [  		  	   		 		  		  		  		    	 		 		   		 		  
        0.25,  		  	   		 		  		  		  		    	 		 		   		 		  
        0.001,  		  	   		 		  		  		  		    	 		 		   		 		  
        0.0005,  		  	   		 		  		  		  		    	 		 		   		 		  
        2.1,  		  	   		 		  		  		  		    	 		 		   		 		  
    ]  # add code here to compute stats  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		 		  		  		  		    	 		 		   		 		  
    if gen_plot:  		  	   		 		  		  		  		    	 		 		   		 		  
        # add code to plot here  		  	   		 		  		  		  		    	 		 		   		 		  
        df_temp = pd.concat(  		  	   		 		  		  		  		    	 		 		   		 		  
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1  		  	   		 		  		  		  		    	 		 		   		 		  
        )  		  	   		 		  		  		  		    	 		 		   		 		  
        pass  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Add code here to properly compute end value  		  	   		 		  		  		  		    	 		 		   		 		  
    ev = sv  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    return cr, adr, sddr, sr, ev  		  	   		 		    
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
def test_code():  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
    This function WILL NOT be called by the auto grader.  		  	   		 		  		  		  		    	 		 		   		 		  
    """  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008, 6, 1)  		  	   		 		  		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2009, 6, 1)  	
    symbols = ['IBM', 'X', 'GLD', 'JPM']	  	   		 		  		  		  		    	 		 		   		 		  
    # symbols = ["GOOG", "AAPL", "GLD", "XOM", "IBM"]
    # symbols = ["GOOG", "AAPL", "GLD", "XOM"]   		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Assess the portfolio  		  	   		 		  		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 		  		  		  		    	 		 		   		 		  
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True  		  	   		 		  		  		  		    	 		 		   		 		
    )  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"End Date: {end_date}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Symbols: {symbols}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Allocations:{allocations}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Sharpe Ratio: {sr}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Average Daily Return: {adr}")  		  	   		 		  		  		  		    	 		 		   		 		  
    print(f"Cumulative Return: {cr}")  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
  		  	   		 		  		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 		  		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		  	   		 		  		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		  	   		 		  		  		  		    	 		 		   		 		  
    test_code()  		  	   		 		  		 