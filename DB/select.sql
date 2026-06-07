select r.nom, i.nom, ri.qte
from recette r
join recette_ingredient ri on r.id = ri.id_recette
join ingredient i on ri.id_ingredient = i.id;


select i.id ingredient_id, i.nom, u.libele unite
from ingredient i
join recette_ingredient ri on i.id = ri.id_ingredient
join unite u on ri.id_unite = u.id
ORDER BY i.nom;

SELECT
    r.id,
    r.nom,
    r.etape,
    r.note,
    COALESCE(
        json_agg(
            DISTINCT jsonb_build_object(
                'ingredient', i.nom,
                'quantite', ri.qte,
                'unite', u.libele,
                'optionnel', ri.optionnel
            )
        ) FILTER (WHERE i.id IS NOT NULL),
        '[]'
    ) AS ingredients,
    COALESCE(
        json_agg(
            DISTINCT jsonb_build_object(
                'mode_four', mf.libele,
                'chaleur', rf.chaleur,
                'duree', rf.duree
            )
        ) FILTER (WHERE mf.id IS NOT NULL),
        '[]'
    ) AS fours
FROM recette r
LEFT JOIN recette_ingredient ri ON ri.id_recette = r.id
LEFT JOIN ingredient i ON i.id = ri.id_ingredient
LEFT JOIN unite u ON u.id = ri.id_unite
LEFT JOIN recette_four rf ON rf.id_recette = r.id
LEFT JOIN mode_four mf ON mf.id = rf.id_four
WHERE r.id = 2
GROUP BY r.id, r.nom, r.etape, r.note;