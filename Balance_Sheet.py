from basics import *

# stops DF from truncating
pd.options.display.max_columns = 40
pd.options.display.width = 500
columns = [f'Year: 0']

balance_sheet = pd.DataFrame.from_dict(annual_balance_sheet[0], orient='index')
balance_sheet = balance_sheet[8:52]
balance_sheet.columns = [f'Year: 0']

for year in range(1, years):
      balance_sheet[f'Year: -{year}'] = pd.DataFrame.from_dict(annual_balance_sheet[year], orient='index')
      columns.append(f'Year: -{year}')
orderedColumns = orderColumns(columns)
balance_sheet = balance_sheet.reindex(columns = orderedColumns)

for year in range(1,years_to_project + 1):
      new_list = orderedColumns[-3:]
      average = balance_sheet.loc[:, new_list].mean(axis=1)
      balance_sheet[f'Year: {year}'] = average
      orderedColumns.append(f'Year: {year}')