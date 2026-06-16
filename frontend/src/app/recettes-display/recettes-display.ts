import { Component, signal } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { Router, RouterModule, RouterLink } from '@angular/router';
@Component({
  selector: 'app-recettes-display',
  imports: [MatButtonModule, MatCardModule, RouterModule, RouterLink],
  templateUrl: './recettes-display.html',
  styleUrl: './recettes-display.css',
})
export class RecettesDisplay {
  constructor(private router: Router) {}
  recettes = [
    {
      id: 1,
      nom: 'Bounty',
      etape:
        '1. Tout mélanger\n2. au congélateur 30 minutes\n3. fondre le choco\n4. trempez la pâte puis remettre au congélateur',
      note: null,
      img: '/bounty.jpg',
    },
    {
      id: 2,
      nom: '4 Quart',
      etape: '1. tout mélanger puis mettre au four',
      note: 'un œuf fait environ 60g\nCuisson: 35 min',
      img: '/quatre-quarts.jpg',
    },
    {
      id: 3,
      nom: 'Gâteau choco variante 1',
      etape:
        '1. mélanger les œufs, le sucre et la farine\n2. fondre le choco et le beurre (feu doux)\n3. mélanger le tout',
      note: 'Cuisson: 30 min',
      img: '/gateau_au_chocolat1.jpg',
    },
    {
      id: 9,
      nom: 'Gâteau choco variante 2',
      etape:
        "1. mélanger les œufs, le sucre, la poudre d'amande et la farine\n2. fondre le choco et le beurre (feu doux)\n3. mélanger le tout",
      note: 'Cuisson: 30 min',
      img: '/gateau-au-chocolat2.jpg',
    },
    {
      id: 4,
      nom: 'Tiramisu',
      etape:
        "1. Mélanger les jaunes avec le sucre, ajoutez le mascarpone quand le mélange est blanchâtre\n2. Monter les blancs en neige. Les incorporer progressivement au mélange\n3. Dans un plat, tapisser de biscuits trempés dans le café, mettre une couche de crème. Répéter jusqu'à ne plus avoir de crème\n4. Saupoudrer de cacao puis laisser reposer au frigo min. 2h",
      note: null,
      img: '/tiramisu.jpg',
    },
    {
      id: 5,
      nom: 'Cookies',
      etape:
        "1. Ramollir le beurre (ne pas faire fondre)\n2. Fouettez le beurre mou, la cassonade et le sucre. Quand l'aspect est crémeux, ajouter les œufs\n3. Ajoutez la farine, le cacao, le sel. Mélanger puis ajoutez les pépites\n4. Faire des boules de pâte sur du papier sulfurisé (plus ou moins 25g)\n5. 8' (fondant) - 12' (croustillant) au four. Laissez refroidir",
      note: '8 minutes -> fondant\n12 minutes -> croustillant\nCuisson: 8 min',
      img: '/cookies.jpg',
    },
    {
      id: 6,
      nom: 'Cake citron',
      etape:
        "1. Faites fondre le beurre. Versez le sucre dans un bol avec le beurre et le zeste des citrons.\n2. Mélangez sommairement le beurre fondu avec le sucre.\n3. Ajoutez les œufs.\n4. Ajoutez la farine et la levure chimique et le jus de citron.\n5. Versez la pâte dans un petit moule à cake, légèrement beurré.\n6. Pendant la cuisson, préparez le glaçage en mélangeant le sucre glace avec le jus de citron\n7. Après cuisson, emballez-le immédiatement de film étirable pour qu'il conserve toute son humidité.\n8. Laissez le cake refroidir totalement dans son emballage. Quand il est à température ambiante, versez le glaçage sur le gâteau. Mettez une assiette en dessous pour récupérer l'excédent.\n9. Lissez le nappage pour qu'il tombe de tous les côtés et qu'il soit fin.\n10. Remettez le cake au four (100°C 8 minutes) pour sécher le glaçage. Au toucher: le glaçage est bien sec et très doux.",
      note: 'Cuisson: 45 min',
      img: '/Cake_citron.jpg',
    },
    {
      id: 7,
      nom: 'Meringue',
      etape: '1. Battre les blancs et ajouter petit à petit le sucre',
      note: '1/2h - 1h au four (blanche moelleuse - rose fondante)\nCuisson: 30 min',
      img: '/meringue.jpg',
    },
    {
      id: 8,
      nom: 'Crêpes',
      etape: '1. Fondre le beurre\n2. tout mélanger',
      note: 'pour un peu plus de goût, faire fondre le beurre à la poêle pour un beurre noisette',
      img: '/Crepes.jpg',
    },
  ];

  onSelect(recetteId: number) {
    this.router.navigate(['/RecetteDetails', recetteId]);
  }
}
