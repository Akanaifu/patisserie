import { RouterModule, Routes } from '@angular/router';
import { RecetteDetails } from './recette-details/recette-details';
import { RecettesDisplay } from './recettes-display/recettes-display';
import { NgModule } from '@angular/core';

export const routes: Routes = [
  {
    path: 'RecetteDetails/:id',
    component: RecetteDetails,
  },
  {
    path: 'RecettesDisplay',
    component: RecettesDisplay,
  },
];

export class AppRoutinModule {}
export const routinModule = [RecetteDetails, RecettesDisplay];
