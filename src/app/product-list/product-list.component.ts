import { Component, OnInit } from "@angular/core";
// import { PageChangedEvent } from "ngx-bootstrap/pagination";
import { DataService } from "../services/data.service";

@Component({
  selector: "app-product-list",
  templateUrl: "./product-list.component.html",
  styleUrls: ["./product-list.component.css"]
})
export class ProductListComponent implements OnInit {
  itemsPerPage = 12;
  maxSize = 5;
  returnedProducts: any[];
  constructor(private data: DataService) {
  }

  ngOnInit() {
    this.data.currentResult.subscribe(data => this.returnedProducts = data);
  //  console.log(this.returnedProducts);
  }

  // pageChanged(event: PageChangedEvent): void {
  //   const startItem = (event.page - 1) * event.itemsPerPage;
  //   const endItem = event.page * event.itemsPerPage;
  //   this.returnedProducts.slice(startItem, endItem);
  //   //click phân trang thì scroll nhảy lên cùng
  //   document.body.scrollTop = 0;
  //   document.documentElement.scrollTop = 0;
  // }

  // showResults() {
  //   this.returnedProducts = this.data.getResult();
  //   return this.returnedProducts;
  // }
}
