import { Component, OnInit } from '@angular/core';
import { PlayerService } from '../player.service';
import { TeamService } from '../team.service';
import { Player } from '../player';
import { Team } from '../team';
import { TeamFilterInterface } from '../teamFilter';
import { NavService } from '../nav.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.less']
})
export class NavComponent implements OnInit {

  public selectedTeam: Team;
  public selectedPlayer: Player;
  public dropDownText: string;

  constructor(
    public playerSrv: PlayerService,
    public teamSrv: TeamService,
    public navSrv: NavService
  ) {
    teamSrv.teamChangeAccouncement.subscribe(
      res => {
        this.selectedTeam  = res;
    });
    playerSrv.palyerChangeAccouncement.subscribe(
      res => {
        this.selectedPlayer = res;
    });
  }

  ngOnInit(): void {
    this.dropDownText = 'Filter Teams';
  }

  unsetPlayer(): void{
    this.playerSrv.setSelectePlayer(null);
  }

  unsetTeam(): void{
    this.teamSrv.setActiveTeam(null);
  }

  setFilter( filter: TeamFilterInterface ): void {
    if ( !filter) {
      this.dropDownText = 'Filter Teams';
    } else {
      this.dropDownText = filter.league;
      this.dropDownText  = filter.division ? this.dropDownText + ' - ' + filter.division : this.dropDownText;
    }
    this.navSrv.announceFilterChange(filter);
  }
}
