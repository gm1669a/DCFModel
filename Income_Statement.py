from basics import *

# stops DF from truncating
pd.options.display.max_columns = 40
pd.options.display.width = 500
columns = [f'Year: 0']

income_statement = pd.DataFrame.from_dict(annual_income_statement[0], orient='index')
income_statement = income_statement[8:36]
income_statement.columns = [f'Year: 0']

for year in range(1, years):
      income_statement[f'Year: -{year}'] = pd.DataFrame.from_dict(annual_income_statement[year], orient='index')
      columns.append(f'Year: -{year}')
orderedColumns = orderColumns(columns)
income_statement = income_statement.reindex(columns = orderedColumns)

for year in range(1,years_to_project + 1):
      new_list = orderedColumns[-3:]
      average = income_statement.loc[:, new_list].mean(axis=1)
      income_statement[f'Year: {year}'] = average
      orderedColumns.append(f'Year: {year}')
