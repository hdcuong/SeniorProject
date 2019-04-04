import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-product-carousel",
  templateUrl: "./product-carousel.component.html",
  styleUrls: ["./product-carousel.component.css"]
})
export class ProductCarouselComponent implements OnInit {
  images1 = "assets/logo/carousel-fptshop.png";
  images2 = "assets/logo/carousel-fptshop2.png";
  images3 = "assets/logo/carousel-tgdd.png";
  images4 = "assets/logo/carousel-tgdd2.png";
  constructor() {}

  ngOnInit() {}
}
