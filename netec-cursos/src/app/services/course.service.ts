import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { catchError, Observable, throwError, timeout } from 'rxjs';



export interface Course {
  id: number;
  name: string;
  description: string;
  duration: string;
  level: string;
  price: number;
}



@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private http:HttpClient=inject(HttpClient);
  private baseUri:string="http://localhost:8084/course";

  getAllCourses():Observable<Course[]>{
    return this.http.get<Course[]>(`${this.baseUri}`)
    .pipe(
      timeout(3000),
      catchError(err=>{
          console.log("error al obtener api data ", err);
          return throwError(()=>new Error("error get api data"));
        }) 
    );
  }

  getCourseById(id:number):Observable<Course>{
    return this.http.get<Course>(`${this.baseUri}/${id}`)
    .pipe(
      timeout(3000),
      catchError(err=>{
          console.log("error al obtener api data ", err);
          return throwError(()=>new Error("error get api data"));
        }) 
    );
  }
  

  insertCourse(course:Course):Observable<Course>{
    return this.http.post<Course>(`${this.baseUri}`,course)
    .pipe(
      timeout(3000),
      catchError(err=>{
          console.log("error al insertar api data ", err);
          return throwError(()=>new Error("error insertar api data"));
        }) 
    );
  }

  updateCourse(course:Course):Observable<Course>{
    return this.http.put<Course>(`${this.baseUri}`,course)
    .pipe(
      timeout(3000),
      catchError(err=>{
          console.log("error al actualizar api data ", err);
          return throwError(()=>new Error("error actualizar api data"));
        }) 
    );
  }

  deleteCourse(id:number):Observable<Course>{
    return this.http.delete<Course>(`${this.baseUri}/${id}`)
    .pipe(
      timeout(3000),
      catchError(err=>{
          console.log("error al eliminar api data ", err);
          return throwError(()=>new Error("error eliminar api data"));
        }) 
    );
  }


}
