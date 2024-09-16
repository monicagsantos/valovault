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

'''
class Arma:

    def __init__(self, nome):
        self.nome = nome

        self.skins = []

    def add_skin(self, skin: str):

        #Se a arma não tiver skins associadas, adiciona-a
        if len(self.skins) == 0:
            self.skins.append(skin)
            return 1

        #Verifica se a skin já existir na lista
        for s in self.skins:
            if s == skin:
                return 0
        
        #Se a skin não existe na lista, adiciona-a
        self.skins.append(skin)
        return 1
'''



def main():

    cnx, cursor = db.iniciar()

    clear_screen()
    menu_inicial(cnx, cursor)


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

#------------------------------- COLEÇÃO ----------------------------------#

def show_col(cursor):

    result = db.get_all_col(cursor)
    
    if len(result) == 0:
        print("A coleção está vazia. Adicione skins selecionando 2 no menu Coleção")
    else:
        armas = []
        for r in result:
            arma = r[1].decode()
            skin = r[2].decode()

            if len(armas) == 0 or not (arma in armas):
                armas.append(arma)
                print(f"{arma}:")
                print(f"     - {skin}")
            else:
                print(f"     - {skin}")


def add_colecao(cnx, cursor):

    skin = sel_skin()
    clear_screen()

    if skin == 'B':
        menu_colecao(cnx, cursor)

    arma = sel_arma(cursor, skin)
    clear_screen()

    if arma == 'B':
        menu_colecao(cnx, cursor)

    db.adicionar_colecao(cnx, cursor, arma, skin)


def rem_colecao(cnx, cursor):

    #db.del_col(cnx, cursor, 3)
    result = db.get_all_col(cursor)
    
    if len(result) == 0:
        print("A coleção está vazia. Adicione skins selecionando 2 no menu Coleção")
        return
    
    print("Selecione a skin: ")
    
    for r in result:
        id   = r[0]
        arma = r[1].decode()
        skin = r[2].decode()

        print(f"{id}: {arma} - {skin}")
    
    op = input("OPCAO > ").upper()

    db.del_col(cnx, cursor, op)

#--------------------------------- WISHLIST -----------------------------------#

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


def show_wish(cursor):

    result = db.get_all_wish(cursor)

    if len(result) == 0:
        print("A wishlist está vazia. Adicione skins selecionando 2 no menu Wishlist")

    else:
        armas = []
        for x in result:
            arma = x[1].decode()
            skin = x[2].decode()

            if len(armas) == 0 or not (arma in armas):
                armas.append(arma)
                print(f"{arma}:")
                print(f"     - {skin}")
            else:
                print(f"     - {skin}")



def add_wishlist(cnx, cursor):

    skin = sel_skin()
    clear_screen()

    if skin == 'B':
        menu_wishlist(cnx, cursor)

    arma = sel_arma(cursor, skin)
    clear_screen()

    if arma == 'B':
        menu_wishlist(cnx, cursor)

    db.adicionar_wishlist(cnx, cursor, arma, skin)


def rem_wishlist(cnx, cursor):

    result = db.get_all_wish(cursor)
    
    if len(result) == 0:
        print("A coleção está vazia. Adicione skins selecionando 2 no menu Coleção")
        return
    
    print("Selecione a skin: ")

    ids = []

    for r in result:
        id = r[0]
        
        if len(ids) == 0:
            ids.append(id)
            continue

        if len(ids) == 1:
            if(ids[0] < id):
                ids.append(id)
            else:
                maior = ids[0]
                ids[0] = id
                ids.append(maior)
        
        for i in range(len(ids) - 1):
            if(ids[])

        print(ids)
    
    '''
    for r in result:
        id   = r[0]
        arma = r[1].decode()
        skin = r[2].decode()

        print(f"{id}: {arma} - {skin}")
    
    op = input("OPCAO > ").upper()

    db.del_wish(cnx, cursor, op)
    '''

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

    else:
        skin = int(op)

    return skin


def sel_arma(cursor, skin):

    #Obtem a lista de armas disponiveis para a skin escolhida
    armas = db.get_arma_bundle(cursor, skin)

    print('*' * 52)
    print('*' + (' ' * 50) + '*')
    print(f"{'*'}{'Selecione a arma':>19}{'*':>32}")
    print('*' + (' ' * 50) + '*')

    for arma in armas:
        print(f"{'*'}{arma[0]:>5} - {arma[1].decode()}{' ':>50} *") #Arma - Skin

    print(f"{'*'}{'B':>5}{' - Voltar'}{'*':>37}")
    print('*' + (' ' * 50) + '*')
    print('*' * 52)
    print()
    op = input("OPCAO > ").upper()

    arma = 0

    if op == 'B':
        return op

    else:
        arma = int(op)

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