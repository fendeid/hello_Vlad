# -*- coding: utf-8 -*- 
import os

# Значение 1 считает пустые строки, Значение 2 без них
turn = 1
# Путь со скриптом.(начальная директория)
script_direct = __file__[0 : __file__.find(os.path.basename(__file__))]
print()
def bust_script(direct):	
	# Если директория не пустая	
	if os.listdir(direct) != '':			
		for obj in os.listdir(direct):
			# Обновляем количество строк для каждого файла
			strings = 0	
			# Если объект является директорией
			if os.path.isdir(direct + obj) == True:	
				# Задается новая директория, рекурсивная функция.				
				new_direct = direct + obj + '\\'
				bust_script(new_direct)	
			# Если объект является файлом
			elif os.path.isfile(direct + obj) == True:
				try:
					#Файл открывается для чтения
					with open(direct + obj, 'r', encoding = 'utf-8') as file:
						for line in file:	
							if turn == 1:	
								strings += 1
							elif turn == 2:							
								for line in file:
									if file.readline != '\n' and file.readline != '':
										strings += 1
				except:
					pass
			# Вывод 	
			if os.path.isfile(direct + obj) == True:
				print('Директория:',direct,'\nИмя:',obj,'\nКоличество строк:', strings)	
				print('-------------------')
	# Если директория пустая
	else:
		print('Директория:',direct,'\nСтатус: Пуста')
		print('-------------------')	
	
bust_script(script_direct)