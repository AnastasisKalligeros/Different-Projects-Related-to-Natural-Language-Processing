import nltk
import sqlite3
grammar = nltk.data.load('gr_voc.fcfg')
from nltk import load_parser
cp = load_parser('gr_voc.fcfg')
query = 'who loves book'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)
query='who watch tv'
trees = list(cp.parse(query.split()))
answer = [s for s in answer if s]
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)
sqliteConnection = sqlite3.connect('C:/Users/tasso/Desktop/EPEXERGASIAFYSIKHSGLWSSAS/Knowledge.db')
cursor = sqliteConnection.cursor()
cursor.execute(q+';')
records = cursor.fetchall()
for row in records:
 print(row[0])
sqliteConnection.close()