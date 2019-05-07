import { Component, OnInit } from "@angular/core";
import { carouselList } from "./carouselList";

@Component({
  selector: "app-product-carousel",
  templateUrl: "./product-carousel.component.html",
  styleUrls: ["./product-carousel.component.css"]
})
export class ProductCarouselComponent implements OnInit {
  
  image = "assets/logo/carousel-fptshop.png";
  productCarousels = carouselList;
  constructor() {}

  ngOnInit() {}
}
