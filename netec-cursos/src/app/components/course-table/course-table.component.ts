import { Component, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { CourseService, Course } from '../../services/course.service';
import { toSignal } from '@angular/core/rxjs-interop';
import { catchError, of } from 'rxjs';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-course-table',
  imports: [RouterLink,CommonModule,FormsModule],
  templateUrl: './course-table.component.html',
  styleUrl: './course-table.component.css'
})
export class CourseTableComponent {
  filtro: string = '';
  private service:CourseService=inject(CourseService);
  private router=inject(Router);
  private courses=signal<Course[]>([]);



  ngOnInit(){
    this.service.getAllCourses().subscribe({
      next: values => {this.courses.set(values)},
      error: err => {console.log(err)},
      complete: () => {console.log('complete')}
    })
  }
 
cursosFiltrados(): Course[] {
    return this.courses().filter((c: Course) =>
  c.name.toLowerCase().includes(this.filtro.toLowerCase())
    );
  }




}
