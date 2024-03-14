import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private http: HttpClient) {}

  loginUser(loginData:object) {
    return this.http.post('http://your-mongodb-endpoint/login', loginData);
  }
}