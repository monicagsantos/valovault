import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ValoVault"
)

cursor = cnx.cursor(prepared=True)


def adicionar_colecao(arma: int, skin: int):

    query = "INSERT INTO Colecao (ArmaID, SkinID) VALUES (%s, %s)"
    data = (arma, skin)
    cursor.execute(query, data)
    cnx.commit()


def adicionar_wishlist(arma: int, skin: int):

    query = "INSERT INTO Wishlist (ArmaID, SkinID) VALUES (%s, %s)"
    data = (arma, skin)
    cursor.execute(query, data)
    cnx.commit()


def get_col(arma, skin):

    query = f"SELECT ID FROM Colecao WHERE ArmaID = {arma} AND SkinID = {skin}"
    cursor.execute(query)
    result = cursor.fetchall()

    return result


def get_wish(arma, skin):

    query = f"SELECT ID FROM Wishlist WHERE ArmaID = {arma} AND SkinID = {skin}"
    cursor.execute(query)
    result = cursor.fetchall()

    return result


def get_all_col():
    query = "SELECT c.ID, a.Nome, s.Nome FROM Colecao c, Arma a, Skin s WHERE c.ArmaID = a.ID AND c.SkinID = s.ID ORDER BY c.ArmaID"
    cursor.execute(query)
    
    result = cursor.fetchall()

    return result


def get_all_wish():
    query = "SELECT w.ID, a.Nome, s.Nome FROM Wishlist w, Arma a, Skin s WHERE w.ArmaID = a.ID AND w.SkinID = s.ID  ORDER BY w.ArmaID"
    cursor.execute(query)
    
    result = cursor.fetchall()

    return result


def get_bundle():

    query = "SELECT b.SkinID, s.Nome, b.ArmaID, a.Nome FROM Bundle b, Skin s, Arma a WHERE b.ArmaID = a.ID AND b.SkinID = s.ID ORDER BY b.SkinID"
    cursor.execute(query)
    
    result = cursor.fetchall()

    return result


def get_arma_bundle(skin):

    query = f"SELECT a.ID, a.Nome FROM Bundle b, Skin s, Arma a WHERE b.SkinID = {skin} AND b.SkinID = s.ID AND b.ArmaID = a.ID"
    cursor.execute(query)
    
    result = cursor.fetchall()

    return result


def del_col(id):

    query = f"DELETE FROM Colecao WHERE ID = {id}"
    cursor.execute(query)
    cnx.commit()

    #print(cursor.rowcount, "record(s) deleted")


def del_wish(id):

    query = f"DELETE FROM Wishlist WHERE ID = {id}"
    cursor.execute(query)
    cnx.commit()

    #print(cursor.rowcount, "record(s) deleted")


def fechar():
    # Close the cursor and connection
    cursor.close()
    cnx.close()