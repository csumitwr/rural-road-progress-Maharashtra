## Purpose:

This project demonstrates a simple and transparent approach to analyzing public infrastructure data using reproducible data analysis techniques.


## Data Source:

The analysis uses publicly available Monthly Progress Report (MPR) data published by the Government of India March snapshot data is used for each year from 2018 to 2025. 
These snapshots represent the reported status of sanctioned and completed road works as ofMarch for each year.

NOTE: Financial completion data for 2022 is not reported in the official source and is shown as missing in the analysis.


## Outputs:

Sanctioned Road Length: Total road length approved for construction in a given year.
Completed Road Length: Total road length reported as completed.

Length Completion Rate (%): Shows the share of sanctioned road length that has been completed.
Length Completion Rate = (Completed Length / Sanctioned Length) × 100

Sanctioned Amount: Total funds approved for road construction.
Completed Amount: Total expenditure reported for completed works.

Spend Realization Rate (%): Indicates how much of the sanctioned amount has been realized as reported expenditure.
Spend Realization Rate = (Completed Amount / Sanctioned Amount) × 100


## Generated Outputs:

1. Year-wise summary of sanctioned and completed road works
2. Length completion and spend realization rates by year
3. Sanction-year summaries to understand backlog and execution patterns
4. Static charts showing trends over time

Final datasets are exported as CSV files in the data/exports/ folder.


## Limitations:

1. Analysis is limited to officially reported MPR data
2. Missing values are not estimated or filled
3. Results reflect reporting status, not on-ground verification
