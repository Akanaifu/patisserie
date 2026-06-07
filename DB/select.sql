select r.nom, i.nom, ri.qte
from recette r
join recette_ingredient ri on r.id = ri.id_recette
join ingredient i on ri.id_ingredient = i.id;


select i.id ingredient_id, i.nom, u.libele unite
from ingredient i
join recette_ingredient ri on i.id = ri.id_ingredient
join unite u on ri.id_unite = u.id
ORDER BY i.nom;