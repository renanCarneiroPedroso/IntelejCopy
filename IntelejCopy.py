from dateutil import relativedelta
from datetime import datetime
from Modulos.Core import verifyFiles
from os import walk,path
from time import sleep

print("""
#   /$$$$$$             /$$               /$$ /$$            /$$$$$$                               
#  |_  $$_/            | $$              | $$|__/           /$$__  $$                              
#    | $$   /$$$$$$$  /$$$$$$    /$$$$$$ | $$ /$$ /$$      | $$  \__/  /$$$$$$   /$$$$$$  /$$   /$$
#    | $$  | $$__  $$|_  $$_/   /$$__  $$| $$| $$|__/      | $$       /$$__  $$ /$$__  $$| $$  | $$
#    | $$  | $$  \ $$  | $$    | $$$$$$$$| $$| $$ /$$      | $$      | $$  \ $$| $$  \ $$| $$  | $$
#    | $$  | $$  | $$  | $$ /$$| $$_____/| $$| $$| $$      | $$    $$| $$  | $$| $$  | $$| $$  | $$
#   /$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$| $$| $$      |  $$$$$$/|  $$$$$$/| $$$$$$$/|  $$$$$$$
#  |______/|__/  |__/   \___/   \_______/|__/|__/| $$       \______/  \______/ | $$____/  \____  $$
#                                           /$$  | $$                          | $$       /$$  | $$
#                                          |  $$$$$$/                          | $$      |  $$$$$$/
#                                           \______/                           |__/       \______/ 
#                                                                                                                                                                                                 
\n\n
""")

# Recebendo os parametros do usuário
pathSource = str(input('\nDIGITE O CAMINHO ORIGINAL: '))+'/' # Caminho fonte
pathDestiny = str(input('\nDIGITE O CAMINHO DE DESTINO: '))+'/' # Caminho Destino
fileExtension = str(input('\nDIGITE A EXTENÇÃO DO ARQUIVO: ')) # Extenção Desejada
daysParam = int(input('\nDIGITE A QUANTIDADE DE DIAS RETROATIVOS: '))
daysParam = (datetime.now() - relativedelta.relativedelta(days=daysParam)).date() # Responsavel por fazer a substração do momento atual - o parametro passado
folderJSON = str(input('\nDIGITE O CAMINHO PARA SALVAR O RELATÓRIO: '))+'/' # Extenção Desejada

print('\nPROCURANDO POR ARQUIVOS COM A DATA DE MODIFICAÇÃO >= {} COM {}, POR FAVOR AGURADE...'.format(
                                                                                                    daysParam,
                                                                                                    'TODOS OS FORMATOS' if fileExtension == '*' else 'A EXTENSÃO %s'%fileExtension.upper()))

sleep(10)
# Chamando a função principal
verifyFiles(fileExtension=fileExtension,pathSource=pathSource,pathDestiny=pathDestiny,daysParam=daysParam,folderJSON=folderJSON)
