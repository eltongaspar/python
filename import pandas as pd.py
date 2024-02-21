import pandas as pd

# Ler o arquivo Excel
dataframe = pd.read_excel('D:\Dados\Extrato_20210101_20210131.xls')
dataframe = pd.read_excel('D:\Dados\Extrato_20220101_20220131.xls')
dataframe = pd.read_excel('D:\Dados\Extrato_20230101_20230131.xls')

# Exibir os dados
print(dataframe)