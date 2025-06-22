import { Component, Inject, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Course, CourseService } from '../../services/course.service';
import { ActivatedRoute, Router } from '@angular/router';
import { take } from 'rxjs';

@Component({
  selector: 'app-course-edit',
  imports: [ReactiveFormsModule],
  templateUrl: './course-edit.component.html',
  styleUrl: './course-edit.component.css'
})
export class CourseEditComponent {
  private services: CourseService = inject(CourseService);
  private build = inject(FormBuilder)
  private router = inject(Router)
  private route = inject(ActivatedRoute)
  courseId?: number;



  form = this.build.group({
    id: [0],
    name: ['', [Validators.required, Validators.minLength(3)]],
    description: ['', Validators.required],
    duration: ['', Validators.required],
    level: ['', Validators.required],
    price: [0, [Validators.required, Validators.min(0)]],
  });

  ngOnInit() {
    const idParam = this.route.snapshot.paramMap.get('id');


    if (idParam) {
      this.services.getCourseById(+idParam).subscribe(curso => {
      this.form.patchValue(curso); // ✅ aquí sí funciona
      });
    }

  }

  onSubmit() {
    let id = this.form.controls.id.value!;
    let name = this.form.controls.name.value!;
    let description = this.form.controls.description.value!;
    let duration = this.form.controls.duration.value!;
    let level = this.form.controls.level.value!;
    let price = this.form.controls.price.value!;

    let course: Course = {
      id: id,
      name: name,
      description: description,
      duration: duration,
      level: level,
      price: price
    }
    this.services.updateCourse(course).pipe(take(1)).subscribe({
      next: value => {
        this.router.navigate(['courses'])
      },
      error: err => { console.log(err) }
    });
  }

}
