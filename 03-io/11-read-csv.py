import csv


def str_to_float(s):
    return float(s.replace(',', ''))


# read table by rows:
with open('数据透视表.csv', newline='', encoding='cp936') as csvfile:
    csvreader = csv.reader(csvfile)
    table = list(csvreader)

for row in table[:5]:
    print(row)


print('-'*80)


# read table to dict:
with open('数据透视表.csv', newline='', encoding='cp936') as csvfile:
    csvreader = csv.DictReader(csvfile)
    table = list(csvreader)

for row in table[:5]:
    print(
        row['订购日期'],
        row['产品类别'],
        round(str_to_float(row['销售额']) - str_to_float(row['成本']), 2)
    )

