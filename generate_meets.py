import csv
import os

def process_meets(folder_path='meets'):
    meets = {}
    all_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    for csv_file in all_files:
        full_path = os.path.join(folder_path, csv_file)
        with open(full_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            all_data = list(reader)

            meet_id = csv_file.replace('.csv', '')
            meet_info = {
                'meet_name': all_data[0][0],
                'meet_date': all_data[1][0],
                'meet_link': all_data[2][0],
                'meet_desc': all_data[3][0]
            }

            team_results, athlete_results = {}, {}
            in_team_section, in_athlete_section = False, False

            for row in all_data:
                if not row:
                    continue
                if row[0] == 'Place' and row[1] == 'Team':
                    in_team_section = True
                    in_athlete_section = False
                if row[0] == 'Place' and row[1] == 'Grade':
                    in_team_section = False
                    in_athlete_section = True
                
                if in_team_section and len(row) >= 3 and row[0] != 'Place':
                    team_results[row[1]] = {
                        'place': row[0],
                        'team': row[1],
                        'score': row[2]
                    }
                if in_athlete_section and len(row) >= 8 and row[0] != 'Place':
                    athlete_results[row[2]] = {
                        'place': row[0],
                        'grade': row[1],
                        'name': row[2],
                        'athlete_link': row[3],
                        'time': row[4],
                        'team': row[5],
                        'team_link': row[6],
                        'profile_pic': row[7]
                    }

            meets[meet_id] = {'info': meet_info, 'team_results': team_results, 'athlete_results': athlete_results}
    return meets
