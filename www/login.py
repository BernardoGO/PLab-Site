
<%
import sqlite3 as lite
import sys
from subprocess import call
import os 
import config
from server.page import html, textStyle, javascript
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.setMetaUTF8(self)
html.endHead(self)
html.beginContent(self)




os.chdir(config.__WWW_DIR__)

con = lite.connect('test.db')


login = __GET__['login'][0]
password = __GET__['password'][0]

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users WHERE login = '"+login+"' and password = '"+password+"'")

    rows = cur.fetchall()

    if len(rows) >= 1:
         javascript.redirect(self, "inicio.py")
    else:
        print u"senha inválida" #avisa que não encontrou e redireciona para a pagina do index

html.endContent(self)
html.endHtml(self)
%>

