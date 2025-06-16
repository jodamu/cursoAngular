import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, timeout, map, catchError, throwError } from 'rxjs';


export interface Dog{
  id:number,
  breed:string,
  description:string,
  urlImage:string
}

@Injectable({
  providedIn: 'root'
})
export class DogService {
  private http: HttpClient = inject(HttpClient);
  private baseUri = 'http://localhost:8082/dog';


  getDogs(): Observable<Dog[]> {
    return this.http.get<any[]>(this.baseUri)
      .pipe(timeout(3000),
        map(anyDataList => anyDataList.map(any => any as Dog)),
        catchError(err => {
          console.error('Error al obtener api data', err);
          return throwError(() => new Error("error get api data"))
        }
        )
      );
  }

  insertDog(dog: Dog): Observable<void> {
    return this.http.post<void>(this.baseUri + '/add', dog)
      .pipe(timeout(3000),
        catchError(err => {
          console.error('Error al insertar dog', err);
          return throwError(() => new Error("error insert dog"))
        }
        )
      );
  }

  updateDog(dog: Dog): Observable<void> {
    return this.http.put<void>(this.baseUri + '/', dog)
      .pipe(timeout(3000),
        catchError(err => {
          console.error('Error al actualizar dog', err);
          return throwError(() => new Error("error update dog"))
        }
        )
      );
  }

  deleteDog(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUri}/${id}`)
      .pipe(timeout(3000),
        catchError(err => {
          console.error('Error al eliminar dog', err);
          return throwError(() => new Error("error delete dog"))
        }
        )
      );
  }

}
