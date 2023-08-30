import pandas as pd


data=pd.read_excel("employees_data_latest.xlsx")

# print(data.columns)
# print(data.values)
# print(data.items)
for column in data.columns:
    data[column] = data[column].astype(str).str.replace(' ', '')

value_counts = data['Aug 27,2023'].value_counts()
wfh_count = value_counts.get('WFH', 0)
wfo_count = value_counts.get('WFO', 0)

print(f"Count of WFH_today: {wfh_count}")
print(f"Count of WFO_today: {wfo_count}")

last_five_days_data = ['Aug 23,2023', 'Aug 24,2023', 'Aug 25,2023', 'Aug 26,2023', 'Aug 27,2023']
WFH_last_5_days = data[last_five_days_data].apply(lambda col: (col == 'WFH').sum(), axis=1)
WFO_last_5_days = data[last_five_days_data].apply(lambda col: (col == 'WFO').sum(), axis=1)

employees_wfh_previous_days = (WFH_last_5_days > 0).sum()
employees_wfo_previous_days = (WFO_last_5_days > 0).sum()

print("Employees Marked WFH for Previous 5 Days:", employees_wfh_previous_days)
print("Employees Marked WFO for Previous 5 Days:", employees_wfo_previous_days)
