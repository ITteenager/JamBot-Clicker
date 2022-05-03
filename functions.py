from aiogram import Bot, Dispatcher, executor, types
import sqlite3
from config import sum
from main import wallet_p2p

connection = sqlite3.connect('data.db')
q = connection.cursor()


def toFixed(numObj, digits=0):
	return f"{numObj:.{digits}f}"

def first(chat_id):
	q.execute(f"SELECT * FROM users WHERE user_id = {chat_id}")
	result = q.fetchall()
	if len(result) == 0:
			q.execute(f"INSERT INTO users (user_id, balance)"
						f"VALUES ('{chat_id}', '0')")
			connection.commit()

def pay(chat_id):
	invoice = wallet_p2p.create_invoice(value=sum)
	link = invoice['payUrl'] 
	bid = invoice['billId']
	sql = "UPDATE users SET bd = ? WHERE user_id = ?"
	data = (bid, chat_id)
	q.execute(sql, data)
	connection.commit()
	return link
