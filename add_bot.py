from conector import mycursor, mydb

change = input(str("ADICIONAR:\n[1] NOVO SORTEIO\n[2] NOVO USUARIO\n\n👉 "))

if change == '1':
    sweepstakes_username = input(str("DIGITE O @ DO PERFIL QUE ESTÁ SORTEANDO\n👉 "))
    sweepstakes_title = input(str("DIGITE O TITULO DO SORTEIO:\n👉 "))
    sweepstakes_value = input(str("DIGITE O VALOR OU PRODUTO QUE ESTÁ SENDO SORTEADO:\n👉 "))
    sweepstakes_description = input(str("DIGITE O DESCRIÇÃO DO SORTEIO:\n👉 "))
    sweepstakes_rules = input(str("DIGITE O REGRAS DO SORTEIO:\n[1] 1 amigo\n[2] 2 amigos\n[3] 3 amigos\n 👉 "))
    sweepstakes_link = input(str("DIGITE O LINK DO SORTEIO:\n👉 "))

    if(sweepstakes_rules == '1'):
        sweepstakes_rules = '1 friend'
     
    elif(sweepstakes_rules == '2'):
        sweepstakes_rules = '2 friend'    

    elif(sweepstakes_rules == '3'):
        sweepstakes_rules = '3 friend'  
    
    
    sql = f"INSERT INTO `bot_instagram`.`sweepstakes` (`sweepstakes_username`, `sweepstakes_title`, `sweepstakes_value`, `sweepstakes_description`, `sweepstakes_rules`, `sweepstakes_link`) VALUES ('{sweepstakes_username}','{sweepstakes_title}','{sweepstakes_value}','{sweepstakes_description}','{sweepstakes_rules}','{sweepstakes_link}')"
    print(sql)

    mycursor.execute(sql)
    mydb.commit()

elif change == '2':

    username = input(str("DIGITE O NOME DO NOVO USUARIO DO SISTEMA:\n👉 "))
    password = input(str("DIGITE A SENHA:\n👉"))
    friends = input(str("DIGITE OS AMIGOS QUE DESEJA MARCAR SEPARADOS POR VIRGULA (SEM ESPAÇOS):\n👉"))

    sql = f"INSERT INTO users (username, password, friends_score) VALUES ('')"

    print(sql)
    exit()
    # val = ("John", "Highway 21")
    # mycursor.execute(sql, val)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record inserted.")