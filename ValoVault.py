"""
VALOVAULT

Aplicação de gestão de skins do videojogo Valorant, desenvolvido por Riot Games

Trabalho realizado por:
    - Mónica Santos
"""

import sys
import subprocess
import os
import database as db


def main():

    cnx, cursor = db.iniciar()

    clear_screen()
    menu_inicial(cnx, cursor)

#------------------------------- MENU INICIAL ----------------------------------#

def menu_inicial(cnx, cursor):

    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'VALOVAULT':>12}{'*':>39}")
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{1:>5}{' - Coleção'}{'*':>36}")
    print(f"{'*'}{2:>5}{' - Wishlist'}{'*':>35}")
    print(f"{'*'}{'E':>5}{' - Encerrar'}{'*':>35}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    op = input("OPCAO > ").upper()

    match op:

        case '1':
            clear_screen()
            menu_colecao(cnx, cursor)

        case '2':
            clear_screen()
            menu_wishlist(cnx, cursor)

        case 'E':
            clear_screen()
            db.fechar(cnx, cursor)
            sys.exit(2)

        case _:
            clear_screen()
            print("Opção Inválida")
            pause()

            clear_screen()
            menu_inicial(cnx, cursor)

#------------------------------- MENU COLEÇÃO ----------------------------------#

def menu_colecao(cnx, cursor):
    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Coleção':>10}{'*':>41}")
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{1:>5}{' - Ver Coleção'}{'*':>32}")
    print(f"{'*'}{2:>5}{' - Adicionar skin'}{'*':>29}")
    print(f"{'*'}{3:>5}{' - Remover skin'}{'*':>31}")
    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    op = input("OPCAO > ").upper()

    match op:

        case '1':
            clear_screen()
            show_col(cursor)
            pause()

            clear_screen()
            menu_colecao(cnx, cursor)

        case '2':
            clear_screen()
            add_colecao(cnx, cursor)

            clear_screen()
            show_col(cursor)
            pause()

            clear_screen()
            menu_colecao(cnx, cursor)

        case '3':
            clear_screen()
            rem_colecao(cnx, cursor)

            clear_screen()
            show_col(cursor)
            pause()

            clear_screen()
            menu_colecao(cnx, cursor)

        case 'B':
            clear_screen()
            menu_inicial(cnx, cursor)

        case _:
            clear_screen()
            print("Opção Inválida")
            pause()

            clear_screen()
            menu_colecao(cnx, cursor)

#------------------------------- SHOW COLEÇÃO ----------------------------------#

def show_col(cursor):

    result = db.get_all_col(cursor)
    
    if len(result) == 0:
        print("A coleção está vazia. Adicione skins selecionando 2 no menu Coleção")
    else:
        print('*' * 52)
        print('*' + (' ' * 50) + '*')
        print(f"{'*'}{'Coleção':>10}{'*':>41}")
        print('*' + (' ' * 50) + '*')
        armas = []
        for r in result:
            arma = r[1]
            skin = r[2]

            if len(armas) == 0 or not (arma in armas):
                armas.append(arma)
                print(f"{'*':<6}{arma.upper()}" + (' ' * (45 - len(arma))) + '*')
                print(f"{'*':<8} - {skin}" + (' ' * (40 - len(skin))) + '*')
            else:
                print(f"{'*':<8} - {skin}" + (' ' * (40 - len(skin))) + '*')

        print('*' + (' ' * 50) + '*')
        print('*' * 52)

#--------------------------------- ADD COLEÇÃO ----------------------------------#

def add_colecao(cnx, cursor):

    skin = sel_skin()
    clear_screen()

    if skin == 'B':
        menu_colecao(cnx, cursor)

    arma = sel_arma(cursor, skin)
    clear_screen()

    if arma == 'B':
        menu_colecao(cnx, cursor)

    existe = existe_col(cursor, arma, skin)

    if existe:
        print("Skin já existe na coleção")
        pause()

        clear_screen()
        menu_colecao(cnx, cursor)

    else:
        w, id = existe_wish(cursor, arma, skin)
        if w:
            db.del_wish(cnx, cursor, id)
        db.adicionar_colecao(cnx, cursor, arma, skin)

#-------------------------------- EXISTE COLEÇÃO --------------------------------#

def existe_col(cursor, arma, skin):

    result = db.get_col(cursor, arma, skin)

    if len(result) == 1:
        return 1

    return 0

#--------------------------------- REM COLEÇÃO ----------------------------------#

def rem_colecao(cnx, cursor):

    #db.del_col(cnx, cursor, 3)
    result = db.get_all_col(cursor)
    
    if len(result) == 0:
        print("A coleção está vazia. Adicione skins selecionando 2 no menu Coleção")
        return
    
    #Ordenar a lista por ordem crescente de ids
    #result = sorted(result)
    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Selecione a skin:':>20}{'*':>31}")
    print('*' + (' ' * 50) + '*')

    armas = []
    ids = []
    for r in result:

        id   = r[0]
        arma = r[1]
        skin = r[2]

        ids.append(id)

        if len(armas) == 0 or not (arma in armas):
            armas.append(arma)
            print(f"{'*':<5}{arma.upper()}" + (' ' * (46 - len(arma))) + '*')
            print(f"{'*':<7} - {id}: {skin}" + (' ' * (39 - len(str(id)) - len(skin))) + '*')
        else:
            print(f"{'*':<7} - {id}: {skin}" + (' ' * (39 - len(str(id)) - len(skin))) + '*')

    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()

    op = input("OPCAO > ").upper()

    if op == 'B':
        clear_screen()
        menu_colecao(cnx, cursor)
    elif (op.isnumeric()):
        op = int(op)
        if op in ids:
            db.del_col(cnx, cursor, op)
        else:
            clear_screen()
            print("Opção Inválida")
            pause()

            clear_screen()
            menu_colecao(cnx, cursor)
    else:
        clear_screen()
        print("Opção Inválida")
        pause()

        clear_screen()
        menu_colecao(cnx, cursor)

#--------------------------------- MENU WISHLIST -----------------------------------#

def menu_wishlist(cnx, cursor):
    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Wishlist':>10}{'*':>41}")
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{1:>5}{' - Ver Wishlist'}{'*':>31}")
    print(f"{'*'}{2:>5}{' - Adicionar skin'}{'*':>29}")
    print(f"{'*'}{3:>5}{' - Remover skin'}{'*':>31}")
    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    op = input("OPCAO > ").upper()

    match op:

        case '1':
            clear_screen()
            show_wish(cursor)
            pause()

            clear_screen()
            menu_wishlist(cnx, cursor)

        case '2':
            clear_screen()
            add_wishlist(cnx, cursor)

            clear_screen()
            show_wish(cursor)
            pause()

            clear_screen()
            menu_wishlist(cnx, cursor)

        case '3':
            clear_screen()
            rem_wishlist(cnx, cursor)

            clear_screen()
            show_wish(cursor)
            pause()

            clear_screen()
            menu_wishlist(cnx, cursor)

        case 'B':
            clear_screen()
            menu_inicial(cnx, cursor)

        case _:
            clear_screen()
            print("Opção Inválida")
            pause()

            clear_screen()
            menu_wishlist(cnx, cursor)

#--------------------------------- SHOW WISHLIST -----------------------------------#

def show_wish(cursor):

    result = db.get_all_wish(cursor)

    if len(result) == 0:
        print("A wishlist está vazia. Adicione skins selecionando 2 no menu Wishlist")

    else:
        print('*' * 52)
        print('*' + (' ' * 50) + '*')
        print(f"{'*'}{'Wishlist':>10}{'*':>41}")
        print('*' + (' ' * 50) + '*')
        armas = []
        for r in result:
            arma = r[1]
            skin = r[2]

            if len(armas) == 0 or not (arma in armas):
                armas.append(arma)
                print(f"{'*':<6}{arma.upper()}" + (' ' * (45 - len(arma))) + '*')
                print(f"{'*':<8} - {skin}" + (' ' * (40 - len(skin))) + '*')
            else:
                print(f"{'*':<8} - {skin}" + (' ' * (40 - len(skin))) + '*')
        
        print('*' + (' ' * 50) + '*')
        print('*' * 52)

#----------------------------------- ADD WISHLIST -----------------------------------#

def add_wishlist(cnx, cursor):

    skin = sel_skin()
    clear_screen()

    if skin == 'B':
        menu_wishlist(cnx, cursor)

    arma = sel_arma(cursor, skin)
    clear_screen()


    if arma == 'B':
        menu_wishlist(cnx, cursor)
    else:
        existe, id = existe_wish(cursor, arma, skin)

        if existe:
            print("Skin já existe na wishlist")
            pause()

            clear_screen()
            menu_wishlist(cnx, cursor)

        else:
            db.adicionar_wishlist(cnx, cursor, arma, skin)

#--------------------------------- EXISTE WISHLIST ---------------------------------#

def existe_wish(cursor, arma, skin):

    result = db.get_wish(cursor, arma, skin)
    print(result)

    if len(result) == 1:
        return 1, result[0][0]

    return 0, 0

#----------------------------------- REM WISHLIST -----------------------------------#

def rem_wishlist(cnx, cursor):

    result = db.get_all_wish(cursor)
    
    if len(result) == 0:
        print("A coleção está vazia. Adicione skins selecionando 2 no menu Coleção")
        return

    #Ordenar a lista por ordem crescente de ids
    #result = sorted(result)

    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Selecione a skin:':>20}{'*':>31}")
    print('*' + (' ' * 50) + '*')

    armas = []
    ids = []
    for r in result:

        id   = r[0]
        arma = r[1]
        skin = r[2]

        ids.append(id)

        if len(armas) == 0 or not (arma in armas):
            armas.append(arma)
            print(f"{'*':<6}{arma.upper()}" + (' ' * (45 - len(arma))) + '*')
            print(f"{'*':<8} - {id}: {skin}" + (' ' * (37 - len(skin))) + '*')
        else:
            print(f"{'*':<8} - {id}: {skin}" + (' ' * (37 - len(skin))) + '*')

    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    
    op = input("OPCAO > ").upper()

    if op == 'B':
        clear_screen()
        menu_wishlist(cnx, cursor)
    elif (op.isnumeric()):
        op = int(op)
        if op in ids:
            db.del_wish(cnx, cursor, op)
        else:
            clear_screen()
            print("Opção Inválida")
            pause()

            clear_screen()
            menu_colecao(cnx, cursor)
    else:
        clear_screen()
        print("Opção Inválida")
        pause()

        clear_screen()
        menu_wishlist(cnx, cursor)
    
# ----------------------------------------------------------------------------- #

def sel_skin():

    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Selecione a skin':>19}{'*':>32}")
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{1:>5}{' - Smite'}{'*':>38}")
    print(f"{'*'}{2:>5}{' - Kohaku'}{'*':>37}")
    print(f"{'*'}{3:>5}{' - Gaia'}{'*':>39}")
    print(f"{'*'}{4:>5}{' - Spectrum'}{'*':>35}")
    print(f"{'*'}{5:>5}{' - Evori'}{'*':>38}")
    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    op = input("OPCAO > ").upper()

    skin = 0

    if op == 'B':
        return op

    elif op.isnumeric():
        op = int(op)
        if op >= 1 and op < 6:
            skin = op
        else:
            clear_screen()
            print("Opção Inválida")
            pause()

            return 'B'
    else:
        clear_screen()
        print("Opção Inválida")
        pause()
            
        return 'B'

    return skin


def sel_arma(cursor, skin):

    #Obtem a lista de armas disponiveis para a skin escolhida
    armas = db.get_arma_bundle(cursor, skin)

    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Selecione a arma':>19}{'*':>32}")
    print('*' + (' ' * 50) + '*')

    ids = []
    for arma in armas:
        ids.append(arma[0])
        print(f"{'*'}{arma[0]:>5} - {arma[1]}" + (' ' * (42 - len(arma[1]))) + '*') #Arma - Skin

    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    op = input("OPCAO > ").upper()

    arma = 0

    if op == 'B':
        return op

    elif op.isnumeric():
        op = int(op)
        if op in ids:
            arma = op
        else:
            clear_screen()
            print("Opção Inválida")
            pause()

            return 'B'
    else:
        clear_screen()
        print("Opção Inválida")
        pause()
            
        return 'B'

    return arma
    

# ----------------------------------------------------------------------------- #

def clear_screen():

    match os.name:
        case 'posix':
            subprocess.run(['clear'])

        case 'nt':
            subprocess.run(['cls'], shell = True)


def pause(mensagem = "Pressione ENTER para continuar..."):

    print()

    input(mensagem)


if __name__ == '__main__':
    main()