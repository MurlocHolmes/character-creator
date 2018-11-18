import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CreateService {

  private url = 'http://localhost:5000';
  constructor(private http: HttpClient) { }

  setUrl(url) {
    this.url = url;
  }

  createUniverse(data) {
    console.log(data);
    return this.http.post(this.url + '/universe/create', data).subscribe();
  }

  createCharacter(data) {
    console.log(data);
    return this.http.get(this.url + '/character/create');
  }

  createLocation(data) {
    console.log(data);
    return this.http.get(this.url + '/location/create');
  }

  createItem(data) {
    console.log(data);
    return this.http.get(this.url + '/item/create');
  }
}
