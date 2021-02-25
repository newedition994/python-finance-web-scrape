import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

url_stats = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
url_profile = 'https://finance.yahoo.com/quote/{}/profile?p={}'
url_financials = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = 'GE'

response = requests.get(url_financials.format(stock, stock))

soup = BeautifulSoup(response.text, 'html.parser')

pattern = re.compile(r'\s--\sData\s--\s')
soup.find('script', text=pattern).contents[0]

start = script_data.find("context")-2

json_data = json.loads(script_data[start:-12])

json_data['context'].keys()

dict_keys(['dispatcher', 'options', 'plugins'])

json_data['context']['dispatcher']['stores']['QuoteSummaryStore'].keys()

# income statement
annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
quaterly_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore'][
    'incomeStatementHistoryQuaterly']['incomeStatementHistory']
# cash flow
annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
quaterly_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore'][
    'cashflowStatementHistoryQuaterly']['cashflowStatements']
# balance sheet
annual_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetsStatements']
quaterly_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore'][
    'balanceSheetHistoryQuaterly']['balanceSheetsStatements']

print(annual_is[0])

annual_is[0]['operatingIncome']

annual_is_stmts = []

# consolidate annual
for s in annual_is:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
        annual_is_stmts.append(statement)


annual_is_stmts[0]

annual_cf_stmts = []
quarterly_cf_stmts = []

# annual cash flow
for s in annual_cf:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
        annual_cf_stmts.append(statement)

# quarterly cash flow
for s in quarterly_cf:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
        quarterly_cf_stmts.append(statement)

annual_cf_stmts[0]

# Profile Data
response = requests.get(url_profile.format(stock, stock))
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
soup.find('script', text=pattern).contents[0]
start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])

json_data['context']['dispatcher']['stores']['QuoteSummaryStore'].keys()

json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['assetProfile'].keys()

# Company Officers
json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['assetProfile']['companyOfficers']

# Business Summary
json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['assetProfile']['longBusinessSummary']

# SEC Filings
json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['secFilings']['filings']

# Statistics
response = requests.get(url_stats.format(stock, stock))
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
soup.find('script', text=pattern).contents[0]
start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])

json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['defaultKeyStatistics']

# Historical Stock Data
stock_url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?'

params = {
    'period1': '1582602261',
    'period2': '1614224661',
    'interval': '1d',
    'events': 'history',
    'includeAdjustedClose': true
}

params = {
    'range': '5y',
    'interval': '1d',
    'events': 'history',
    'includeAdjustedClose': true
}

response = requests.get(stock_url.format(stock), params=params)

file = StringIO(response.text)
reader = csv.reader(file)
data = list(reader)
for row in data[:5]:
    print(row)
