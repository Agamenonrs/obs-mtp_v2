passo a passo para criacao

1- criar diretorio raiz ex. obs-mtp
   
2- Entrarno diretorio 
   cd obs-mtp
3- configurar a versão do python para o diretorio
   virtualenv -p python3.5 .
4- startar o ambiente virtual (dentro do diretorio obs-mtp)
    source /bin/activate
5- já dentro do ambiente virtual configurar as dependencias atraves
do arquivo requirements.txt
   pip install -r requirements.txt

6- Para criar o projeto
   django-admin startproject obs_mtp

7- start o projeto
   python manage.py runserver
8- Para criar uma app dentro do projeto bastar executar o comando
   python manage.py startapp "nome da app"
   python manage.py startapp client_rest
9- apos as configurações do tutorial testar a nova url
   http://127.0.0.1:8000/client_rest/


--========================== --

tutorial base
https://docs.djangoproject.com/en/2.1/intro/tutorial01/
versão do python 3.5
versão do django 2.1

PROCEDIMENTO PARA UTILIZACAO DO DOCKER
IMPORTANTE O DOCKER JÁ DEVE ESTAR INSTALADO






