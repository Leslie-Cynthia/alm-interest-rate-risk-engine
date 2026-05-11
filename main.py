import pandas as pd
import math
from src import data_loader as dat
from src import valuation as val
from src import gap_analysis as gap
from src import stress_tests as stress

#  I -  Load the csv
balance_sheet, yield_curve = dat.data_loading('Data/Balance_sheet.csv','Data/yield_curve.csv')

# II-  present value

yield_curve = yield_curve.sort_values("maturity_years")  # to make the choice rate easier
balance_sheet = val.add_market_rate_column(balance_sheet,yield_curve)
balance_sheet = val.present_value(balance_sheet)
print ("New balance sheet")
print (balance_sheet.head())

#III- Now we calculate the Net Economic Value :  PV asset - PV liabilities

economic_value = balance_sheet[balance_sheet["type"]== "asset"]["present_value"].sum() - balance_sheet[balance_sheet["type"] == "liability"]["present_value"].sum()
#economic_value = pv_assets - pv_liabilities
print (f"the economic value of the firm is {economic_value}\n")

# IV- The gap analysis
# Now we have to calculate the gap analysis in order to evaluate any 
#liquidity risk
economic_value_gap1=0.0    # for maturity <=1
economic_value_gap2=0.0    # 1<maturity<=3
economic_value_gap3=0.0    # 3< maturity <=5
economic_value_gap4=0.0    # maturity >5

economic_value_gap1 = gap.gap1(balance_sheet)
economic_value_gap2 = gap.gap2(balance_sheet)
economic_value_gap3 = gap.gap3(balance_sheet)
economic_value_gap4 = gap.gap4(balance_sheet)


print (f"the economic value for gap between <=1y maturity is {economic_value_gap1}\nthe economic value for gap between 1y and 3y is {economic_value_gap2}\n")
print (f"the economic value for gap between 3y and 5y is {economic_value_gap3}\nthe economic value for gap > 5y is {economic_value_gap4}\n")


# V - Stress tests
# When the market rate rises

stressed_economic_value, stressed_economic_value_gap1,stressed_economic_value_gap2,stressed_economic_value_gap3,stressed_economic_value_gap4,delta_economic_value, delta_economic_value_gap1, delta_economic_value_gap2, delta_economic_value_gap3, delta_economic_value_gap4 = stress.tests(balance_sheet)
# printing of the results

print (f" the stress impact on the:\n- economic value: {delta_economic_value}\n-value gap 1: {delta_economic_value_gap1}\n")
print(f"-value gap 2: {delta_economic_value_gap2}\n-value gap 3: {delta_economic_value_gap3}\n-value gap 4: {delta_economic_value_gap4}\n")

#  VI- Creation of outputs for Power BI
balance_sheet.to_csv("outputs/balance_sheet_enriched.csv", index = False)

gap_results = pd.DataFrame({
    "bucket": ["<=1y", "1y-3y", "3y-5y", ">5y"],
    "base_gap": [
        economic_value_gap1,
        economic_value_gap2,
        economic_value_gap3,
        economic_value_gap4

    ],
    "stressed_gap": [
        stressed_economic_value_gap1,
        stressed_economic_value_gap2,
        stressed_economic_value_gap3,
        stressed_economic_value_gap4
    ],
    "delta_gap":[
        delta_economic_value_gap1,
        delta_economic_value_gap2,
        delta_economic_value_gap3,
        delta_economic_value_gap4
    ]
    })

gap_results.to_csv ("outputs/gap_analysis.csv", index = False)

stress_results = pd.DataFrame({
    "metric": ["economic_value"],
    "base_value": [economic_value],
    "stressed_value": [stressed_economic_value],
    "delta": [delta_economic_value]
})

stress_results.to_csv ("outputs/stress_results.csv", index = False)

