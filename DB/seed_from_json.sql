BEGIN;

INSERT INTO unite (libele) VALUES
    ('g'),
    ('càs'),
    ('pcs'),
    ('sans unité'),
    ('càc'),
    ('ml');

INSERT INTO mode_four (libele) VALUES
    ('chaleur tournante');

INSERT INTO ingredient (nom) VALUES
    ('fromage frais'),
    ('poudre amande'),
    ('coco râpée'),
    ('miel'),
    ('chocolat'),
    ('farine'),
    ('sucre'),
    ('beurre'),
    ('mascarpone'),
    ('biscuits'),
    ('tasse de café'),
    ('œuf'),
    ('cassonade'),
    ('cacao'),
    ('pépites choco'),
    ('sel'),
    ('bicarbonate de soude'),
    ('citron (+zeste)'),
    ('sucre glace'),
    ('levure chimique'),
    ('blanc d''œuf'),
    ('pincée de sel'),
    ('lait');

INSERT INTO recette (id, nom, etape, note) VALUES
    (
        1,
        'Bounty',
        E'1. Tout mélanger\n2. au congélateur 30 minutes\n3. fondre le choco\n4. trempez la pâte puis remettre au congélateur',
        NULL
    ),
    (
        2,
        '4 Quart',
        E'1. tout mélanger puis mettre au four',
        E'un œuf fait environ 60g\nCuisson: 35 min'
    ),
    (
        3,
        'Gâteau choco variante 1',
        E'1. mélanger les œufs, le sucre et la farine\n2. fondre le choco et le beurre (feu doux)\n3. mélanger le tout',
        E'Cuisson: 30 min'
    ),
    (
        9,
        'Gâteau choco variante 2',
        E'1. mélanger les œufs, le sucre, la poudre d''amande et la farine\n2. fondre le choco et le beurre (feu doux)\n3. mélanger le tout',
        E'Cuisson: 30 min'
    ),
    (
        4,
        'Tiramisu',
        E'1. Mélanger les jaunes avec le sucre, ajoutez le mascarpone quand le mélange est blanchâtre\n2. Monter les blancs en neige. Les incorporer progressivement au mélange\n3. Dans un plat, tapisser de biscuits trempés dans le café, mettre une couche de crème. Répéter jusqu''à ne plus avoir de crème\n4. Saupoudrer de cacao puis laisser reposer au frigo min. 2h',
        NULL
    ),
    (
        5,
        'Cookies',
        E'1. Ramollir le beurre (ne pas faire fondre)\n2. Fouettez le beurre mou, la cassonade et le sucre. Quand l''aspect est crémeux, ajouter les œufs\n3. Ajoutez la farine, le cacao, le sel. Mélanger puis ajoutez les pépites\n4. Faire des boules de pâte sur du papier sulfurisé (plus ou moins 25g)\n5. 8'' (fondant) - 12'' (croustillant) au four. Laissez refroidir',
        E'8 minutes -> fondant\n12 minutes -> croustillant\nCuisson: 8 min'
    ),
    (
        6,
        'Cake citron',
        E'1. Faites fondre le beurre. Versez le sucre dans un bol avec le beurre et le zeste des citrons.\n2. Mélangez sommairement le beurre fondu avec le sucre.\n3. Ajoutez les œufs.\n4. Ajoutez la farine et la levure chimique et le jus de citron.\n5. Versez la pâte dans un petit moule à cake, légèrement beurré.\n6. Pendant la cuisson, préparez le glaçage en mélangeant le sucre glace avec le jus de citron\n7. Après cuisson, emballez-le immédiatement de film étirable pour qu''il conserve toute son humidité.\n8. Laissez le cake refroidir totalement dans son emballage. Quand il est à température ambiante, versez le glaçage sur le gâteau. Mettez une assiette en dessous pour récupérer l''excédent.\n9. Lissez le nappage pour qu''il tombe de tous les côtés et qu''il soit fin.\n10. Remettez le cake au four (100°C 8 minutes) pour sécher le glaçage. Au toucher: le glaçage est bien sec et très doux.',
        E'Cuisson: 45 min'
    ),
    (
        7,
        'Meringue',
        E'1. Battre les blancs et ajouter petit à petit le sucre',
        E'1/2h - 1h au four (blanche moelleuse - rose fondante)\nCuisson: 30 min'
    ),
    (
        8,
        'Crêpes',
        E'1. Fondre le beurre\n2. tout mélanger',
        E'pour un peu plus de goût, faire fondre le beurre à la poêle pour un beurre noisette'
    );

