import { Component, inject,signal } from '@angular/core';
import { Dog, DogService } from '../../services/dog.service';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { RouterLink } from '@angular/router';
import { Router } from '@angular/router';
import { take } from 'rxjs';
// import { toSignal } from '@angular/core/rxjs-interop';
// import { catchError, of } from 'rxjs';

@Component({
  selector: 'app-dog-table',
  imports: [MatCardModule,MatIconModule,RouterLink],
  templateUrl: './dog-table.component.html',
  styleUrl: './dog-table.component.css'
})
export class DogTableComponent {

  private service:DogService = inject(DogService);
  private router=inject(Router);
  dogs = signal<Dog[]>([]);

  //uso del tosignal
  // private dogs2=toSignal(this.service.getDogs().pipe(
  //   catchError(err=>{ 
  //     console.log(err);
  //     return of ([])})
      
  // ), {initialValue: [] as Dog[]});
 
  ngOnInit(){
    this.service.getDogs().subscribe({
      next: values=> {this.dogs.set(values)},
      error: err => {console.error(err)}
    })
  }

  ngOnDestroy(){  
    this.dogs.set([]);
  }

  deleteDog(id:number){
    this.service.deleteDog(id).pipe(take(1)).subscribe({
      next: value=>{this.router.navigate(['dogs'])},
      error: err => {console.error(err)}
    })
  }

 


}
