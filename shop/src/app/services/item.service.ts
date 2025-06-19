import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, timeout, map, catchError, throwError } from 'rxjs';

export interface Item {
  id: number;
  name: string;
  description: string;
  amount: number;
  urlImage: string;
}

@Injectable({
  providedIn: 'root'
})
export class ItemService {
  private http:HttpClient=inject(HttpClient);
  private baseUri:string="http://localhost:8083/item";

 getItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.baseUri)
    .pipe(
      timeout(3000), 
      // map(anyDataList => anyDataList.map(any => any as Item) ),
      catchError(err=>{
        console.log("error al obtener api data ", err);
        return throwError(()=>new Error("error get api data"));
      }) 
   );
  }

  getItemById(id: number): Observable<Item> {
    return this.http.get<Item>(`${this.baseUri}/${id}`)
    .pipe(
      timeout(3000), 
      catchError(err=>{
        console.log("error al obtener api data ", err);
        return throwError(()=>new Error("error get api data"));
      }) 
    );
  }





}
