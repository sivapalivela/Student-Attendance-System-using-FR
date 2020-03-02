import { Component, OnInit, Input, AfterViewInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  Position: any;
  PROFILE_PICTURE: any;
  Bio: any;
  DoB: Date;
  Skills: Array<string>;
  Achievement: Array<string>;
  Education: Array<string>;
  Languages: Array<string>;
  BelongingDept: any;
  Email: any;
  FirstName: any;
  LastName: any;
  Name: any;
  Location: any;
  Facebook: any;
  Twitter: any;
  Linkedin: any;
  Github: any;
  Stackoverflow: any;
  Gender: any;
  Mobile: any;

  constructor(private http: HttpClient, private route: ActivatedRoute, private router: Router, public user: UserService) { }

  ngOnInit() {
    this.initize();
  }

  initize() {
    this.http.get('http://127.0.0.1:8000/appfr1/api/students/getprofile?user=' + this.user.username).subscribe(data => {
      this.Position = data[0].Position;
      this.PROFILE_PICTURE  = data[0].Profile_Picture;
      this.Bio = data[0].Bio;
      this.DoB = data[0].DoB;
      this.BelongingDept = data[0].Belonging_Dept;
      this.Location = data[0].Location;
      this.Facebook = data[0].Facebook;
      this.Linkedin = data[0].Linkedin;
      this.Twitter = data[0].Twitter;
      this.Github = data[0].Github;
      this.Stackoverflow = data[0].Stackoverflow;
      this.Gender = data[0].Gender;
      this.Mobile = data[0].Mobile;
      this.Skills = this.user.splitter(data[0].Skills);
      this.Achievement = this.user.splitter(data[0].Achievements);
      this.Education = this.user.splitter(data[0].Education);
      this.Languages = this.user.splitter(data[0].Languages);
    });

    this.http.get('http://127.0.0.1:8000/appfr1/api/students/getuser?user=' + this.user.username).subscribe(
      data => {
        this.Email = data[0].email;
        this.FirstName = data[0].first_name;
        this.LastName = data[0].last_name;
        this.Name = this.FirstName + ' ' + this.LastName;
      }
    );

  }

  closeit() {
    this.router.navigate(['dashboard']);
  }

}
