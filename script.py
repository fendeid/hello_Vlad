# -*- coding: utf-8 -*- 
import os

def files():
	'''Подсчет не пустых файлов в ТЕКУЩЕМ каталоге.'''	
	#Список не пустых файлов.
	filelist = [ ]
	#Обозначаем дерикторию	
	location = __file__[0 : __file__.find(os.path.basename(__file__))]
	print(location)	
	#Перебираем объекты в дериктории		
	for obj in os.listdir(location):			
		strings = 0			
		try:
			with open(location + obj, 'r') as file:			
				for string in file:				
					if file.readline() != '':
						strings += 1
				filelist.append([obj, strings])
		except:
			pass	

	return filelist
#Присвоили список
filelist = files()

def statistic(f):
	'''Вывод статистики'''	
	for file in f:
		print('\tName:', file[0], '\tStrings:',file[1])
statistic(filelist)







