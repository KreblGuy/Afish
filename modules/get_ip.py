try:
    import socket
    import requests
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

def get_ip(ip: str):

    try:
        ip = socket.gethostbyname(ip)
        
        infoList1 = requests.get(f"http://ipwho.is/{ip}")
        infoList = infoList1.json()
        
        if infoList.get("success"):
            print(f'{COLOR_CODE["RESET"]}╔══════════════                     ══════════════╗\n')
            print(f'     {COLOR_CODE["RESET"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Айпи адресс:{COLOR_CODE["RESET"]}  {infoList["ip"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Успех:{COLOR_CODE["RESET"]}  {infoList["success"]}  ')
            print(f'     {COLOR_CODE["RESET"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Тип:{COLOR_CODE["RESET"]}   {infoList["type"]}     ')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Континент:{COLOR_CODE["RESET"]}   {infoList["continent"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Страна:{COLOR_CODE["RESET"]}   {infoList["country"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Регион:{COLOR_CODE["RESET"]}   {infoList["region"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Город:{COLOR_CODE["RESET"]}   {infoList["city"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Почтовый код:{COLOR_CODE["RESET"]}   {infoList["postal"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Столица:{COLOR_CODE["RESET"]}  {infoList["capital"]}\n')
            print(f'{COLOR_CODE["RESET"]}╚══════════════                     ══════════════╝\n')

            
        else:
            print(f'{COLOR_CODE["RESET"]}╔══════════════                     ══════════════╗\n')
            print(f'     {COLOR_CODE["RESET"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} IP:{COLOR_CODE["RESET"]}  {infoList["ip"]}')
            print(f'     {COLOR_CODE["RESET"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Success:{COLOR_CODE["RESET"]}   {infoList["success"]}')
            print(f'     {COLOR_CODE["RED"]}[+]{COLOR_CODE["RESET"]}{COLOR_CODE["RESET"]} Message:{COLOR_CODE["RESET"]}  {infoList["message"]}')
            print(f'{COLOR_CODE["RESET"]}╚══════════════                     ══════════════╝\n')
    except Exception as e:
        print(f'An error occurred: {e}')



