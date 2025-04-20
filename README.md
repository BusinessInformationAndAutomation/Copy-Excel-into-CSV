# Copy-Excel-into-CSV
Overview
This script automates the process of locating the most recent Excel file in the user's Downloads directory, cleaning and converting it to a CSV, and then filtering the data based on specified date and organizational fields. The final filtered output is saved to a new CSV file. I created this script in order to automate a process within my daily workflow that was prone to user error.

Key Features
Automatically identifies the latest file in C:Downloads/

Reads the Excel file, skipping the first 8 header rows

Saves cleaned data into a CSV file

Loads a working CSV for additional processing

Converts the "Date Change Entered" field to datetime

Gets today’s and yesterday’s date in MM/DD/YYYY format

Filters entries by:

"Location - Previous" equal to a set value

"Date Change Entered" is today or yesterday

"Last Day Worked" is not blank

Drops rows where "Last Day Worked" is null

Exports final filtered data to Beginning_Filter.csv

File Paths Used
Input Directory: C:/Downloads/

Working File: C:/test_change.csv

Output
test_change.csv: Cleaned version of the original Excel

test_keep.csv: Same as test_change.csv for reference/backup

Beginning_Filter.csv: Final filtered data

Requirements
Python 3.10+

pandas

Notes
Ensure the target Excel file is consistently structured with usable data starting after row 8

Script overwrites Beginning_Filter.csv every run

All filters are hardcoded and specific to the organization referenced
