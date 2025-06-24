import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { Store } from '@ngrx/store';
import { selectCartItems, selectCartTotal } from '../../store/cart.selector';
import { CartItem } from '../../store/cart.state';
import { clearCart, removeFromCart } from '../../store/cart.actions';

import * as alertifyjs from 'alertifyjs';
import { CommonModule } from '@angular/common';
import { Course } from '../../services/course.service';

@Component({
  selector: 'app-course-cart',
  imports: [CommonModule],
  templateUrl: './course-cart.component.html',
  styleUrl: './course-cart.component.css'
})
export class CourseCartComponent {
 private store = inject(Store);
  items = toSignal(
    this.store.select(selectCartItems),
    {initialValue: [] as CartItem[]}
    )
  total = toSignal(
    this.store.select(selectCartTotal),
    {initialValue: 0}
  )

  deleteItem(id:number){
    alertifyjs.error('Item  Eliminado corectamente');
    this.store.dispatch(removeFromCart({idCourse:id}))
  }

  clearCart(){
    this.store.dispatch(clearCart())
  }
}
