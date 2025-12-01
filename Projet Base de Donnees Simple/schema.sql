-- Ce script SQL définit le schéma de la base de données pour une bibliothèque de différents auteurs
-- Il crée deux tables : auteurs et livres avec une relation entre les deux

-- Création de la table auteurs
-- Cette table stocke les informations sur les auteurs des livres
CREATE TABLE auteurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- C'est le nom unique pour identifier chaque auteur
    nom TEXT NOT NULL, -- Nom complet de l'auteur
    annee_naissance INTEGER -- Année de naissance de l'auteur
);

-- Création de la table livres
-- Cette table stocke les informations sur les livres de la bibliothèque que j'ai créer
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- C'est le nom unique pour identifier chaque livre
    titre TEXT NOT NULL, -- Titre du livre
    auteur_id INTEGER, -- Référence au nom de l'auteur
    annee_publication INTEGER, -- Année de publication du livre
    FOREIGN KEY (auteur_id) REFERENCES auteurs(id) -- Sa met en relation livres et auteurs
);