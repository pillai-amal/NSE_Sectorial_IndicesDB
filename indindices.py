import os
import pandas as pd
import sqlite3

con = sqlite3.connect('/mnt/c/Users/pillai_amal/indindices.db')
cur = con.cursor()
cur.execute(f"CREATE TABLE indexlist (ticker TEXT, indice TEXT, industry TEXT)")

for file in os.listdir():
    if file.endswith('csv'):
        df = pd.read_csv(file)
        index_name = file[4:]
        index_name = index_name.replace("list.csv","").upper()
        for indx in df.index:
             cur.execute(f"INSERT INTO indexlist VALUES ('{df['Symbol'][indx]}', '{index_name}', '{df['Industry'][indx]}')")
             con.commit()