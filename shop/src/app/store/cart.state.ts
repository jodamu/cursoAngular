// en este archivo se definen los objetos que seran usados para manejar el estado del carrito de compras
import {Item} from '../services/item.service';

export interface CartItem {
  item: Item;
  quantity: number;
}


export interface CartState {
  items: CartItem[];
}

export const initialCartState: CartState = {
  items: [],
};