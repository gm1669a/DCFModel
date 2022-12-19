#Attributions
#Data provided by Financial Modeling Prep
#https://financialmodelingprep.com/developer/docs/

#https://www.youtube.com/watch?v=XCMsdi3CLGA&t=893s

import requests
import matplotlib
import pandas as pd
import sys
import numpy

api_key = 'deb2b6ddd1894231c4a3767ebd1306a4'

company = input(f"Enter company ticker:\n").upper()
years = 3
years_to_project = 3

annual_income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
annual_balance_sheet = requests.get(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}")
annual_cash_flow = requests.get(f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{company}?limit={years}&apikey={api_key}")
current_share_price = requests.get(f"https://financialmodelingprep.com/api/v3/quote-short/{company}?limit={years}&apikey={api_key}")
discount_cash_flow = requests.get(f"https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={company}&apikey={api_key}")

annual_income_statement = annual_income_statement.json()
annual_balance_sheet = annual_balance_sheet.json()
annual_cash_flow = annual_cash_flow.json()
current_share_price = current_share_price.json()
discount_cash_flow = discount_cash_flow.json()

'''print(annual_income_statement[0]['revenue'])
print(annual_balance_sheet[0]['totalCurrentAssets'])
print(annual_cash_flow[0]['netIncome'])
print(current_share_price[0]['price'])'''

def orderColumns(a):
    intList = []
    for element in a:
        new_string = element.replace('Year: ', "")
        new_string = int(new_string)
        intList.append(new_string)

    intList.sort()
    orderedColumns = []

    for element in intList:
        new_element = str(element)
        new_element = 'Year: ' + new_element
        orderedColumns.append(new_element)

    return orderedColumns




def calcGrowth(a, b):
    #calcualtes the growth rates for each line item y/y
    #a = statement
    #b = line item
    rates = []
    for year in range(years):
        currentYear = a[year][b]
        previousYear= a[year - 1][b]
        growth = (previousYear - currentYear) / currentYear
        rates.append(growth)
    rates.__delitem__(0)
    return rates

def aveGrowth(l):
    #calculates the average of the growth rates for each line item y/y
    return sum(l) / len(l)

