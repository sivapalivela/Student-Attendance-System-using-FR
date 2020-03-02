import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  userset = false;

  id: number;
  username: any;

  DJANGO_SERVER = 'http://127.0.0.1:8000/appfr1/api/students/take_attendance';
  DJANGO_SERVER2 = 'http://127.0.0.1:8000/appfr1/api/students/add_student';
  LOGIN_URL = 'http://127.0.0.1:8000/api/login/';



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

  authenticate(uname: string, password: string) {
    const data = { 'username': uname, 'password': password };
    return this.http.post(this.LOGIN_URL, data, this.options)
      .pipe(
        catchError(this.handleError)
      );
  }

  upload(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER}`, formData);
  }

  upload2(formData) {
    return this.http.post<any>(`${this.DJANGO_SERVER2}`, formData);
  }

  uploadprofile(formData) {
    const DJANGO_URL = 'http://127.0.0.1:8000/appfr1/api/students/updateprofile/' + this.id.toString();
    return this.http.patch<any>(`${DJANGO_URL}`, formData);
  }

  uploadprofileuser(userdata) {
    const DJANGO_URL = 'http://127.0.0.1:8000/appfr1/api/students/updateprofileuser/' + this.id.toString();
    return this.http.patch<any>(`${DJANGO_URL}`, userdata);
  }

  splitter(splitval: string ) {
    const Skills: Array<string> = [];
    const newsplit = splitval.slice(1, splitval.length - 1).split(',');
    for (const st of newsplit) {
      const newst = st.trim().split(':');
      const newst2 = newst[0].slice(1, newst[0].length - 1);
      Skills.push(newst2);
    }
    return Skills;
  }

  convertostring(convertparam) {
    let temp = '';
    for (const ob of convertparam) {
      temp += (ob + ' :: ');
    }
    return temp;
  }

  formatter(formatit) {
    const temp = formatit.split('::');
    const obj = {};
    for (const ob of temp) {
      obj[ob] = 'True';
    }
    return JSON.stringify(obj);
  }
}
