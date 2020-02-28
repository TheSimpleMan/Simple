import os #подключаем модуль
ask1 = input('Хотите создать папку?y/n: ')

if ask1 == 'y': 
  
    UserPath = input('Введите путь, в котором будет созадана папка: ') 
    if os.path.exists(UserPath): #проверяем существует ли введенный путь
        
        if (UserPath[-1] != "/"): # добавляем слэш, если его нету
            UserPath=UserPath+"/"
        
        DirName = input('Введите имя папки: ')
        
        if os.path.exists(UserPath+DirName):
            print ('Такая папка уже существует.')
        
        else: 
            os.mkdir(UserPath+DirName) #создаем папку
            print ('Создна папка с именем ' + DirName + ' в директории ' + UserPath)
        
        ask2 = input('Создать файл в '+UserPath+DirName+' директории?y/n: ')
        
        if ask2 == 'y':        
            FileName = input('Введите имя файла: ')
            NewDirectory = UserPath + DirName+ '/' + FileName
            
            if os.path.exists(NewDirectory):
                print ('Такой файл уже существует.')
            
            else:
                Text = input('Введите текст файла: '+ '\n')
                f = open( NewDirectory, 'w') #создание файла
                f.write(Text + '\n') #запись в  файл
                f.close()
                print ('Создан файл с именем ' + FileName + ' в директории ' + UserPath+DirName)  
            
            f = open( NewDirectory) 
            print('Содежримое файла: '+ '\n' + f.read()) #чтение файла
            f.close()
            
        else:    
            print ('Хорошо, идем дальше.')    
        
        ask3 = input('Удалим все созданные объекты?y/n: ')
        
        if ask3 == 'y': 
            os.remove(NewDirectory) #удаление файла
            os.rmdir(UserPath + DirName) # удаление папки
            print ('Данные удалены.') 
            
        else:    
            print ('Данные сохранены.')
        
    else:    
        print ('Путь не существует.')
        
else:
    print ('Ok, End.')  