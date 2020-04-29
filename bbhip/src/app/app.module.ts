import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlayerComponent } from './player/player.component';
import { HttpClientModule } from '@angular/common/http';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { TeamComponent } from './team/team.component';
import { TeamFilter } from './team/team.pipe';
import { PitchOutcomesComponent } from './pitch-outcomes/pitch-outcomes.component';

@NgModule({
  declarations: [
    AppComponent,
    PlayerComponent,
    TeamComponent,
    TeamFilter,
    PitchOutcomesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
