import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private http: HttpClient) {}

  loginUser(loginData:object) {
    return this.http.post('http://localhost:3000/login', loginData);
  }
}