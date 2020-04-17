import psycopg2
import constants
import glob
import csv
from zipfile import ZipFile

def main() -> None:
    """
    Take CSV files crated by bevent_process and insert that data into the bbhip database
    :return: None
    """
    try:
        constants.main()
    except Exception as exp:
        print("You have an error in you constants file.  You must correct that before you can continue")
        print(exp.args[0])
        exit(1)

    connect_str = "user='bbhip' host='localhost' dbname='bbhip'"
    conn = psycopg2.connect(connect_str)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    insert_game_query = """
        INSERT INTO game (
            game_date,
            game_num,
            dow,
            visitor_name,
            visitor_league,
            visitor_game_num,
            home_name,
            home_league,
            home_game_num,
            visitor_score,
            home_score,
            game_len_outs,
            day_night, 
            completion_info,
            forfeit_info,
            protest_info,
            park_id,
            attendance,
            game_time,
            visitor_line_score,
            home_line_score,
            visitor_at_bats,
            visitor_hits,
            visitor_doubles,
            visitor_triples,
            visitor_home_runs,
            visitor_rbi,
            visitor_sacrifice_hits,
            visitor_sacrifice_flies,
            visitor_hit_by_pitch,
            visitor_walks ,
            visitor_intentional_walks,
            visitor_strikeouts,
            visitor_stolen_bases,
            visitor_caught_stealing,
            visitor_grounded_into_double_plays,
            visitor_awarded_first_on_catcher_interference,
            visitor_left_on_base,
            visitor_pitches_used,
            visitor_individual_earned_runs,
            visitor_team_earned_runs,
            visitor_wild_pitches,
            visitor_balks,
            visitor_putouts,
            visitor_assists,
            visitor_errors,
            visitor_passed_balls,
            visitor_double_plays,
            visitor_triple_plays,
            home_at_bats,
            home_hits,
            home_doubles,
            home_triples,
            home_home_runs,
            home_rbi,
            home_sacrifice_hits,
            home_sacrifice_flies,
            home_hit_by_pitch,
            home_walks ,
            home_intentional_walks,
            home_strikeouts,
            home_stolen_bases,
            home_caught_stealing,
            home_grounded_into_double_plays,
            home_awarded_first_on_catcher_interference,
            home_left_on_base,
            home_pitches_used,
            home_individual_earned_runs,
            home_team_earned_runs,
            home_wild_pitches,
            home_balks,
            home_putouts,
            home_assists,
            home_errors,
            home_passed_balls,
            home_double_plays,
            home_triple_plays,
            ump_hp_id,
            ump_hp_name,
            ump_1b_id,
            ump_1b_name,
            ump_2b_id,
            ump_2b_name,
            ump_3b_id,
            ump_3b_name,
            ump_lf_id,
            ump_lf_name,
            ump_rf_id,
            ump_rf_name,
            visitor_mgr_id,
            visitor_mgr_name,
            home_mgr_id,
            home_mgr_name,
            winning_pitcher_id,
            winning_pitcher_name,
            losing_pitcher_id,
            losing_pitcher_name,
            saving_pitcher_id,
            saving_pitcher_name,
            game_winning_rbi_batter_id,
            game_winning_rbi_batter_name,
            visitor_starting_pitcher_id,
            visitor_starting_pitcher_name,
            home_starting_pitcher_id,
            home_starting_pitcher_name,
            visitor_pos_1_id,
            visitor_pos_1_name,
            visitor_pos_1_def_pos,
            visitor_pos_2_id,
            visitor_pos_2_name,
            visitor_pos_2_def_pos,
            visitor_pos_3_id,
            visitor_pos_3_name,
            visitor_pos_3_def_pos,
            visitor_pos_4_id,
            visitor_pos_4_name,
            visitor_pos_4_def_pos,
            visitor_pos_5_id,
            visitor_pos_5_name,
            visitor_pos_5_def_pos,
            visitor_pos_6_id,
            visitor_pos_6_name,
            visitor_pos_6_def_pos,
            visitor_pos_7_id,
            visitor_pos_7_name,
            visitor_pos_7_def_pos,
            visitor_pos_8_id,
            visitor_pos_8_name,
            visitor_pos_8_def_pos,
            visitor_pos_9_id,
            visitor_pos_9_name,
            visitor_pos_9_def_pos,
            home_pos_1_id, 
            home_pos_1_name,
            home_pos_1_def_pos,
            home_pos_2_id,
            home_pos_2_name,
            home_pos_2_def_pos,
            home_pos_3_id,
            home_pos_3_name,
            home_pos_3_def_pos,
            home_pos_4_id,
            home_pos_4_name,
            home_pos_4_def_pos,
            home_pos_5_id,
            home_pos_5_name,
            home_pos_5_def_pos,
            home_pos_6_id,
            home_pos_6_name,
            home_pos_6_def_pos,
            home_pos_7_id,
            home_pos_7_name,
            home_pos_7_def_pos,
            home_pos_8_id,
            home_pos_8_name,
            home_pos_8_def_pos,
            home_pos_9_id,
            home_pos_9_name,
            home_pos_9_def_pos,
            addition_info,
            acquisition_type 
        )
        VALUES (
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s,
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s, 
            %s 
        );
    """
    for zip_arc in glob.glob(constants.RETRO_DATA_DIR + '/' + "gl*.zip"):
        with ZipFile(zip_arc, 'r') as zipObj:
            zipObj.extractall(constants.RETRO_DATA_DIR + '/')

    for glob_item in glob.glob(constants.RETRO_DATA_DIR + '/GL*.TXT'):
        print("Processing file: " + glob_item)
        with open(glob_item, newline='') as csv_file:
            event_row = csv.reader(csv_file)
            for insert_data in event_row:
                # over come limitation in csv.reader convert empty values (i.e. '') to None (i.e. NULL)
                insert_data[0] = insert_data[0][0:4] + '-' + insert_data[0][4:6] + '-' + insert_data[0][6:8]
                for i in range(len(insert_data)):
                    if insert_data[i] == '':
                        insert_data[i] = None
                cursor.execute(insert_game_query, insert_data)
        print("Finished processing file: " + glob_item)


if __name__ == "__main__":
    main()
