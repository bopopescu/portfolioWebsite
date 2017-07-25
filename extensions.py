import pymysql
import pymysql.cursors
import config
from flask import session

def connect_to_database():
  options = {
	'host': config.env['host'],
	'user': config.env['user'],
	'passwd': config.env['password'],
	'db': config.env['db'],
	'cursorclass' : pymysql.cursors.DictCursor
  }
  db = pymysql.connect(**options)
  db.autocommit(True)
  return db

db = connect_to_database()

def query(query):
	global db
	cur = db.cursor()
	cur.execute(query)
	response = cur.fetchall()
	cur.close()
	return response


def authenticate(options):
	if 'username' in session:
		options['logged_in']= True
		options['user'] = session['username']
	return options
