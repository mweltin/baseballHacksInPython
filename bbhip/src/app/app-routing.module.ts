import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PlayerComponent } from './player/player.component';
import { TeamComponent } from './team/team.component';
import { RosterComponent } from './roster/roster.component';


const routes: Routes = [
  { path: 'player/:player_id', component: PlayerComponent },
  { path: 'teams', component: TeamComponent },
  { path: 'roster', component: RosterComponent },
  { path: '', redirectTo: 'teams', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { enableTracing: true})],
  exports: [RouterModule]
})

export class AppRoutingModule { }
