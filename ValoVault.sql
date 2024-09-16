DROP DATABASE IF EXISTS ValoVault;

CREATE DATABASE IF NOT EXISTS ValoVault;

USE ValoVault;

-- CRIAÇÃO DE TABELAS --

CREATE TABLE Arma(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(10) NOT NULL
);

CREATE TABLE Skin(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(20) NOT NULL,
    Preco INT NOT NULL,
    Nivel ENUM("Select", "Deluxe", "Premium", "Exclusive", "Ultra") NOT NULL
);

CREATE TABLE Colecao(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    ArmaID INT NOT NULL,
    SkinID INT NOT NULL,
    
    FOREIGN KEY (ArmaID) REFERENCES Arma(ID),
    FOREIGN KEY (SkinID) REFERENCES Skin(ID)
);

CREATE TABLE Wishlist(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    ArmaID INT NOT NULL,
    SkinID INT NOT NULL,
    
    FOREIGN KEY (ArmaID) REFERENCES Arma(ID),
    FOREIGN KEY (SkinID) REFERENCES Skin(ID)
);

CREATE TABLE Bundle(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    SkinID INT NOT NULL,
    ArmaID INT NOT NULL,
    
    FOREIGN KEY (SkinID) REFERENCES Skin(ID),
    FOREIGN KEY (ArmaID) REFERENCES Arma(ID)
);

-- INSERÇÃO DE DADOS --

INSERT INTO Arma(Nome) VALUES ('Classic'), ('Ghost'), ('Sheriff'), ('Vandal'), ('Phantom'), ('Faca');
SELECT * FROM Arma;

INSERT INTO Skin(Nome, Preco, Nivel) VALUES ('Smite', 875, 'Select');
INSERT INTO Skin(Nome, Preco, Nivel) VALUES ('Kohaku', 1275, 'Deluxe');
INSERT INTO Skin(Nome, Preco, Nivel) VALUES ('Gaia', 1775, 'Premium');
INSERT INTO Skin(Nome, Preco, Nivel) VALUES ('Spectrum', 2675, 'Exclusive');
INSERT INTO Skin(Nome, Preco, Nivel) VALUES ('Evori', 2475, 'Ultra');
SELECT * FROM Skin;

-- SMITE --
INSERT INTO Bundle(SkinID, ArmaID) VALUES (1, 1);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (1, 5);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (1, 6);
-- KOHAKU --
INSERT INTO Bundle(SkinID, ArmaID) VALUES (2, 1);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (2, 5);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (2, 6);
-- GAIA --
INSERT INTO Bundle(SkinID, ArmaID) VALUES (3, 2);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (3, 4);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (3, 5);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (3, 6);
-- SPECTRUM --
INSERT INTO Bundle(SkinID, ArmaID) VALUES (4, 1);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (4, 5);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (4, 6);
-- EVORI --
INSERT INTO Bundle(SkinID, ArmaID) VALUES (5, 2);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (5, 4);
INSERT INTO Bundle(SkinID, ArmaID) VALUES (5, 6);
SELECT * FROM Bundle;