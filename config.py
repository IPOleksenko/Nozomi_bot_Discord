from os import getenv

TOKEN = getenv("API_TOKEN")
NAME_NOZOMI = 'Nozomi_bot_Discord'
SERVER_ID = getenv("SERVER_ID")
SERVER_STARTER_CHANNEL= int(getenv("SERVER_STARTER_CHANNEL"))
STANDART_LANGUAGE_USER = str(getenv('STANDART_LANGUAGE_USER')) # en(English) or ru(Russian)
Hello= ["Hello, world!", "Hello, Nozomi!"]
Hello_Admine= ["Hello, IPOleksenko!"]
FATHER_NAME_COMMAND= ['Nozomi, кто твой папочька?', 'Nozomi, кто тебя сделал?', 'Nozomi, покажи создателя', 'Nozomi, who is your daddy?', 'Nozomi, who is created you?', 'Nozomi, show your creator']
FATHER_NAME= "<@!328871610364854273>"
STARTER_ROLE= int(getenv("STARTER_ROLE"))
BAN_WORDS = {}

DATABASE_URL = getenv('DATABASE_URL')
#Author: IPOleksenko