from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/colecao')
def colecao():
    result = db.get_all_col()

    skins = []

    col = {}

    for r in result:
        id  = r[0]
        a   = r[1].decode()
        s   = r[2].decode()

        if not(a in col):
            skins = []
            skins.append((id, s))
            col[a] = skins
        else:
            skins.append((id, s))
            col[a] = skins

    #print(col)

    return render_template("colecao.html", colecao = col)


@app.route('/wishlist')
def wishlist():
    result = db.get_all_wish()

    skins = []

    wish = {}

    for r in result:
        id  = r[0]
        a   = r[1].decode()
        s   = r[2].decode()

        if not(a in wish):
            skins = []
            skins.append((id, s))
            wish[a] = skins
        else:
            skins.append((id, s))
            wish[a] = skins

    return render_template("wishlist.html", wishlist = wish)


@app.route('/add_col')
def add_col():

    result = db.get_bundle()

    armas = []

    bund = {}

    for r in result:

        skinID  = r[0]
        s       = r[1].decode()
        armaID  = r[2]
        a       = r[3].decode()

        if not((skinID, s) in bund):
            armas = []
            armas.append((armaID, a))
            bund[(skinID, s)] = armas
        else:
            armas.append((armaID, a))
            bund[(skinID, s)] = armas

    #print(bund)

    return render_template("add_colecao.html", bundles = bund)
