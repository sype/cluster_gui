__author__ = 'sype'
import MySQLdb


db = MySQLdb.connect(host="10.7.20.3", # your host, usually localhost
                     user="spincemail", # your username
                     passwd="Seb4sB9oXx", # your password
                     db="information_schema") # name of the data base


db2 = MySQLdb.connect(host="10.7.20.4", # your host, usually localhost
                     user="spincemail", # your username
                     passwd="Seb4sB9oXx", # your password
                     db="information_schema") # name of the data base
