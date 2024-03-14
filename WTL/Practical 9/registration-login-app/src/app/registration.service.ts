import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class RegistrationService {
  constructor(private http: HttpClient) {}

  registerUser(userData:object) {
    return this.http.post('http://your-mongodb-endpoint', userData);
  }
}
