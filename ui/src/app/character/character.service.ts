import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, Subject} from 'rxjs/index';

@Injectable({
  providedIn: 'root'
})
export class CharacterService {

  private url = 'http://localhost:5000';
  public characters: Subject<any> = new Subject();
  constructor(private http: HttpClient) { }

  setUrl(url) {
    this.url = url;
  }

  public getAllCharacters() {
    this.http.get(this.url + '/character/all').subscribe(data => {
      this.characters.next(data);
    });
  }

  createCharacter(data) {
    const post = this.transformFromInputToPost(data);
    return this.http.post(this.url + '/character/create', post);
  }

  transformFromInputToPost(data) {
    const post = {};
    post['attributes'] = {};
    for (const datum in data) {
      if (!datum.includes('attribute')) {
        post[datum] = data[datum];
      } else {
        const key = datum.split('-')[2];
        post['attributes'][data['attribute-name-' + key]] = data['attribute-value-' + key];
      }
    }
    return post;
  }

}
