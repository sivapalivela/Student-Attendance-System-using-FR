import { Component, OnInit, AfterViewInit, ComponentFactoryResolver } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup } from '@angular/forms';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit, AfterViewInit {

  constructor(private user: UserService, private router: Router, private http: HttpClient, private formBuilder: FormBuilder) {
  }

  facultyname: string;
  displayedColumns: string[] = ['Roll Number', 'Status'];
  datasource = [];

  br_opt : Array<string> = [];
  se_opt : Array<string> = [];
  pe_opt : Array<string> = [];
  PRESENT_LIST = false;
  MAIN_COMP = true;

  form: FormGroup;
  response;
  imageURL;

  ngOnInit() {
    this.form = this.formBuilder.group({
      Branch : '',
      Studying_Year : '',
      Period : '',
      Section : '',
      Semester : '',
      Video: [''],
      Faculty_ID : ''
    });
  }

  ngAfterViewInit() {
    this.get_data(this.facultyname);
  }

  public setUser() {
    this.facultyname = localStorage.getItem('username');
    return this.facultyname;
  }

  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('Video').setValue(file);
    }
  }

  onSe(event) {
    let temp_Sec = event.value;
    this.form.get('Section').setValue(temp_Sec);
  }

  onPe(event) {
    let temp_Per = event.value
    this.form.get('Period').setValue(temp_Per);
  }

  onBr(event) {
    let temp_Br = event.value;
    let new_Br = temp_Br.split(' ');
    this.form.get('Branch').setValue(new_Br[2]);
    this.form.get('Studying_Year').setValue(new_Br[7]);
    this.form.get('Semester').setValue(new_Br[11]);
  }

  get_data(teacher) {
    this.http.get('http://127.0.0.1:8000/appfr1/api/students/getallocatedclass?user=' + teacher).subscribe(data => {
      // tslint:disable-next-line: forin
      for (const ob in data) {
        const val = data[ob];
        this.se_opt.push(val['Allocated_Section']);
        this.pe_opt.push(val['Allocated_Period']);
        // tslint:disable-next-line: max-line-length
        const varible = 'Branch - ' + val['Allocated_Branch'] + ' , Studying Year - ' + val['Allocate_Studying_Year'] + ' , Semester - ' + val['Allocated_Semester'];
        this.br_opt.push(varible);
      }
    });
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.form.get('Video').value);
    formData.append('Branch', this.form.get('Branch').value);
    formData.append('Studying_Year', this.form.get('Studying_Year').value);
    formData.append('Period', this.form.get('Period').value);
    formData.append('Section', this.form.get('Section').value);
    formData.append('Semester', this.form.get('Semester').value);
    formData.append('Faculty_ID', this.facultyname);
    this.MAIN_COMP = false;
    this.user.upload(formData).subscribe(
      (res) => {
        this.PRESENT_LIST = true;
        this.MAIN_COMP = true;
        // tslint:disable-next-line: forin
        for (const i in res) {
          this.datasource.push(i);
        }
        console.log(this.datasource);
      },
      (err) => {
        alert(err);
      }
    );
  }
  public display() {
    if (this.PRESENT_LIST === false && this.MAIN_COMP === false) {
      return true;
    }
    return false;
  }

  public onLogout() {
    localStorage.setItem('username', '');
    localStorage.setItem('refresh', '');
    localStorage.setItem('access', '');
    this.facultyname = 'UserName';
    this.router.navigate(['login']);
    this.user.userset = false;
  }

}
