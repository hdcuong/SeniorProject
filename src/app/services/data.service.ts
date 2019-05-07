import { Injectable } from '@angular/core';
import { BehaviorSubject } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private resultSource = new BehaviorSubject([]);
  currentResult = this.resultSource.asObservable();

  constructor() { }

  changeResult(item: any[]) {
    this.resultSource.next(item);
  }
}
