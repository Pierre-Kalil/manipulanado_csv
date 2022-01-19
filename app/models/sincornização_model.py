import pandas as pd
import csv
import os

'''
A função merge_files_csv faz a varredura no diretorio selecionado em busca de todos os
arquivos de extensão .csv e em seguida mescla todos ele em um unico arquivo.
'''

def merge_files_csv():
    master_df = pd.DataFrame()
    for file in os.listdir(os.getcwd()):
        if file.endswith('.csv'):
            master_df = master_df.append(pd.read_csv(file))

    master_df.to_csv('master_file.csv', index=False, sep=';')


'''
A função verify_master_file faz a leitura de todas as linhas do arquivo master_file.csv
e verifica se os campos atendem as especificações necessárias:
agencia: precisa ter 4 digitos
conta: precisa ter 7 digitos
status: precisa ser dos tipos ["A", "I", "B", "P"]
'''

def verify_master_file():
    merge_files_csv()
    
    tipos = ["A", "I", "B", "P"]
    with open('master_file.csv', 'r') as f:
        rows = csv.reader(f, delimiter=';')
        count = 0
        for row in rows:
            if count == 0:
                count += 1
            else:
                if len(row[0])!= 4 or len(row[1]) != 7 or row[3] not in tipos:
                    print(row, 'Dados incorretos')
