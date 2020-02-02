import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-login-component',
  templateUrl: './login-component.component.html',
  styleUrls: ['./login-component.component.css'],
  providers: [UserService]
})
export class LoginComponentComponent implements OnInit {

  input;
  constructor(private userService: UserService) { }

  ngOnInit() {
    this.input = {
      username : '',
      password : '',
    };
  }

  onLogin() {
    this.userService.LoginUser(this.input).subscribe(
      response => {
        alert('User Logged Successfully' + this.input.username);
      },
      error => {
        console.log('error', error);
      }
    );
  }

}
