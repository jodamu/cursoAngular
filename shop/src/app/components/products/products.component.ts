import { Component, inject, signal } from '@angular/core';
import { Item, ItemService } from '../../services/item.service';
import { Router } from '@angular/router';
import { CurrencyPipe } from '@angular/common';

@Component({
  selector: 'app-products',
  imports: [CurrencyPipe],
  templateUrl: './products.component.html',
  styleUrl: './products.component.css'
})
export class ProductsComponent {
  private service:ItemService=inject(ItemService);
  private router=inject(Router);
  items=signal<Item[]>([]);

  ngOnInit() {
    this.service.getItems().subscribe({
      next: (data) => {
        this.items.set(data);
      },
      error: (err) => {
        console.error("Error al obtener los productos", err);
      }
    });
  }

}
