import {Component, ElementRef, OnInit, ViewChild, Input } from '@angular/core';
import { Universe } from '../models/universe';
import { Location } from '../models/location';
import { Item } from '../models/item';
import { Character } from '../models/character';
import {DomSanitizer} from '@angular/platform-browser';
import {ViewService} from '../services/view.service';
import {CreateService} from '../services/create.service';
import {UniverseService} from '../universe/universe.service';
import {LocationService} from '../location/location.service';
import {ItemService} from '../item/item.service';
import {CharacterService} from '../character/character.service';
@Component({
  selector: 'app-creation-tabs',
  templateUrl: './creation-tabs.component.html',
  styleUrls: ['./creation-tabs.component.css']
})
export class CreationTabsComponent implements OnInit {

  public types: object[];
  public counter: number;
  @Input() universes: any;
  public currentValues = {};
  @ViewChild('attributes') attributes: ElementRef;
  constructor(private el: ElementRef,
              private viewService: ViewService,
              private universeService: UniverseService,
              private locationService: LocationService,
              private itemService: ItemService,
              private characterService: CharacterService) {

    this.types = [Universe, Location, Item, Character];
    this.counter = 0;
  }

  ngOnInit() {
  }

  createAttribute(event: any) {
    event.preventDefault();
    this.counter++;
  }

  createRange(number: number) {
    const range: number[] = [];
    for (let i = 0; i <= number; i++) {
      range.push(i);
    }
    return range;
  }

  create(type: string) {
    if (type === 'Universe') {
      this.universeService.createUniverse(this.currentValues).subscribe(() => {
        this.universeService.getAllUniverses();
      });
    }
    if (type === 'Location') {
      this.locationService.createLocation(this.currentValues).subscribe(() => {
        this.locationService.getAllLocations();
      });
    }
    if (type === 'Item') {
      this.itemService.createItem(this.currentValues).subscribe(() => {
        this.itemService.getAllItems();
      });
    }
    if (type === 'Character') {
      this.characterService.createCharacter(this.currentValues).subscribe(() => {
        this.characterService.getAllCharacters();
      });
    }
  }

  onChange(label: string, value: any) {
    console.log(value);
    this.currentValues[label.toLowerCase()] = value;
  }

  reset() {
    this.counter = 0;
  }
}
