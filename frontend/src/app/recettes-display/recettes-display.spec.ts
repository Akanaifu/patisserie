import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecettesDisplay } from './recettes-display';

describe('RecettesDisplay', () => {
  let component: RecettesDisplay;
  let fixture: ComponentFixture<RecettesDisplay>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RecettesDisplay],
    }).compileComponents();

    fixture = TestBed.createComponent(RecettesDisplay);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
