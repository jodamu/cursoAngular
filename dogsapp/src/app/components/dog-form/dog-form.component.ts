import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Dog, DogService } from '../../services/dog.service';
import { take } from 'rxjs';
import { Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-dog-form',
  imports: [ReactiveFormsModule, MatCardModule, MatInputModule,MatFormFieldModule,MatButtonModule],
  templateUrl: './dog-form.component.html',
  styleUrl: './dog-form.component.css'
})
export class DogFormComponent {
  private service:DogService = inject(DogService);
  private build=inject(FormBuilder);
  private router=inject(Router);
  form = this.build.group({
    breed:['',[
                Validators.required, 
                Validators.maxLength(150),
                Validators.pattern('/^[A-Z,a-z,\s]/')
              ]],
    description:['',[
                Validators.required, 
                Validators.minLength(5),
                Validators.maxLength(200),
                Validators.pattern('/^[A-Z,a-z,\s]/')
              ]],
    urlImage:['',[
                Validators.required,
                Validators.maxLength(200),
                Validators.pattern(/^https?:\/\/[^\s]+?\.(jpg|jpeg|png)$/)
              ]]
  });

  submit(){
    if(this.form.valid){
      let breed=this.form.controls.breed.value!;
      let description=this.form.controls.description.value!;
      let urlImage=this.form.controls.urlImage.value!;

      let dog:Dog={
        id:0,
        breed:breed,
        description:description,
        urlImage:urlImage
      };
      this.service.insertDog(dog).pipe(take(1)).subscribe({
        next: value=>{this.router.navigate(['dogs'])},
        error: err => {console.error(err)}
      })

   

      }
      
  }

}

