from Income_Statement import *
from Balance_Sheet import *
from Cash_Flow import *


def FCF(nextPeriod,currentPeriod, IS, BS):
    CF_forecast = {}
    CF_forecast[nextPeriod] = {}

    CF_forecast[nextPeriod]['netIncome'] = IS[nextPeriod]['netIncome']
    CF_forecast[nextPeriod]['inc_depreciation'] = IS[nextPeriod]['depreciationAndAmortization'] - IS[currentPeriod]['depreciationAndAmortization']
    CF_forecast[nextPeriod]['inc_receivables'] = BS[nextPeriod]['netReceivables'] - BS[currentPeriod]['netReceivables']
    CF_forecast[nextPeriod]['inc_inventory'] = BS[nextPeriod]['inventory'] - BS[currentPeriod]['inventory']
    CF_forecast[nextPeriod]['inc_payables'] = BS[nextPeriod]['accountPayables'] - BS[currentPeriod]['accountPayables']
    CF_forecast[nextPeriod]['CF_operations'] = CF_forecast[nextPeriod]['netIncome'] + CF_forecast[nextPeriod]['inc_depreciation'] + (CF_forecast[nextPeriod]['inc_receivables'] * -1) + (CF_forecast[nextPeriod]['inc_inventory'] * -1) + (CF_forecast[nextPeriod]['inc_payables'] * -1)
    CF_forecast[nextPeriod]['CAPEX'] = BS[nextPeriod]['propertyPlantEquipmentNet'] - BS[currentPeriod]['propertyPlantEquipmentNet'] + IS[nextPeriod]['depreciationAndAmortization']

    CF_forecast[nextPeriod]['FCF'] = CF_forecast[nextPeriod]['CAPEX'] + CF_forecast[nextPeriod]['CF_operations']

    return CF_forecast[nextPeriod]



'''historicalPeriods = orderColumns(columns)
print(historicalPeriods)
for period in historicalPeriods:'''

print(FCF('Year: -2', 'Year: -1', income_statement, balance_sheet))
print(FCF('Year: -1', 'Year: 0', income_statement, balance_sheet))
print(FCF('Year: 1', 'Year: 1', income_statement, balance_sheet))
print(FCF('Year: 2', 'Year: 3', income_statement, balance_sheet))

