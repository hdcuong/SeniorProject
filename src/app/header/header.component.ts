import { Component, OnInit } from "@angular/core";
import { TranslateService } from "@ngx-translate/core";
import { HttpClient, HttpParams } from '@angular/common/http';
import { DataService } from "../services/data.service";

@Component({
  selector: "app-header",
  templateUrl: "./header.component.html",
  styleUrls: ["./header.component.css"]
})
export class HeaderComponent implements OnInit {
  price = 1;
  producer = "NoBrand";
  object = "student";
  arrayResults: any[];
  constructor(public translate: TranslateService, private http: HttpClient, private data: DataService) {
    translate.use('vi');
    localStorage.removeItem('results');
  }

  onSubmit() {
    let price = this.price;
    let producer = this.producer;
    let object = this.object;
    let httpParams = new HttpParams().append('price', price.toString())
      .append('brand', producer).append('typelt', object);
    const url = 'http://localhost:5000/request';
    this.http.get<any[]>(url, { params: httpParams }).subscribe(data => {
      this.arrayResults = data;
      // this.data.setResults(this.arrayResults);
      // this.test = this.data.getResult();
      // console.log(this.test);
      this.data.changeResult(this.arrayResults);
      console.log(this.arrayResults);
    }
    );
  }

  ngOnInit() {
    this.data.currentResult.subscribe(data => this.arrayResults = data);
  }
}
