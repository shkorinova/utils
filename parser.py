import re
pattern = re.compile("\s*((?:\w(?!\s+')+|\/+|\s(?!\s*'))+\w)\s*")
tickers = []

for i, line in enumerate(open('./your_file_name.txt', 'r')):
    for match in re.finditer(pattern, line):
        tickers.append(match.group())
unique_tickers = list(set(tickers))
unique_securities = [ticker + ' Equity' for ticker in unique_tickers]

with open('./output.txt', "w+") as output:
    output.write(", ".join(map(str, unique_securities)))
