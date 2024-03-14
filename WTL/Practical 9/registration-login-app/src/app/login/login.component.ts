import { Component } from '@angular/core';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})

export class LoginComponent {
  constructor(private loginService: LoginService) {}

  onSubmit(formData:object) {
    this.loginService.loginUser(formData).subscribe(
      response => {
        alert('Welcome ' + formData.username + '!');
        // Redirect to the desired page here
      },
      error => {
        console.error('Error:', error);
      }
    );
  }
}