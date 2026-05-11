import pandas as pd

def gap1 (balance_sheet):

    economic_value_gap1 = balance_sheet[(balance_sheet["type"]=="asset")&
                                     (balance_sheet["maturity_years"]<=1)]["present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                     (balance_sheet["maturity_years"]<=1)]["present_value"].sum()
    return economic_value_gap1
 



def gap2 (balance_sheet):
    
    economic_value_gap2 = balance_sheet[(balance_sheet["type"]=="asset")& 
                                     (balance_sheet["maturity_years"]>1 ) &
                                       (balance_sheet["maturity_years"]<=3)]["present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                     (balance_sheet["maturity_years"]>1 ) &
                                       (balance_sheet["maturity_years"]<=3)]["present_value"].sum()


    return economic_value_gap2


def gap3 (balance_sheet):

    economic_value_gap3 = balance_sheet[(balance_sheet["type"]=="asset")& 
                                     (balance_sheet["maturity_years"]>3 ) &
                                       (balance_sheet["maturity_years"]<= 5)]["present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                     (balance_sheet["maturity_years"]>3 ) &
                                       (balance_sheet["maturity_years"]<=5)]["present_value"].sum()

    return economic_value_gap3

def gap4(balance_sheet):
    economic_value_gap4 = balance_sheet[(balance_sheet["type"]=="asset")&
                                     (balance_sheet["maturity_years"]>5)]["present_value"].sum() - balance_sheet[(balance_sheet["type"]=="liability")&
                                     (balance_sheet["maturity_years"]> 5)]["present_value"].sum()

    return economic_value_gap4

