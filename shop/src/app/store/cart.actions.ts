import { createAction, props } from '@ngrx/store';
import { Item } from '../services/item.service';
/*  se definen las acciones (emetodos) que se usaran
para modificar el estado */

export const addToCart = createAction(
    '[cart] Add to Cart',
    props<{ item: Item }>()
);

export const removeFromCart = createAction(
    '[cart] Remove from Cart',
    props<{ idItem:number }>()
);

export const clearCart = createAction(
    '[cart] Clear Cart'
);