import os #подключаем модуль
UserPath = input('Введите путь: ') #запрашиваем путь
 
if os.path.exists(UserPath): #проверяем существует ли введенный путь

    print('{:<40} {:<40}'.format('Имя', 'Тип')) # рисуем шапку таблицы
    
    for File in os.listdir(UserPath): # цикл, смотрящий все объекты в пути
                
        if os.path.islink(UserPath+os.path.basename(File)): # проверяем является ли объект ссылкой
            print('{:<40} {:<40}'.format(os.path.basename(File), "Ссылка")) #печатаем инфу в два столбца
            continue
            
        elif os.path.isdir(UserPath+os.path.basename(File)):
            print('{:<40} {:<40}'.format(os.path.basename(File), "Папка"))
            
        elif os.path.isfile(UserPath+os.path.basename(File)):
            print('{:<40} {:<40}'.format(os.path.basename(File), "Файл"))                
        
         
else:
    print ('Путь не существует.')
