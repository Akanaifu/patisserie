import { Component, signal } from '@angular/core';
import { Navbar } from './navbar/navbar';
import { RecettesDisplay } from './recettes-display/recettes-display';
import { RouterModule, RouterLink } from '@angular/router';
@Component({
  selector: 'app-root',
  imports: [Navbar, RecettesDisplay, RouterModule, RouterLink],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected readonly title = signal('frontend');
}
