import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { DogTableComponent } from './components/dog-table/dog-table.component';
import { DogFormComponent } from './components/dog-form/dog-form.component';
import { NotFoundComponent } from './components/not-found/not-found.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'dogs', component: DogTableComponent },
    { path: 'add', component: DogFormComponent },
    {path: '**', component: NotFoundComponent}
];
