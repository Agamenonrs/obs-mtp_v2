from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.http import Http404

import json
import requests
import time
import pprint
from bson.json_util import dumps


# from django.http import HttpResponse

#Realizada a conexao com o banco
client = MongoClient('mongodb://mongodb:27017')
#Definine o database a ser utilizado
db = client.obs_mtp

def buscar_dados(request):
	
	total = str(db.registro_gps.count())
	data = dumps(db.registro_gps.find_one()) 
	ultimo_registro = json.loads(data)
	print('===================== ' + str(ultimo_registro['REGISTRO']))
	#iniciar_processo()
	return render(request, 'sucesso.html', {'total': total, 'ultimo_registro' : ultimo_registro['REGISTRO'][1] })


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
	#iniciar_processo()
	return HttpResponse(rdata)

def index(request):
	return render(request, 'index.html')

def gravaRegistro():
	print ('TIME EXECUTOU')

def iniciar_processo():
	scheduler = BackgroundScheduler()
	scheduler.add_job(gravaRegistro, 'interval', seconds=10)
	scheduler.start()
