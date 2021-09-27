from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random
from datetime import datetime
from conector import mycursor
import os


def type_like_a_person(sentence, single_input_field):
    """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
    for letter in sentence:
        single_input_field.send_keys(letter)
        sleep(random.randint(1, 5) / 30)

def LoginInsta(username, pwd):
    browser.get('https://www.instagram.com/accounts/login/')
    sleep(5)

    browser.find_element_by_name('username').send_keys(username)
    sleep(6)
    browser.find_element_by_name('password').send_keys(pwd)


    # browser.find_element_by_xpath(
    #     '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    # browser.find_element_by_xpath(
    #     '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(pwd)
    sleep(3)
    browser.find_element_by_css_selector('button[type=submit]').click()
    sleep(10)

# for i in range(
#             1, 3
#         ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
#             driver.execute_script(
#                 "window.scrollTo(0, document.body.scrollHeight);")

sql_usuarios = f"SELECT * FROM users"
mycursor.execute(sql_usuarios)

users = mycursor.fetchall()
print("\033[1;42m +++++ USUARIOS CADASTRADOS +++++\033[0;0m")
for user in users:
    print('                 ')
    print(user[1])
print("\n+++++++++++++++++++")

username = input(str("🍀 Digite seu nome de usuario do instagram \n👉 "))

try:

    sql = f"SELECT * FROM users WHERE username = '{username}'"

    mycursor.execute(sql)
    data_user = mycursor.fetchall()

    if not bool(data_user):
        print(f"\033[1;41m USER '{username}' NÃO POSSUI CADASTRO NO SISTEMA \033[0;0m\n\n")
        exit()

    for user in data_user:
        user_data = {
            'id': user[0],
            'username': user[1],
            'password': user[2],
            'friends_score': user[3].split(',')
        }
    i = 1
    sql_sweepstakes = "SELECT * FROM sweepstakes"

    mycursor.execute(sql_sweepstakes)
    data_sweepstakes = mycursor.fetchall()
    os.system('cls' if os.name == 'nt' else 'clear')
    for sweepstakes in data_sweepstakes:

        print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++")

        print(f"[{sweepstakes[0]}] => \033[1;42m {sweepstakes[2]} \033[0;0m  \033[1;42m SORTEIOS DISPONIVEL\033[0;0m 💲\n")
        print(f"👤 @{sweepstakes[1]}\n")
        
        # print(f"INICIO: {datetime.__format__(sweepstakes[7], '%d/%m/%Y')} 🟢")
        # print(f"FIM: {datetime.__format__(sweepstakes[8], '%d/%m/%Y')} 🔴")

        i += 1
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n")

    choice_sweepstakes = input(str("\033[1;41m QUAL SORTEIO DESEJA CONCORRER ? \033[0;0m\n 👉 "))
    os.system('cls' if os.name == 'nt' else 'clear')

    sql_ = f"SELECT * FROM sweepstakes WHERE id = {choice_sweepstakes}"

    mycursor.execute(sql_)
    data_choice = mycursor.fetchall()

    for data in data_choice:

        user_sweepstakes = {
            'id': data[0],
            'sweepstakes_username': data[1],
            'sweepstakes_title': data[2],
            'sweepstakes_description': data[4],
            'sweepstakes_rules': data[5],
            'sweepstakes_link': data[6],
            'sweepstakes_value': data[3]
        }

        print(f"SORTEIO SELECIONADO => \033[1;42m {data[2]} \033[0;0m\n")
        #print(f"INICIO: {datetime.__format__(data[7], '%d/%m/%Y')} 🟢")
        #print(f"FIM: {datetime.__format__(data[8], '%d/%m/%Y')} 🔴\n\n\n")
        print(f"Marcar {data[5]}")
        print("\033[1;41m SIGA TODAS AS REGRAS ANTES DE COMEÇAR \033[0;0m 🤞\n\n\n")
        print(f"Link do sorteio\n\033[1;34m{data[6]}\033[0;0m\n\n\n")


    init_bot = input(str("INICIAR 🔥\n[1] SIM 🍀\n[2] CANCELAR 🔴\n👉 "))

    emj = [
        '[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]', '(^_^.)', '¯\_(ツ)_/¯', ' ´• ل •`', '•̀.̫•́✧', '(｡ŏ﹏ŏ)', '•̀.̫•́✧', '✢', '✣', '✤', '✥',
        '✦', '✧', '★', '☆', '✯', '✩', '✪', '✫', '✬', '✭', '✮', '✶', '✷', '✵', '✸'
    ]

    if(init_bot == '1'):

        browser = webdriver.Chrome()
        LoginInsta(username, data_user[0][2])
        browser.get(data_choice[0][6])
        sleep(3)
        cont = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            try:
                for x in range(0, 10):
                    # clica na barra de comentario
                    browser.find_element_by_class_name('Ypffh').click()
                    # comenta

                    sleep(4)


                    if user_sweepstakes['sweepstakes_rules'] == '1 friend':
                        
                        comentario = browser.find_element_by_class_name('Ypffh')
                        texto = f"{random.choice(emj)} @{random.choice(user_data['friends_score'])}"

                        type_like_a_person(texto, comentario)

                    if user_sweepstakes['sweepstakes_rules'] == '2 friend':

                        comentario = browser.find_element_by_class_name('Ypffh')
                        texto = f"{random.choice(emj)} @{random.choice(user_data['friends_score'])} @{random.choice(user_data['friends_score'])}"

                        type_like_a_person(texto, comentario)

                    if user_sweepstakes['sweepstakes_rules'] == '3 friend':

                        comentario = browser.find_element_by_class_name('Ypffh')
                        texto = f"{random.choice(emj)} @{random.choice(user_data['friends_score'])} @{random.choice(user_data['friends_score'])} @{random.choice(user_data['friends_score'])}"

                        type_like_a_person(texto, comentario)

                        # comentario = browser.find_element_by_class_name('Ypffh').send_keys(
                        # f"{random.choice(emj)} @{random.choice(user_data['friends_score'])} @{random.choice(user_data['friends_score'])} @{random.choice(user_data['friends_score'])}")

                    sleep(2)
                    # envia
                    browser.find_element_by_css_selector('button[type=submit]').click()
                    cont += 1
                    print(f"\033[1;42m   \033[1;97m  Total comentados {x}   \033[0;0m\n↓")
                    sleep(70)
            except:
                cont -= 1
                print(f"Algo deu errado")
                browser.refresh()
                sleep(30)
            print(f"\033[1;42m O numero de comentarios é de {cont} \033[0;0m")
            print(f"\033[1;40m   \033[1;97m  $$$ Pausa para o café ☕  $$$   \033[0;0m\n↓")
            sleep(150)




except :
    print(f"\033[1;41m BYE \033[0;0m 😉")





