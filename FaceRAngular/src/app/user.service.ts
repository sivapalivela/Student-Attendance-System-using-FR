import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  LoginUser(userData): Observable<any> {
    return this.http.post('http://localhost:8000/auth/', userData);
  }
}
