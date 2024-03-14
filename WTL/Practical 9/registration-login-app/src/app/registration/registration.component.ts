import { Component } from '@angular/core';
import { RegistrationService } from '../registration.service';

@Component({
  selector: 'app-registration',
  standalone: true,
  imports: [],
  templateUrl: './registration.component.html',
  styleUrl: './registration.component.css'
})
export class RegistrationComponent {
  constructor(private registrationService: RegistrationService) {}

  onSubmit(formData: object) {
    this.registrationService.registerUser(formData).subscribe(
      response => {
        alert('Registration successful!');
      },
      error => {
        console.error('Error:', error);
      }
    );
  }
}
