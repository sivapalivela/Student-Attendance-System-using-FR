import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UserService } from '../user.service';

@Component({
  selector: 'app-addstudent',
  templateUrl: './addstudent.component.html',
  styleUrls: ['./addstudent.component.css']
})
export class AddstudentComponent implements OnInit {

  loginForm: FormGroup;
  submitted = false;

  constructor(private formBuilder: FormBuilder, private user: UserService) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      rollnumber: ['', Validators.required],
      branch: ['', Validators.required],
      year: ['', Validators.required],
      section: ['', Validators.required],
      semester: ['', Validators.required],
      image: ['']
    });
  }

  onChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.loginForm.get('image').setValue(file);
    }
  }

  get f() {
    return this.loginForm.controls;
  }

  onSubmit() {

    this.submitted = true;
    if (this.loginForm.invalid) {
      return;
    }

    const formData = new FormData();
    formData.append('rollnumber', this.loginForm.value.rollnumber);
    formData.append('branch', this.loginForm.value.branch);
    formData.append('year', this.loginForm.value.year);
    formData.append('section', this.loginForm.value.section);
    formData.append('semester', this.loginForm.value.semester);
    formData.append('file', this.loginForm.value.image);
    this.user.upload2(formData).subscribe(
      (data) => {
        alert(data);
      }
    );

  }
}
