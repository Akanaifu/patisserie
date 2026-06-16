import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-recette-details',
  imports: [],
  templateUrl: './recette-details.html',
  styleUrl: './recette-details.css',
})
export class RecetteDetails implements OnInit {
  public recetteId: number | null = 0;
  constructor(private route: ActivatedRoute) {}
  ngOnInit() {
    let idRecette = Number(this.route.snapshot.paramMap.get('id'));
    console.log('🚀 ~ RecetteDetails ~ ngOnInit ~ idRecette:', idRecette);
    this.recetteId = idRecette;
  }
}