INSERT INTO recette_ingredient (id_recette, id_ingredient, id_unite, qte, optionnel) VALUES
    (1, (SELECT id FROM ingredient WHERE nom = 'fromage frais'), (SELECT id FROM unite WHERE libele = 'g'), 11.67, FALSE),
    (1, (SELECT id FROM ingredient WHERE nom = 'poudre amande'), (SELECT id FROM unite WHERE libele = 'g'), 3.33, TRUE),
    (1, (SELECT id FROM ingredient WHERE nom = 'coco râpée'), (SELECT id FROM unite WHERE libele = 'g'), 16.67, FALSE),
    (1, (SELECT id FROM ingredient WHERE nom = 'miel'), (SELECT id FROM unite WHERE libele = 'càs'), 0.50, FALSE),
    (1, (SELECT id FROM ingredient WHERE nom = 'chocolat'), (SELECT id FROM unite WHERE libele = 'g'), 30.00, FALSE),

    (2, (SELECT id FROM ingredient WHERE nom = 'farine'), (SELECT id FROM unite WHERE libele = 'g'), 31.20, FALSE),
    (2, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 31.20, FALSE),
    (2, (SELECT id FROM ingredient WHERE nom = 'beurre'), (SELECT id FROM unite WHERE libele = 'g'), 31.20, FALSE),
    (2, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.50, FALSE),

    (3, (SELECT id FROM ingredient WHERE nom = 'chocolat'), (SELECT id FROM unite WHERE libele = 'g'), 33.40, FALSE),
    (3, (SELECT id FROM ingredient WHERE nom = 'beurre'), (SELECT id FROM unite WHERE libele = 'g'), 16.60, FALSE),
    (3, (SELECT id FROM ingredient WHERE nom = 'farine'), (SELECT id FROM unite WHERE libele = 'g'), 8.40, FALSE),
    (3, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 16.60, FALSE),
    (3, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.60, FALSE),

    (9, (SELECT id FROM ingredient WHERE nom = 'chocolat'), (SELECT id FROM unite WHERE libele = 'g'), 33.40, FALSE),
    (9, (SELECT id FROM ingredient WHERE nom = 'beurre'), (SELECT id FROM unite WHERE libele = 'g'), 16.60, FALSE),
    (9, (SELECT id FROM ingredient WHERE nom = 'farine'), (SELECT id FROM unite WHERE libele = 'g'), 8.40, FALSE),
    (9, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 16.60, FALSE),
    (9, (SELECT id FROM ingredient WHERE nom = 'poudre amande'), (SELECT id FROM unite WHERE libele = 'g'), 16.60, FALSE),
    (9, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.60, FALSE),

    (4, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.75, FALSE),
    (4, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 18.80, FALSE),
    (4, (SELECT id FROM ingredient WHERE nom = 'mascarpone'), (SELECT id FROM unite WHERE libele = 'g'), 62.60, FALSE),
    (4, (SELECT id FROM ingredient WHERE nom = 'biscuits'), (SELECT id FROM unite WHERE libele = 'pcs'), 6.00, FALSE),
    (4, (SELECT id FROM ingredient WHERE nom = 'tasse de café'), (SELECT id FROM unite WHERE libele = 'sans unité'), 0.00, FALSE),
    (4, (SELECT id FROM ingredient WHERE nom = 'cacao'), (SELECT id FROM unite WHERE libele = 'sans unité'), 0.00, FALSE),

    (5, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.20, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 1.60, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'beurre'), (SELECT id FROM unite WHERE libele = 'g'), 4.00, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'cassonade'), (SELECT id FROM unite WHERE libele = 'g'), 2.60, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'farine'), (SELECT id FROM unite WHERE libele = 'g'), 4.40, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'cacao'), (SELECT id FROM unite WHERE libele = 'g'), 0.60, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'pépites choco'), (SELECT id FROM unite WHERE libele = 'g'), 3.40, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'sel'), (SELECT id FROM unite WHERE libele = 'càc'), 0.008, FALSE),
    (5, (SELECT id FROM ingredient WHERE nom = 'bicarbonate de soude'), (SELECT id FROM unite WHERE libele = 'càc'), 0.016, TRUE),

    (6, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 40.00, FALSE),
    (6, (SELECT id FROM ingredient WHERE nom = 'beurre'), (SELECT id FROM unite WHERE libele = 'g'), 24.00, FALSE),
    (6, (SELECT id FROM ingredient WHERE nom = 'citron (+zeste)'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.40, FALSE),
    (6, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.60, FALSE),
    (6, (SELECT id FROM ingredient WHERE nom = 'farine'), (SELECT id FROM unite WHERE libele = 'g'), 30.00, FALSE),
    (6, (SELECT id FROM ingredient WHERE nom = 'sucre glace'), (SELECT id FROM unite WHERE libele = 'g'), 26.00, FALSE),
    (6, (SELECT id FROM ingredient WHERE nom = 'levure chimique'), (SELECT id FROM unite WHERE libele = 'càc'), 0.10, TRUE),

    (7, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'g'), 12.60, FALSE),
    (7, (SELECT id FROM ingredient WHERE nom = 'blanc d''œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.20, FALSE),
    (7, (SELECT id FROM ingredient WHERE nom = 'pincée de sel'), (SELECT id FROM unite WHERE libele = 'sans unité'), 0.00, FALSE),

    (8, (SELECT id FROM ingredient WHERE nom = 'farine'), (SELECT id FROM unite WHERE libele = 'g'), 50.00, FALSE),
    (8, (SELECT id FROM ingredient WHERE nom = 'lait'), (SELECT id FROM unite WHERE libele = 'ml'), 100.00, FALSE),
    (8, (SELECT id FROM ingredient WHERE nom = 'œuf'), (SELECT id FROM unite WHERE libele = 'pcs'), 0.80, FALSE),
    (8, (SELECT id FROM ingredient WHERE nom = 'sucre'), (SELECT id FROM unite WHERE libele = 'càs'), 0.40, FALSE),
    (8, (SELECT id FROM ingredient WHERE nom = 'sel'), (SELECT id FROM unite WHERE libele = 'sans unité'), 0.00, FALSE),
    (8, (SELECT id FROM ingredient WHERE nom = 'beurre'), (SELECT id FROM unite WHERE libele = 'g'), 25.00, FALSE);

INSERT INTO recette_four (id_recette, id_four, chaleur, duree) VALUES
    (2, (SELECT id FROM mode_four WHERE libele = 'chaleur tournante'), 180, 35),
    (3, (SELECT id FROM mode_four WHERE libele = 'chaleur tournante'), 180, 30),
    (9, (SELECT id FROM mode_four WHERE libele = 'chaleur tournante'), 180, 30),
    (5, (SELECT id FROM mode_four WHERE libele = 'chaleur tournante'), 180, 8),
    (6, (SELECT id FROM mode_four WHERE libele = 'chaleur tournante'), 170, 45),
    (7, (SELECT id FROM mode_four WHERE libele = 'chaleur tournante'), 120, 30);

-- Keep SERIAL sequences aligned with inserted IDs.
SELECT setval(pg_get_serial_sequence('ingredient', 'id'), COALESCE((SELECT MAX(id) FROM ingredient), 1), true);
SELECT setval(pg_get_serial_sequence('unite', 'id'), COALESCE((SELECT MAX(id) FROM unite), 1), true);
SELECT setval(pg_get_serial_sequence('mode_four', 'id'), COALESCE((SELECT MAX(id) FROM mode_four), 1), true);
SELECT setval(pg_get_serial_sequence('recette', 'id'), COALESCE((SELECT MAX(id) FROM recette), 1), true);
SELECT setval(pg_get_serial_sequence('admin', 'id'), COALESCE((SELECT MAX(id) FROM admin), 1), true);

COMMIT;