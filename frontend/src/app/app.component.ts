import { HttpClient } from '@angular/common/http';
import { Component, Injectable} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

@Injectable({ providedIn: 'root' })
export class AppComponent {
  constructor(private http: HttpClient) {}
   // @ViewChild('f') signupForm: NgForm;
  // title = 'image-frontend';
  text: String;
  result: String;

  onSubmit()
  {
    this.http.get<any>('https://reqres.in/api/users?page=2').subscribe(
      (response) => {
        console.log("Success Response" + response);
        this.result = response},
      (error) => { console.log("Error happened" + error)},
      () => { console.log("the subscription is completed")}
  );
  }
}
