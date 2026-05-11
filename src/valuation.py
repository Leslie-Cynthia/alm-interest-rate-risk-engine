import pandas as pd

def  get_rate (maturity, yield_curve):  
    """ Take the closest rate from the table
    according to the distance between the maturities
    :params maturity: float - the maturity of and asset
    :params yield_curve: [float,float] - the yield curve to use
    :return closest: float - the corresponding yield

    """
    closest = yield_curve.iloc[(yield_curve["maturity_years"] - maturity).abs().argsort()[:1]]

    return closest["rate"].values[0]



def add_market_rate_column (data , yield_curve):
    data["market_rate"] = 0.0
    for index, maturity in enumerate(data["maturity_years"]):
        data.loc[index,"market_rate"]= get_rate(maturity, yield_curve)
    return data

# Now we calculate the present value, which is 
# the notional /(1+ market_rate)^maturity_years

def present_value(data):
    data ["present_value"] = 0.0
    data ["present_value"] = data ["notional"]/(1+data ["market_rate"])** data ["maturity_years"]
    return data


