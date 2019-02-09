from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

import schedule
import json
import requests
import time
import pprint


# from django.http import HttpResponse

#Realizada a conexao com o banco
client = MongoClient('mongodb://mongodb:27017')
#Definine o database a ser utilizado
db = client.obs_mtp

def client(request, question_id):
	print('=====================')
	iniciar_processo()
	return render(request, 'sucesso.html')


def client2(request):
	print('=====================')
	#url = 'http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterPosicoesDaLinha/688'
	url = 'http://dadosabertos.rio.rj.gov.br/apiTransporte/apresentacao/rest/index.cfm/obterTodasPosicoes'
	resultado = ''
	response = requests.get(url)
	#Verifica se o retorno esta ok
	if response.status_code == 200:
		resultado = 'URL ATIVA'
		rdata = response.text
		data = json.loads(rdata)

		#Passa a informacao para registro
		registro = {'REGISTRO' : data['DATA']}
		#Adiciona o atributo DATA_ATUALIZACAO ao json
		registro['REGISTRO'].append( {'DATA_ATUALIZACAO' : datetime.now().strftime('%m-%d-%Y %H:%M:%S') } )

		#Define a collection a ser utilizada(se nao existir cria)
		collection = db.registro_gps
		collection.insert_one(registro)
	#schedule.every(1).minutes.do(gravaRegistro)
	#schedule.every(5).seconds.do(gravaRegistro)#funcionou
	#cron()
	#iniciar_processo()
	return HttpResponse(rdata)

def index(request):
	return render(request, 'index.html')

def gravaRegistro():
	print ('TIME EXECUTOU')

def cron():
	while True:
		schedule.run_pending()
		time.sleep(1)
def iniciar_processo():
	scheduler = BackgroundScheduler()
	scheduler.add_job(gravaRegistro, 'interval', seconds=10)
	scheduler.start()
