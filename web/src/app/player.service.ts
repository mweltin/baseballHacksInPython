import { Injectable } from '@angular/core';
import { Player } from './player';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Team } from './team';

@Injectable({
  providedIn: 'root'
})

export class PlayerService {

  constructor(private http: HttpClient) { }

  private playerUrl = 'api/player';
  private rosterUrl = 'api/roster';
  private pichOutcomeUrl =  'api/pitch_outcome';
  private battingAverageUrl =  'api/batting_average';
  private sluggingUrl =  'api/slugging';
  private OBPUrl =  'api/on_base_percentage';
  private ERAUrl =  'api/era';
  public selectedPlayer: Player;
  public currentDisplayYear: number;
  // Observable display date sources
  private displayYear = new Subject<number>();

  // Observable Player sources
  private selectedPlayerSource = new Subject<Player>();
  // Observable Player streams (this is what consumers of the service subscribe to)
  palyerChangeAccouncement = this.selectedPlayerSource.asObservable();

  // Observable streams (this is what consumers of the service subscribe to)
  displayYearAccouncement = this.displayYear.asObservable();


  // Publish the fact that the selected team has changed.
  announcePlayerChange(dPlyaer: Player) {
    this.selectedPlayerSource.next(dPlyaer);
  }

  setSelectePlayer(inPlyaer: Player): void {
    this.selectedPlayer = inPlyaer;
    this.announcePlayerChange(inPlyaer);
  }

  // Publish the fact that the selected display Year has changed.
  announceDisplayDateChange(year: number) {
    this.displayYear.next(year);
    this.currentDisplayYear = year;
  }

  getPlayer(id: string): Observable<Player> {
    const url = `${this.playerUrl}/${id}`;
    return this.http.get<Player>(url);
  }

  getPlayersByTeam(team: Team): Observable<Player[]> {
    const url = `${this.rosterUrl}/${team.abbrev}`;
    return this.http.get<Player[]>(url);
  }

  getPitchOutcomeByPlayer(player: Player): Observable<any[]> {
    const url = `${this.pichOutcomeUrl}/${player.id}`;
    return this.http.get<any[]>(url);
  }

  getBattingAverageByPlayer(player: Player): Observable<any[]> {
    const url = `${this.battingAverageUrl}/${player.id}`;
    return this.http.get<any[]>(url);
  }

  getSluggingByPlayer(player: Player): Observable<any[]> {
    const url = `${this.sluggingUrl}/${player.id}`;
    return this.http.get<any[]>(url);
  }

  getOnBasePercentageByPlayer(player: Player): Observable<any[]> {
    const url = `${this.OBPUrl}/${player.id}`;
    return this.http.get<any[]>(url);
  }

  getEarnedRunAverageByPlayer(player: Player): Observable<any[]> {
    const url = `${this.ERAUrl}/${player.id}`;
    return this.http.get<any[]>(url);
  }
}
