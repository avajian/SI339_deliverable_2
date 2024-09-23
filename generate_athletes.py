import csv
import os

def process_athletes(folder_path='athletes/mens_team'):
    all_athletes = {}
    all_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    for csv_file in all_files:
        full_path = os.path.join(folder_path, csv_file)
        with open(full_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            all_data = list(reader)
            
            info = {
                'name': all_data[0][0],
                'athlete_id': all_data[1][0],
            }
            
            athlete_results = {}
            in_athlete_section = False
            i = 0

            for row in all_data:
                if not row:
                    continue
                if row[0] == 'Name' and row[1] == 'Overall Place':
                    in_athlete_section = True
                if in_athlete_section and len(row) >= 8 and row[0] != 'Name':

                    athlete_results[i] = {
                        'name': row[0] if row[0] else 'N/A',
                        'overall_place': row[1] if row[1] else 'N/A',
                        'grade': row[2] if row[2] else 'N/A',
                        'time': row[3] if row[3] else 'N/A',
                        'date': row[4] if row[4] else 'N/A',
                        'meet': row[5] if row[5] else 'N/A',
                        'comments': row[6] if row[6] else 'N/A',
                        'photo': row[7] if row[7] else 'N/A'
                    }
                    i += 1

            all_athletes[info['athlete_id']] = {'info': info, 'results': athlete_results.copy()}
    return all_athletes
