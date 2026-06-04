CREATE TABLE ingredient (
    id   SERIAL PRIMARY KEY,
    nom  VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE unite (
    id      SERIAL PRIMARY KEY,
    libele  VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE mode_four (
    id      SERIAL PRIMARY KEY,
    libele  VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE recette (
    id      SERIAL PRIMARY KEY,
    nom     VARCHAR(150) NOT NULL,
    etape   TEXT NOT NULL,
    note    TEXT
);

CREATE TABLE recette_ingredient (
    id_recette    INT NOT NULL REFERENCES recette(id) ON DELETE CASCADE,
    id_ingredient INT NOT NULL REFERENCES ingredient(id) ON DELETE RESTRICT,
    id_unite      INT NOT NULL REFERENCES unite(id) ON DELETE RESTRICT,
    qte           DECIMAL(10,2) NOT NULL,
    optionnel     BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (id_recette, id_ingredient)
);

CREATE TABLE recette_four (
    id_recette  INT NOT NULL REFERENCES recette(id) ON DELETE CASCADE,
    id_four     INT NOT NULL REFERENCES mode_four(id) ON DELETE RESTRICT,
    chaleur     INT NOT NULL, -- en °C
    duree       INT NOT NULL, -- en minutes
    PRIMARY KEY (id_recette, id_four)
);

CREATE TABLE admin (
    id   SERIAL PRIMARY KEY,
    mdp  VARCHAR(255) NOT NULL -- bcrypt ou argon2
);