<html>
<body>

<%
import sqlite3 as lite
import sys
from subprocess import call
import os 
import config

os.chdir(config.__WWW_DIR__)

con = lite.connect('test.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users")

    rows = cur.fetchall()

    for row in rows:
        print row

%>

</body>
</html>







