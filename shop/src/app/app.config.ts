import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

import { routes } from './app.routes';
import { provideStore, provideState } from '@ngrx/store';
import { cartFeatureKey, cartReducer } from './store/cart.reducer';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }), 
    provideRouter(routes),
     provideStore(),
     provideHttpClient(),
     provideState(cartFeatureKey, cartReducer)
    ]
};
