import os

from main import *
from Income_Statement import *
from Balance_Sheet import *
from Cash_Flow import *
from Free_Cash_Flows import *

#needs 5 represent 2022- needs to be adjusted
discountedCashFlow = pd.DataFrame.from_dict(discount_cash_flow[5], orient='index')
wacc = discountedCashFlow.at['wacc', 0]

FCF_List = CF_forecast.iloc[-1]

print(FCF_List)