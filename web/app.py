from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/colecao')
def colecao():

    col = db.get_all_col()

    #print(col)

    return render_template("colecao.html", colecao=col)


@app.route('/wishlist')
def wishlist():
    wish = db.get_all_wish()

    return render_template("wishlist.html", wishlist=wish)


@app.route('/add_col')
def add_col():

    bund = db.get_bundle()

    #print(bund)

    return render_template("sel_skin_col.html", bundles=bund)


@app.route('/sel_skin_col', methods=['POST'])
def sel_skin_col():

    skinID = int(request.form['skin'])

    bund = db.get_bundle()

    #print(skinID)

    return render_template("sel_arma_col.html", bundles=bund, skinID=skinID)


@app.route('/sel_arma_col/<skinID>', methods=['POST'])
def sel_arma_col(skinID):

    armaID = request.form['arma']

    result = db.get_col(armaID, skinID)

    if len(result) == 1:
        return redirect(url_for("existe_col"))
    else:
        db.adicionar_colecao(armaID, skinID)

    return redirect(url_for("colecao"))


@app.route('/existe_col')
def existe_col():

    return render_template("existe_col.html")


@app.route('/add_wish')
def add_wish():

    bund = db.get_bundle()

    #print(bund)

    return render_template("sel_skin_wish.html", bundles=bund)


@app.route('/sel_skin_wish', methods=['POST'])
def sel_skin_wish():

    skinID = int(request.form['skin'])

    bund = db.get_bundle()

    #print(skinID)

    return render_template("sel_arma_wish.html", bundles=bund, skinID=skinID)


@app.route('/sel_arma_wish/<skinID>', methods=['POST'])
def sel_arma_wish(skinID):

    armaID = request.form['arma']

    result = db.get_wish(armaID, skinID)

    if len(result) == 1:
        return redirect(url_for("existe_wish"))
    else:
        db.adicionar_wishlist(armaID, skinID)

    return redirect(url_for("wishlist"))


@app.route('/existe_wish')
def existe_wish():

    return render_template("existe_wish.html")


@app.route('/rem_col/<id>')
def rem_col(id):

    db.del_col(id)

    return redirect(url_for("colecao"))


@app.route('/rem_wish/<id>')
def rem_wish(id):

    db.del_wish(id)

    return redirect(url_for("wishlist"))


@app.route('/skin/<nome>')
def pag_skin(nome: str):

    info = db.get_info_skin(nome)
    

    return render_template("skin.html", info=info)


