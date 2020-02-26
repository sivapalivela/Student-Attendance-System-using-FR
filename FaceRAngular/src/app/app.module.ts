import 'hammerjs';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { JwtModule } from '@auth0/angular-jwt';
import { AuthService } from './auth/auth.service';
import { UserService } from '../app/user.service';
import { ReactiveFormsModule } from '@angular/forms';
import { MatMenuModule } from '@angular/material/menu';
import { MatCardModule } from '@angular/material/card';
import {MatTableModule} from '@angular/material/table';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import {MatSelectModule} from '@angular/material/select';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatInputModule } from '@angular/material/input';
import {MatDividerModule} from '@angular/material/divider';
import { BrowserModule } from '@angular/platform-browser';
import {MatProgressSpinnerModule} from '@angular/material/progress-spinner';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { AuthGuardService } from './auth/auth-guard.service';
import { MatFormFieldModule } from '@angular/material/form-field';
import { DashboardComponent } from './dashboard/dashboard.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponentComponent } from './login-component/login-component.component';
import { ProfileComponent } from './profile/profile.component';
import { AttendanceComponent } from './attendance/attendance.component';
import {MatTabsModule} from '@angular/material/tabs';
import {MatDialogModule, MatDialogRef} from '@angular/material/dialog';
import { AddstudentComponent } from './addstudent/addstudent.component';
import { ProfiledialogComponent } from './profiledialog/profiledialog.component';

export function tokenGetter() {
  return localStorage.getItem('token');
}

@NgModule({
  declarations: [
    AppComponent,
    LoginComponentComponent,
    DashboardComponent,
    ProfileComponent,
    AttendanceComponent,
    AddstudentComponent,
    ProfiledialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    MatFormFieldModule,
    MatToolbarModule,
    MatCardModule,
    MatInputModule,
    MatButtonModule,
    MatMenuModule,
    ReactiveFormsModule,
    MatSidenavModule,
    MatSelectModule,
    MatDividerModule,
    MatTableModule,
    MatTabsModule,
    MatProgressSpinnerModule,
    MatDialogModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: tokenGetter,
        whitelistedDomains : ['localhost:4200'],
        blacklistedRoutes : ['example.com/examplebadroute']
      }
    })
  ],
  entryComponents: [
    AddstudentComponent,
    ProfiledialogComponent
  ],
  providers: [UserService, AuthGuardService, AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
