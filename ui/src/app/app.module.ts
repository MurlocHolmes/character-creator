import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import {
  MatButtonModule,
  MatCardModule, MatDividerModule, MatFormFieldModule, MatInputModule, MatSelectModule, MatTableModule, MatTabsModule,
  MatToolbarModule
} from '@angular/material';
import { CreationTabsComponent } from './creation-tabs/creation-tabs.component';
import { ViewTabsComponent } from './view-tabs/view-tabs.component';
import { HttpClientModule } from '@angular/common/http';
import {ReactiveFormsModule} from '@angular/forms';
import {CharacterService} from './character/character.service';
import {UniverseService} from './universe/universe.service';
import {LocationService} from './location/location.service';
import {ItemService} from './item/item.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    CreationTabsComponent,
    ViewTabsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatTabsModule,
    MatInputModule,
    MatFormFieldModule,
    MatSelectModule,
    MatDividerModule,
    MatCardModule,
    MatButtonModule,
    MatTableModule
  ],
  providers: [UniverseService, LocationService, ItemService, CharacterService],
  bootstrap: [AppComponent]
})
export class AppModule { }
