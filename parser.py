import re
pattern = re.compile("\s*((?:\w(?!\s+')+|\/+|\s(?!\s*'))+\w)\s*")
tickers = []

for i, line in enumerate(open('./SnP500 Securities in Array by Year.txt', 'r')):
    for match in re.finditer(pattern, line):
        tickers.append(match.group())
#unique_tickers = list(set(tickers))
tickers = list(tickers)
securities = [ticker[:-2] + 'US Equity' for ticker in tickers]
unique_securities = set(securities)

with open('./output1.txt', "w+") as output:
    output.write(",\n".join(map(str, unique_securities)))
