import { Component, OnInit } from "@angular/core";
import { PageChangedEvent } from "ngx-bootstrap/pagination";
import { fakeProducts } from "./fake-products";

@Component({
  selector: "app-product-list",
  templateUrl: "./product-list.component.html",
  styleUrls: ["./product-list.component.css"]
})
export class ProductListComponent implements OnInit {
  itemsPerPage = 12;
  maxSize = 5;
  products = fakeProducts;
  returnedProducts: any[];
  constructor() { }

  ngOnInit() {
    this.returnedProducts = this.products.slice(0, this.itemsPerPage);
  }

  pageChanged(event: PageChangedEvent): void {
    const startItem = (event.page - 1) * event.itemsPerPage;
    const endItem = event.page * event.itemsPerPage;
    this.returnedProducts = this.products.slice(startItem, endItem);
    //click phân trang thì scroll nhảy lên cùng
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
