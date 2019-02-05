O projeto pode ser executado direto na maquindo do usuário
ou Através de containers com o Docker

DIRETO NA MAQUINA (UBUNTU 16.04) - A instalação foi realizado no UBUNTU 16.04
com a versao 3.5 do Python. Nada impede a instação em outra versão mas deve-se 
atentar para as alteração de versoes das das aplicações de suporte.

Inportante: 
Instalar o virtualenv, pip
sudo apt-get install python3-pip
sudo pip3 install virtualenv

O banco de dados do projeto é o mongodb
(O mesmo deve estar instalado). 
Realizar a configuração do banco e apontamento da aplicação para o banco.

1- Baixar o projeto obs-mtp_v2
2- Entrar no diretorio 
   cd obs-mtp_v2
3- configurar a versão do python para o diretorio
   virtualenv -p python3.5 .
4- startar o ambiente virtual
    source obs-bin/activate
5- já dentro do ambiente virtual configurar as dependencias atraves
do arquivo requirements.txt
   pip install -r requirements.txt
6- start o projeto
   cd obs_mtp && python manage.py runserver
7- apos as configurações do tutorial testar a nova url
   http://127.0.0.1:8000/client_rest/
8- Para sair da aplicacao 
   CTRL + C 
9- Para sair do ambiente virtual 
   deactivate





---========================== --

INSTALAÇÃO UTILIZANDO O DOCKER
Importante: O Docker e o docker compose já devem estar instalados.
Este procedimento já constroi o container da aplicação e o container do 
banco de dados.
O diretorio do projeto(obs_mtp) será criado como volume do container da aplicação.



1- Baixar o projeto obs-mtp_v2
2- Entrar no diretorio 
   cd obs-mtp_v2
3- Alterar o local de criação do volume do banco de dados
   No arquivo docker-compose.yml.
   mongodb:
    image: mongo
    volumes: 
      - [ UM LOCAL NA SUA MAQUINA ]:/data/db
4- Realizar o build para constribuir as imagens
   docker-compose build
5- Levantar os containers. Serão criados os containers: web_obsmtp e mongodb_obsmtp 
   docker-compose up
6- Visualizar se os contairs estão no ar.
   docker ps




tutorial base
https://docs.djangoproject.com/en/2.1/intro/tutorial01/
versão do python 3.5
versão do django 2.1

PROCEDIMENTO PARA UTILIZACAO DO DOCKER
IMPORTANTE O DOCKER JÁ DEVE ESTAR INSTALADO






