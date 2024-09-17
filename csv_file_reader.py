
# for grabbing csv file data from 'meets' folder
import csv
import os

folder_path = 'meets'
all_files = []
meet = {}
info = {}
team_results = {}
athlete_results = {}

in_team_section = False
in_athlete_section = False

# find all files in folder and filter only csv
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        all_files.append(file)

print(len(all_files))

for csv_file in all_files:
    full_path = os.path.join(folder_path, csv_file)
    with open(full_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        all_data = list(reader) # gets all data in one file
        
        meet_id = csv_file.replace('csv', '')
        
        info = {
            'meet_name': all_data[0][0],
            'meet_date': all_data[1][0],
            'meet_link': all_data[2][0],
            'meet_desc': all_data[3][0]
        }

        team_results.clear()
        athlete_results.clear()

        for row in all_data:
            if not row:
                continue
            
            if row[0] == 'Place' and row[1] == 'Team' and row[2] == 'Score':
                in_team_section = True
                in_athlete_section = False

            if row[0] == 'Place' and row[1] == 'Grade' and row[2] == 'Name': # add the rest of column options
                in_team_section = False
                in_athlete_section = True
            
            if in_team_section and len(row) >= 3 and row[0] != 'Place':
                team_results[row[1]] = {  # Use team name as the key
                    'place': row[0],
                    'team': row[1],
                    'score': row[2]
                }
            
            if in_athlete_section and len(row) >= 8 and row[0] != 'Place':
                athlete_results[row[2]] = {  # Use athlete's name as the key
                    'place': row[0],
                    'grade': row[1],
                    'name': row[2],
                    'athlete_link': row[3],
                    'time': row[4],
                    'team': row[5],
                    'team_link': row[6],
                    'profile_pic': row[7]
                }

    # Add team_results and athlete_results to the meet info
    meet[meet_id] = {
        'info': info,
        'team_results': team_results.copy(),  # Copy to avoid overwriting
        'athlete_results': athlete_results.copy()  # Copy to avoid overwriting
    }


# info for one meet
meet_info = meet[meet_id]['info']
meet_name = meet_info['meet_name']
meet_date = meet_info['meet_date']
meet_link = meet_info['meet_link']
meet_desc = meet_info['meet_desc']

athletes = meet[meet_id]['athlete_results']
teams = meet[meet_id]['team_results']


# team_results = meet[meet_id]['team_results'][0]

# Start building the HTML structure
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel = "stylesheet" href = "css/reset.css">
   <link rel = "stylesheet" href = "css/style.css">
   <title>{meet_name} Country Meet</title>
</head>
<body>
<p>{meet_name}</p>
<p>{meet_date}</p>
<p>{meet_link}</p>
<p>{meet_desc}</p>
<br>
<p>team results: {teams}</p>
<br>
<p>athlete results: {athletes} </p>
<br>
</body>
</html>
'''

# Writing the HTML to a file
with open("output.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_content)