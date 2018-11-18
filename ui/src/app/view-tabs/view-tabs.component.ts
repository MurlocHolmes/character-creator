import {Component, ElementRef, Input, OnInit, ViewChild} from '@angular/core';
import { Universe } from '../models/universe';
import { Location } from '../models/location';
import { Item } from '../models/item';
import { Character } from '../models/character';
import {ViewService} from '../services/view.service';

@Component({
  selector: 'app-view-tabs',
  templateUrl: './view-tabs.component.html',
  styleUrls: ['./view-tabs.component.css']
})
export class ViewTabsComponent implements OnInit {

  public types: object[];
  public counter: number;
  @Input() data;
  @ViewChild('attributes') attributes: ElementRef;
  constructor(private viewService: ViewService) {
    this.types = [Universe, Location, Item, Character];
    this.counter = 0;
  }

  public echoThings() {
    console.log(this);
  }
  public echoItem(item) {
    console.log(item);
  }
  ngOnInit() {
  }

}
