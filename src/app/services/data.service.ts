import { Injectable } from '@angular/core';
import { BehaviorSubject } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private resultSource = new BehaviorSubject([]);
  currentResult = this.resultSource.asObservable();
  constructor() { }
  // setResults(item: any[]) {
  //   localStorage.setItem('results', JSON.stringify(item));
  // }
  // getResult() {
  //   return JSON.parse(localStorage.getItem('results'));
  // }
  changeResult(item: any[]) {
    this.resultSource.next(item);
  }
}
