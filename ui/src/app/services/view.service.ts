import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ViewService {

  private url = 'http://localhost:5000';
  constructor(private http: HttpClient) { }

  setUrl(url) {
    this.url = url;
  }

  getAllUniverses() {
    return this.http.get(this.url + '/universe/all');
  }

  getAllCharacters() {
    return this.http.get(this.url + '/character/all');
  }

  getAllLocations() {
    return this.http.get(this.url + '/location/all');
  }

  getAllItems() {
    return this.http.get(this.url + '/item/all');
  }
}
