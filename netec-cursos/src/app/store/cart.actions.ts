import { createAction, props } from '@ngrx/store';
import { Course } from '../services/course.service';
/*  se definen las acciones (emetodos) que se usaran
para modificar el estado */

export const addToCart = createAction(
    '[cart] Add to Cart',
    props<{ course: Course }>()
);

export const removeFromCart = createAction(
    '[cart] Remove from Cart',
    props<{ idCourse:number }>()
);

export const clearCart = createAction(
    '[cart] Clear Cart'
);