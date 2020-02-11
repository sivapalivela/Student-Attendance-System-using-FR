import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  userset = false;
  DJANGO_SERVER: string = "http://127.0.0.1:8000/appfr1/api/students/take_attendance";
  login_url = 'http://127.0.0.1:8000/api/login/';
  private options = { headers: new HttpHeaders().set('Content-Type', 'application/json') };

  constructor(private http: HttpClient) { }

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error('An error occurred:', error.error.message);
    } else {
      alert(error.error.non_field_errors);

    }
    return throwError(
      'Something bad happened; please try again later.');
  }

  authenticate(username: string, password: string) {
    const data = { 'username': username, 'password': password };
    return this.http.post(this.login_url, data, this.options)
      .pipe(
        catchError(this.handleError)
      );
  }

  upload(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER}`, formData);
  }
}
