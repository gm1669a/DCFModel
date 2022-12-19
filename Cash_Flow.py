from basics import *

# stops DF from truncating
pd.options.display.max_columns = 40
pd.options.display.width = 500
columns = [f'Year: 0']

cash_flow = pd.DataFrame.from_dict(annual_cash_flow[0], orient='index')
cash_flow = cash_flow[8:38]
cash_flow.columns = [f'Year: 0']

for year in range(1, years):
      cash_flow[f'Year: -{year}'] = pd.DataFrame.from_dict(annual_cash_flow[year], orient='index')
      columns.append(f'Year: -{year}')
orderedColumns = orderColumns(columns)
cash_flow = cash_flow.reindex(columns = orderedColumns)

for year in range(1,years_to_project + 1):
      new_list = orderedColumns[-3:]
      average = cash_flow.loc[:, new_list].mean(axis=1)
      cash_flow[f'Year: {year}'] = average
      orderedColumns.append(f'Year: {year}')
