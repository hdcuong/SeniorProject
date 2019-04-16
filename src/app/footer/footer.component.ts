import { Component, OnInit } from '@angular/core';
import { listLogo } from "./fake-logo";

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  logos = listLogo;
  constructor() { }

  ngOnInit() {
  }

}
