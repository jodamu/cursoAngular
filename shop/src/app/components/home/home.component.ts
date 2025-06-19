import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-home',
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  images:string[] = [
    "https://storagevefe.blob.core.windows.net/angulardeveloper/items/slide-1.jpg",
    "https://storagevefe.blob.core.windows.net/angulardeveloper/items/slide-2.jpg"
 
  ];

  currentIndex=signal<number>(0); 
  interval!: any;

  ngOnInit() {
    this.interval = setInterval(() => {
      this.currentIndex.update(index => (index + 1) % this.images.length);
    }, 2000); // Change image every 3 seconds
  }
  ngOnDestroy() {
      clearInterval(this.interval);
    
  }

}
