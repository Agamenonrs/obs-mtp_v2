from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.http import Http404
from bson.json_util import dumps

import json
import requests
import time
import pprint
import sys


# from django.http import HttpResponse

#Realizada a conexao com o banco
client = MongoClient('mongodb://mongodb:27017')
#Definine o database a ser utilizado
db = client.obs_mtp

def form_iniciar(request):
	return render(request, 'iniciar_busca.html')

def exibe_ultimo_registro(request):
	
	total = str(db.registro_gps.count())
	data = db.registro_gps.aggregate([{'$group':{'_id': 1,'ultima_data':{'$max': '$DATA_ATUALIZACAO'}}}])
	d = dumps(data)
	ultimo_registro = json.loads(d)
	print('===================== ' + str(ultimo_registro[0]['ultima_data']))
	return render(request, 'sucesso.html', {'total': total, 'ultimo_registro' : str(ultimo_registro[0]['ultima_data']) })


def buscar_dados(request):
	iniciar_processo()
	total = str(db.registro_gps.count())
	data = dumps(db.registro_gps.find_one()) 
	ultimo_registro = json.loads(data)
	data_atualizacao = str(ultimo_registro['DATA_ATUALIZACAO'])
	print('===================== ' + str( data_atualizacao))
	return render(request, 'sucesso.html', {'total': total, 'ultimo_registro' : data_atualizacao })

def index(request):
	return render(request, 'index.html')

def gravaRegistro():
	try:
		print ('Processo executando...')
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
			registro = {'REGISTRO' : data['DATA'],'DATA_ATUALIZACAO' : datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
			#Adiciona o atributo DATA_ATUALIZACAO ao json
			#Define a collection a ser utilizada(se nao existir cria)
			collection = db.registro_gps
			collection.insert_one(registro)
	except Exception as e:
		collection = db.erro_log
		erro = {'data' :  str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')), 'mensagem_erro' : str(e)}
		collection.insert_one(erro)


def iniciar_processo():
	scheduler = BackgroundScheduler()
	scheduler.add_job(gravaRegistro, 'interval', minutes=2)
	scheduler.start()
