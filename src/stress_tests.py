import pandas as pd
from src import gap_analysis as gap

def tests (balance_sheet):
    delta_rate = 0.01   # the delta growth of 100 bps
    economic_value_gap1 = gap.gap1(balance_sheet)
    economic_value_gap2 = gap.gap2(balance_sheet)
    economic_value_gap3 = gap.gap3(balance_sheet)
    economic_value_gap4 = gap.gap4(balance_sheet)
    economic_value = balance_sheet[balance_sheet["type"]== "asset"]["present_value"].sum() - balance_sheet[balance_sheet["type"] == "liability"]["present_value"].sum()

    balance_sheet["stressed_rate"]= balance_sheet["market_rate"]+ delta_rate   # a growth of delta

    print(balance_sheet["market_rate"].head())
    print(balance_sheet["stressed_rate"].head())

    # stressed present value
    balance_sheet["stressed_present_value"] = balance_sheet ["notional"]/(1+balance_sheet ["stressed_rate"])**balance_sheet ["maturity_years"]

    # stressed economic value
    stressed_economic_value = balance_sheet[balance_sheet["type"]== "asset"]["stressed_present_value"].sum()- balance_sheet[balance_sheet["type"] == "liability"]["stressed_present_value"].sum()

    print (f"economic value:{economic_value}, stressed economic value: {stressed_economic_value} ")

    # stressed gap analysis
    stressed_economic_value_gap1 = balance_sheet[(balance_sheet["type"]=="asset")&
                                        (balance_sheet["maturity_years"]<=1)]["stressed_present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                        (balance_sheet["maturity_years"]<=1)]["stressed_present_value"].sum()

    stressed_economic_value_gap2 = balance_sheet[(balance_sheet["type"]=="asset")& 
                                        (balance_sheet["maturity_years"]>1 ) &
                                        (balance_sheet["maturity_years"]<=3)]["stressed_present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                        (balance_sheet["maturity_years"]>1 ) &
                                        (balance_sheet["maturity_years"]<=3)]["stressed_present_value"].sum()

    stressed_economic_value_gap3 = balance_sheet[(balance_sheet["type"]=="asset")& 
                                        (balance_sheet["maturity_years"]>3 ) &
                                        (balance_sheet["maturity_years"]<= 5)]["stressed_present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                        (balance_sheet["maturity_years"]>3 ) &
                                        (balance_sheet["maturity_years"]<=5)]["stressed_present_value"].sum()


    stressed_economic_value_gap4 = balance_sheet[(balance_sheet["type"]=="asset")&
                                        (balance_sheet["maturity_years"]>5)]["stressed_present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                        (balance_sheet["maturity_years"]> 5)]["stressed_present_value"].sum()

    
    # calculation of the different spread
    delta_economic_value = stressed_economic_value - economic_value
    delta_economic_value_gap1 = stressed_economic_value_gap1 - economic_value_gap1
    delta_economic_value_gap2 = stressed_economic_value_gap2 - economic_value_gap2
    delta_economic_value_gap3 = stressed_economic_value_gap3 - economic_value_gap3
    delta_economic_value_gap4 = stressed_economic_value_gap4 - economic_value_gap4

    return stressed_economic_value, stressed_economic_value_gap1, stressed_economic_value_gap2, stressed_economic_value_gap3, stressed_economic_value_gap4,delta_economic_value,delta_economic_value_gap1,delta_economic_value_gap2, delta_economic_value_gap3, delta_economic_value_gap4
