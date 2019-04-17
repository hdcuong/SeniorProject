import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { CommonModule } from "@angular/common";
import { Routes, RouterModule } from "@angular/router";
import { TranslateModule, TranslateLoader } from "@ngx-translate/core";
import { HttpClientModule, HttpClient } from "@angular/common/http";
import { TranslateHttpLoader } from "@ngx-translate/http-loader";
import { PaginationModule } from "ngx-bootstrap/pagination";

import { HeaderComponent } from "./header/header.component";
import { FooterComponent } from "./footer/footer.component";
import { DefaultComponent } from "./default/default.component";
import { ErrorComponent } from "./error/error.component";
import { ProductListComponent } from "./product-list/product-list.component";
import { ProductCarouselComponent } from "./product-carousel/product-carousel.component";

const routes: Routes = [
  {
    path: "",
    component: DefaultComponent,
    children: [{ path: "product-list", component: ProductListComponent }]
  },
  { path: "**", component: ErrorComponent }
];

export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http);
}

@NgModule({
  declarations: [
    HeaderComponent,
    FooterComponent,
    DefaultComponent,
    ErrorComponent,
    ProductListComponent,
    ProductCarouselComponent
  ],
  imports: [
    PaginationModule.forRoot(),
    RouterModule.forRoot(routes),
    BrowserModule,
    HttpClientModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: HttpLoaderFactory,
        deps: [HttpClient]
      }
    }),
    CommonModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
