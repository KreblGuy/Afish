
try:
    from pystyle import *
except: print("Ой! Кажется, не все библиотеки были установлены...\n")

banner = '''
   
         ░█████╗░███████╗██╗░██████╗██╗░░██╗
         ██╔══██╗██╔════╝██║██╔════╝██║░░██║
         ███████║█████╗░░██║╚█████╗░███████║
         ██╔══██║██╔══╝░░██║░╚═══██╗██╔══██║
         ██║░░██║██║░░░░░██║██████╔╝██║░░██║
         ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝

                TGK: @gold_afish | BETA 0.2V\n\n'''

menu = '''               Main Menu
              ╔============================╗
              ║[1] Пробив по номеру        ║
              ║[2] Пробив по почте         ║
              ║[3] Пробив по IP            ║
              ║[4] DDoS Атака              ║
              ║[5] Пробив по машине        ║
              ║[6] Выход из софта          ║ 
              ╚============================╝\n\n'''


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

module_error = "Упс! Сбои в системе модулей...\n"

database_file = './database/AkumaNumber.csv'

def action1_number() -> None:
    """> Первая опция меню 'Пробив по номеру'"""
    try: from modules.phone import get_number
    except: print(module_error)

    search_value = input(f'{COLOR_CODE["RESET"]}[@]Введите номер телефона:')
    get_number(database_file, search_value)

def action2_mail() -> None:
    """> Вторая опция меню 'Пробив по почте'"""
    try: from modules.email import get_email
    except: print(module_error)

    search_value = input(f'{COLOR_CODE["RESET"]}[@]Введите почту:')
    get_email(database_file, search_value)

def action3_ip() -> None:
    """> Третья опция меню 'Пробив по IP'"""
    try: from modules.get_ip import get_ip
    except: print(module_error)

    ip = input(f'{COLOR_CODE["RESET"]}[@]Введите айпи:' )
    get_ip(ip)

def action4_ddos() -> None:
    """> Четвертая опция меню 'DDoS Атака'"""
    try: from modules.ddos import dos
    except: print(module_error)

    link = input('Введите ссылку: ')
    dos(link)

def action5_car() -> None:
    """> Пятая опция меню 'Пробив по машине'"""
    print('бля чувак я не додумался до этого еще, терпи...')

def action6_exit() -> None:
    """> Шестая опция меню 'Выйти из софта'"""
    exit()

def help_func() -> None:
    """> Вызывает главное меню"""
    print(Colorate.Horizontal(Colors.black_to_white,Center.XCenter(menu)))

main_menu = {
    "1": action1_number,
    "2": action2_mail,
    "3": action3_ip,
    "4": action4_ddos,
    "5": action5_car,
    "6": action6_exit,
    "exit": action6_exit,
    "help": help_func
}

def main() -> None:

    print(Colorate.Horizontal(Colors.black_to_white,Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.black_to_white,Center.XCenter(menu)))

    stop = True
    while stop:
        choice = input(f'{COLOR_CODE["URL_L"]}[+]{COLOR_CODE["RESET"]} Выбрать >{COLOR_CODE["RESET"]} ')

        success = False
        for key, value in main_menu.items():
            if str(choice).lower() in key:
                success = True
                value()

        if not success: print(f'{COLOR_CODE["URL_L"]}[!]{COLOR_CODE["RESET"]} Кажется... такого выбора нету.{COLOR_CODE["RESET"]}\n')

if __name__ == "__main__":
    main()
