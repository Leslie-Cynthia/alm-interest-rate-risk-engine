# ALM Interest Rate Risk Engine

## Overview

This project builds a simplified Asset-Liability Management (ALM) engine to measure the impact of interest rate movements on a banking balance sheet.

The model uses a synthetic balance sheet, maps each instrument to a market rate, computes present values, performs maturity gap analysis, and applies a parallel interest rate stress scenario.

## Business Problem

Banks are exposed to interest rate risk when the maturity and repricing profiles of their assets and liabilities are not aligned.

For example, a bank may hold long-term fixed-rate assets while funding itself with shorter-term liabilities. If interest rates rise, long-duration assets may lose more value than liabilities, reducing the economic value of the balance sheet.

This project aims to reproduce this mechanism in a simplified framework.

## Methodology

The project follows these steps:

1. Load a synthetic banking balance sheet and a zero-coupon yield curve.
2. Match each instrument maturity with the closest market rate.
3. Compute the present value of each asset and liability.
4. Calculate the economic value of the balance sheet.
5. Perform maturity gap analysis across time buckets.
6. Apply a +100 basis points parallel interest rate shock.
7. Compare base and stressed results.

## Features

- Synthetic balance sheet modeling
- Yield curve mapping
- Present value calculation
- Economic value computation
- Maturity gap analysis
- Interest rate stress testing
- CSV exports for Power BI visualization

## Project Structure


ALM/
│
├── Data/
│   ├── Balance_sheet.csv
│   └── yield_curve.csv
│
├── outputs/
│   ├── balance_sheet_enriched.csv
│   ├── gap_analysis.csv
│   └── stress_results.csv
│
├── src/
│   ├── data_loader.py
│   ├── valuation.py
│   ├── gap_analysis.py
│   └── stress_tests.py
│
├── main.py
├── README.md
└── requirements.txt


## Stress Scenario

The stress test applies a parallel upward shift of +100 basis points to the market yield curve.

This allows the model to evaluate how the economic value of the balance sheet reacts to a rise in interest rates.

## Key Findings

The stress test shows that long-maturity instruments are more sensitive to interest rate changes.

In this simplified balance sheet, long-term assets lose more value under a +100bps rate shock, while shorter-term liabilities are less affected. As a result, the economic value of the balance sheet deteriorates under the stress scenario.

## Tech Stack

* Python
* pandas
* Power BI
* CSV data processing

## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Run the main script: python main.py
4. The output files will be generated in the `outputs/` folder.
5. These files can then be imported into Power BI.

## Next Improvements

Possible improvements include:

* Adding multiple interest rate scenarios
* Implementing interpolation instead of nearest-rate matching
* Adding duration and convexity calculations
* Using real market yield curve data
* Building a Power BI dashboard



