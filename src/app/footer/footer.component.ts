import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  images1="assets/logo/logo-fptshop.jpg";
  images2="assets/logo/logo-tdgg.png";
  constructor() { }

  ngOnInit() {
  }

}
