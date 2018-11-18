import { Component } from '@angular/core';
import {ViewService} from './services/view.service';
import {CreateService} from './services/create.service';
import {CharacterService} from './character/character.service';
import {UniverseService} from './universe/universe.service';
import {LocationService} from './location/location.service';
import {ItemService} from './item/item.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ui';
  api_url = 'http://localhost:5000';
  private data = {'Universe': [], 'Location': [], 'Item': [], 'Character': []};

  constructor(
              private universeService: UniverseService,
              private locationService: LocationService,
              private itemService: ItemService,
              private characterService: CharacterService,) {
    // viewService.setUrl(this.api_url);
    // createService.setUrl(this.api_url);
    universeService.universes.subscribe((data) => {
      this.data['Universe'] = data;
    });
    locationService.locations.subscribe((data) => {
      this.data['Location'] = data;
    });
    itemService.items.subscribe((data) => {
      this.data['Item'] = data;
    });
    characterService.characters.subscribe((data) => {
      this.data['Character'] = data;
    });
    universeService.getAllUniverses();
    locationService.getAllLocations();
    itemService.getAllItems();
    characterService.getAllCharacters();
  }
}
