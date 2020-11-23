import os
import sys
from datetime import datetime
from os import walk,path
from time import sleep
from shutil import copy
from json import dump
from re import sub

# Função para pegar a data de modificação de um arquivo
def modification_date(filename):
	t = path.getmtime(filename)
	return datetime.fromtimestamp(t)

# Função para criação da pasta no caminho de destino, caso não exista
def makeFolder(path):
	if not os.path.exists(path):
		os.makedirs(path)

# Função para a criação de um relatório em JSON
def makeReport(dictErros, folderDestiny):
	nameFile = 'IntelejCopyReport-{}.json'.format(sub('\W','-',str(datetime.now().replace(microsecond=0))))
	with open(folderDestiny+nameFile, 'w') as fp:
		dump(dictErros, fp)


# Função principal que vai gerenciar o processo como um todo
def verifyFiles(fileExtension, pathSource, pathDestiny, daysParam, folderJSON):
	errors = []
	for root, dirs, files in walk(pathSource, topdown=False):
		try:
			for fileName in files:
				if fileExtension == '*':
					if (modification_date(root+'/'+fileName).date() >= daysParam): # Caso a data de modificação sendo maior ou igual a regra...
						remoteFolder = pathDestiny+'/'+root[len(pathSource):]+'/' # Concatenando a pasta destino com as pastas remotas de onde está o arquivo
						de = root+'/'+fileName
						para = remoteFolder+fileName
						print("REALIZANDO COPIA\nDE:{}\nPARA:{}\n".format(de,para))
						makeFolder(remoteFolder) # Criando a pasta remota
						copy(root+'/'+fileName,remoteFolder+fileName) # Copiando o arquivo
						print('CONCLUIDO COM SUCESSO\n')
									
				else:
					if (fileName.endswith(fileExtension)) and (modification_date(root+'/'+fileName).date() >= daysParam): # Caso a extenção esteja de acordo, bem como a data de modificação sendo maior ou igual a regra...
						remoteFolder = pathDestiny+'/'+root[len(pathSource):]+'/' # Concatenando a pasta destino com as pastas remotas de onde está o arquivo
						de = root+'/'+fileName
						para = remoteFolder+fileName
						print("REALIZANDO COPIA\nDE:{}\nPARA:{}\n".format(de,para))
						makeFolder(remoteFolder) # Criando a pasta remota
						copy(root+'/'+fileName,remoteFolder+fileName) # Copiando o arquivo
						print('CONCLUIDO COM SUCESSO\n')
		except Exception as e:
			# Inserindo no direcionario de erros
			errors.append(
						{
							'file':str(fileName),
							'error': str(e)
						}
						)
			continue
	print('EXPORTANDO RELATÓRIO')
	makeReport(errors,folderJSON) # Exportando o relatório
			