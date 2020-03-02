import { Component, OnInit, AfterViewInit, Input, Inject } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { UserService } from '../user.service';

@Component({
  selector: 'app-profiledialog',
  templateUrl: './profiledialog.component.html',
  styleUrls: ['./profiledialog.component.css']
})
export class ProfiledialogComponent implements OnInit {

  formData = new FormData();
  userData = new FormData();


  Position: any;
  PROFILE_PICTURE: any;
  Bio: any;
  DoB: Date;
  Skills: any;
  Achievement: any;
  Education: any;
  Languages: any;
  BelongingDept: any;
  Email: any;
  FirstName: any;
  LastName: any;
  Location: any;
  Facebook: any;
  Twitter: any;
  Linkedin: any;
  Github: any;
  Stackoverflow: any;
  Gender: any;
  Mobile: any;

  constructor(private http: HttpClient, public user: UserService, private formBuilder: FormBuilder) {
  }

  ngOnInit() {
    this.initialize();
  }

  formchange(id: string, vali: string) {
    if (id == 'first_name' || id == 'last_name' || id == 'email') {
      this.userData.append(id, vali);
    } else {
      if (id == 'Achievements' || id == 'Education' || id == 'Skills' || id == 'Languages') {
        const obj = this.user.formatter(vali);
        this.formData.append(id, obj);
      } else {
        this.formData.append(id, vali);
      }
    }
  }

  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.formData.append(event.target.id, file);
    }
  }

  profileupdate() {
    this.user.uploadprofile(this.formData).subscribe(
      (data) => {
        alert('Updated Successfully');
      }
    );

    this.user.uploadprofileuser(this.userData).subscribe(
      (data) => {
        console.log('Working Fine');
      }
    );
  }

  initialize() {
    this.http.get('http://127.0.0.1:8000/appfr1/api/students/getprofile?user=' + this.user.username).subscribe(data => {
      this.user.id = data[0].id;
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
      this.Skills = this.user.convertostring(this.user.splitter(data[0].Skills));
      this.Achievement = this.user.convertostring(this.user.splitter(data[0].Achievements));
      this.Education = this.user.convertostring(this.user.splitter(data[0].Education));
      this.Languages = this.user.convertostring(this.user.splitter(data[0].Languages));
      console.log(data);
    });

    this.http.get('http://127.0.0.1:8000/appfr1/api/students/getuser?user=' + this.user.username).subscribe(
      data => {
        this.Email = data[0].email;
        this.FirstName = data[0].first_name;
        this.LastName = data[0].last_name;
      }
    );
  }

}
