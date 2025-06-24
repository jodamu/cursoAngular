import { Component, signal } from '@angular/core';
import { RouterLink } from '@angular/router';


@Component({
  selector: 'app-home',
  imports: [RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
images: string[] = [
  "https://picsum.photos/id/1011/800/400",
  "https://picsum.photos/id/1005/800/400",
  "https://picsum.photos/id/1012/800/400",
  "https://picsum.photos/id/1033/800/400",
  "https://picsum.photos/id/1021/800/400",
  "https://picsum.photos/id/1025/800/400",
  "https://picsum.photos/id/1027/800/400",
  "https://picsum.photos/id/1043/800/400",
  "https://picsum.photos/id/1056/800/400",
  "https://picsum.photos/id/1069/800/400",
  "https://picsum.photos/id/1070/800/400",
  "https://picsum.photos/id/1074/800/400",
  "https://picsum.photos/id/1081/800/400",
  "https://picsum.photos/id/1082/800/400",
  "https://picsum.photos/id/1084/800/400",
  "https://picsum.photos/id/1080/800/400",
  "https://picsum.photos/id/1032/800/400",
  "https://picsum.photos/id/1020/800/400",
  "https://picsum.photos/id/1037/800/400",
  "https://picsum.photos/id/1045/800/400"
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
