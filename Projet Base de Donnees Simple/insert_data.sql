-- Ce script insère des données d'exemple dans la base de données.
-- Il ajoute des auteurs et des livres pour illustrer l'utilisation de la base.

-- Insertion des auteurs
-- Ces commandes ajoutent des auteurs célèbres à la table des auteurs
INSERT INTO auteurs (nom, annee_naissance) VALUES ('Victor Hugo', 1802); -- Auteur français
INSERT INTO auteurs (nom, annee_naissance) VALUES ('J.K. Rowling', 1965); -- Auteure britannique
INSERT INTO auteurs (nom, annee_naissance) VALUES ('George Orwell', 1903); -- Auteur britannique

-- Insertion des différent livres choisit
-- Ces commandes ajoutent des livres qui appartiennent aux auteurs que j'ai choisis juste au dessus
INSERT INTO livres (titre, auteur_id, annee_publication) VALUES ('Les Misérables', 1, 1862); -- Roman de Victor Hugo
INSERT INTO livres (titre, auteur_id, annee_publication) VALUES ('Harry Potter à l''école des sorciers', 2, 1997); -- Premier tome de la série Harry Potter
INSERT INTO livres (titre, auteur_id, annee_publication) VALUES ('1984', 3, 1949); -- Roman de George Orwell
INSERT INTO livres (titre, auteur_id, annee_publication) VALUES ('Notre-Dame de Paris', 1, 1831); -- Autre roman de Victor Hugo