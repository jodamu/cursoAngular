import { Component, inject, signal } from '@angular/core';
import { Course, CourseService } from '../../services/course.service';
import { Router, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dashboard',
  imports: [RouterLink,CommonModule,FormsModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
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
