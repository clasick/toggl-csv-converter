# Toggl .CSV Converter

## From Boosted
1. Export `.csv` from Boosted.
2. Remove all columns from exported `.csv` except for:
    * `Project`,`Start Date`, `Start Time`, `Duration`
3. Add Email column to `.csv` with default value.
4. Make sure that all columns in the `.csv` have values.
5. Run `boosted_to_toggl.py` after editing the paths -> `toggl.csv` is created in current directory.
6. Import `toggl.csv` file using Toggl.