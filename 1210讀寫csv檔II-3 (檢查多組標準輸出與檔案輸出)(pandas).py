import pandas as pd  

n = str(input())
s0 = pd.read_csv('./stores_old' + n + '.csv', encoding='big5')
s1 = s0[["sid", "name", "tel", "wifi"]]
s1.to_csv('stores_new' + n + '.csv', encoding = 'utf8')