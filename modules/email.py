
try: from csv import DictReader
except: print("Ой! Кажется, не все библиотеки были установлены...\n")

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

def mainget_email(file, to_find):
    with open(file, 'r', newline='', encoding='utf-8') as file:
        reader = DictReader(file)
        for row in reader:
            for i in row.items():
                try:
                    key = i[0].split(";")
                    value = i[1].split(";")
                except: pass

                try:
                    if value[8] == to_find:
                        i = 0
                        result = {}
                        try:
                            for i in range(0, key.__len__()):
                                result[str(key[i])] = value[i].strip("\"")
                        except: pass
                        return result
                    elif to_find == "afish-loop":
                        i = 0
                        result = {}
                        try:
                            for i in range(0, key.__len__()):
                                result[str(key[i])] = value[i].strip("\"")
                        except: pass
                        print(result)
                except IndexError:
                    return None

def get_email(database_file, search_value: str):
    
    data = mainget_email(database_file, search_value)                                      
    if data == None:
        print(f'{COLOR_CODE["RESET"]}[ERROR]Ты еблан? я нечего не нашел иди нахуй.')
    else:
        data = list(data.values())
        print(f"""
        {COLOR_CODE["RESET"]}[+]ID пользователя: {data[0]}
        [+]Дата регистрации: {data[1]}
        [+]Фамилия: {data[2]}
        [+]Имя: {data[3]}
        [+]Отчество: {data[4]}
        [+]Дата рождения: {data[5]}
        [+]Пол: {data[6]}
        [+]Телефон: {data[7]}
        [+]Почта: {data[8]}
        [+]Роль: {data[9]}
        [+]Класс: {data[12]}
        [+]Адрес: {data[20]}
        [+]Страна: {data[16]}
        [+]Гражданство: {data[15]}
        [+]Регион: {data[17]} 
        [+]Муниципальное образование: {data[18]}  
        [+]Наименование учреждения: {data[19]}  

                {COLOR_CODE["RESET"]}\n\n\n""")


