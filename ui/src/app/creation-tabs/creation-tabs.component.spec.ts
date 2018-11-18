import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreationTabsComponent } from './creation-tabs.component';

describe('CreationTabsComponent', () => {
  let component: CreationTabsComponent;
  let fixture: ComponentFixture<CreationTabsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreationTabsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreationTabsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
