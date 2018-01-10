# coding:utf8

import sqlite3

con = sqlite3.connect('../../myweb.db')

print con

cur = con.cursor()

print cur

# sql_str = 'insert into User (user_id, name) values ("qwq21f","xiali")'
sql_str = 'select *from User'
d = 'select from'

e = cur.execute(sql_str)
# con.commit()
# con.close()


print e

for i in e:
    print i[0]
    print i[1]
