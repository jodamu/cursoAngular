import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { CourseTableComponent } from './components/course-table/course-table.component';
import { CourseFormComponent } from './components/course-form/course-form.component';
import { CourseEditComponent } from './components/course-edit/course-edit.component';
import { CourseCartComponent } from './components/course-cart/course-cart.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'courses', component: CourseTableComponent },
    { path: 'add', component: CourseFormComponent },
    { path: 'edit/:id', component: CourseEditComponent },
    { path: 'dashboard', component: DashboardComponent },
    { path: 'cartCourse', component: CourseCartComponent },


    { path: '**', redirectTo: '' }
    
];
