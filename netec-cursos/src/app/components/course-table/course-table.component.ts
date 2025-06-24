import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CourseService, Course } from '../../services/course.service';
import { toSignal } from '@angular/core/rxjs-interop';
import { catchError, of } from 'rxjs';
import { Store } from '@ngrx/store'
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { selectTotalItems } from '../../store/cart.selector';
import { addToCart } from '../../store/cart.actions';
import * as alertifyjs from 'alertifyjs';

@Component({
  selector: 'app-course-table',
  imports: [RouterLink,CommonModule,FormsModule],
  templateUrl: './course-table.component.html',
  styleUrl: './course-table.component.css'
})
export class CourseTableComponent {
  filtro: string = '';
  private service:CourseService=inject(CourseService);
  
  private store=inject(Store);

  courses=toSignal(this.service
    .getAllCourses()
    .pipe(catchError(err=> {
      console.log(err);
      return of([])
    })),
    {initialValue: [] as Course[]});


   

  countItems=toSignal(this.store
    .select(selectTotalItems),
   {initialValue:0});

   addToCartItem(course:Course){
    alertifyjs.success('Item '+course.name+' agregado al carrito corectamente');
      this.store.dispatch(addToCart({course}));
   }




}
