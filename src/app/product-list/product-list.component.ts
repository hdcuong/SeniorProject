import { Component, OnInit } from "@angular/core";
import { DataService } from "../services/data.service";

@Component({
  selector: "app-product-list",
  templateUrl: "./product-list.component.html",
  styleUrls: ["./product-list.component.css"]
})
export class ProductListComponent implements OnInit {
  returnedProducts: any[];
  
  constructor(private data: DataService) {
  }

  ngOnInit() {
    this.data.currentResult.subscribe(data => this.returnedProducts = data);
  }
}
