import { createReducer, on } from '@ngrx/store';
import { initialCartState } from './cart.state';
import * as CartActions from './cart.actions';

/*
Se implementan las acciones definidas en actions
*/

export const cartFeatureKey='cart';

export const cartReducer = createReducer(
    initialCartState,

    on(CartActions.addToCart, (state, {course})=>{
      const search = state.items.find(t=>t.course.id === course.id);

      if(search){
        return {
            ...state,
            items: state.items.map(
                t=>t.course.id === course.id ? {...t, quantity: t.quantity+1}:t
            )
        };

      }

      return {
        ...state,
        items: [...state.items, {course, quantity:1}]
      }
    }),

    on(CartActions.removeFromCart, (state, {idCourse})=>{
        return {
            ...state,
            items: state.items.filter(t=>t.course.id !== idCourse)
        }
    }),

    on(CartActions.clearCart, (state)=>{
        return {
            ...state,
            items:[]
        }
    })

);
