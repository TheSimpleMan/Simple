import os 

UserPath = input('Введите путь: ') 

def get_size(start_path = '.'): #функция для подсчета суммарного веса файлов в каталоге, взят из http://python.su/forum/topic/22115/?page=1#post-113774
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

 
if os.path.exists(UserPath):

    print('{:<40} {:<15} {:<10}'.format('Имя', 'Тип', 'Размер'))
    
    for File in os.listdir(UserPath):  
                
        if os.path.islink(UserPath+os.path.basename(File)):
            print('{:<40} {:<15} {:<10}'.format(os.path.basename(File), "Ссылка", str(os.path.getsize(UserPath+os.path.basename(File)))+' байт'))
            continue
            
        elif os.path.isdir(UserPath+os.path.basename(File)):
            DirSize = get_size(UserPath+os.path.basename(File))
            print('{:<40} {:<15} {:<10}'.format(os.path.basename(File), "Папка", str(DirSize)+ ' байт'))
            
        elif os.path.isfile(UserPath+os.path.basename(File)):
            print('{:<40} {:<15} {:<10}'.format(os.path.basename(File), "Файл", str(os.path.getsize(UserPath+os.path.basename(File)))+' байт')) 
         
else:
    print ('Путь не существует.')
