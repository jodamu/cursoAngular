import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Course, CourseService } from '../../services/course.service';
import { Router } from '@angular/router';
import { take } from 'rxjs';

@Component({
  selector: 'app-course-form',
  imports: [ReactiveFormsModule],
  templateUrl: './course-form.component.html',
  styleUrl: './course-form.component.css'
})
export class CourseFormComponent {
  private services:CourseService = inject(CourseService);  
  private build=inject(FormBuilder)  
  private router=inject(Router)

  form = this.build.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      description: ['', Validators.required],
      duration: ['', Validators.required],
      level: ['', Validators.required],
      price: [0, [Validators.required, Validators.min(0)]],
    });

  onSubmit(){
    let name = this.form.controls.name.value!;
    let description = this.form.controls.description.value!;
    let duration = this.form.controls.duration.value!;
    let level = this.form.controls.level.value!;
    let price = this.form.controls.price.value!;
    
    let course:Course={
      id: 0,
      name: name,
      description: description,
      duration: duration,
      level: level,
      price: price
    }
    this.services.insertCourse(course).pipe(take(1)).subscribe({
      next: value => {
        this.router.navigate(['courses'])
      },
      error: err=>{console.log(err)}
    });
   
    
  }

}
