// en este archivo se definen los objetos que seran usados para manejar el estado del carrito de compras
import {Course} from '../services/course.service';

export interface CartItem {
  course: Course;
  quantity: number;
}


export interface CartState {
  items: CartItem[];
}

export const initialCartState: CartState = {
  items: [],
};