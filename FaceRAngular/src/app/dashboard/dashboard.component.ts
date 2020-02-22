import { Component, OnInit, AfterViewInit, ComponentFactoryResolver } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements OnInit {

  constructor(private user: UserService, private router: Router, private http: HttpClient) {
  }

  facultyname: string;

  response;
  imageURL;

  ngOnInit() {}

  public setUser() {
    this.facultyname = localStorage.getItem('username');
    return this.facultyname;
  }

  public onLogout() {
    localStorage.setItem('username', '');
    localStorage.setItem('refresh', '');
    localStorage.setItem('access', '');
    this.facultyname = 'UserName';
    this.router.navigate(['login']);
    this.user.userset = false;
  }

  openprofile() {
    this.router.navigate(['profile', this.facultyname]);
  }

}
