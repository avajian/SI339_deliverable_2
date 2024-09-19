from generate_athletes import process_athletes
from generate_meets import process_meets
import os
import re


def generate_athlete_pages(athletes):
    for athlete_id, athlete in athletes.items():
        name = athlete['info']['name']
        athlete_results = athlete['results']

        # Start building the HTML structure
        html_content = f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{name}'s Cross Country Progress</title>
        </head>
        <body>

            <!-- Header Section -->
            <header>
                <h1>{name}'s Progress Report</h1>
                <p><strong>Athlete ID:</strong> {athlete_id}</p>
                <p>A summary of {name}'s cross country performances across multiple seasons.</p>
            </header>

            <!-- Progress Table Section -->
            <section>
                <h2>Performance Overview</h2>
                <table border="1" cellpadding="10" cellspacing="0">
                    <thead>
                        <tr>
                            <th>Year</th>
                            <th>Meet</th>
                            <th>Overall Place</th>
                            <th>Grade</th>
                            <th>Time</th>
                            <th>Date</th>
                            <th>Comments</th>
                        </tr>
                    </thead>
                    <tbody>'''

        # Loop through athlete results and output each row
        for result_id, result in athlete_results.items():

            html_content += f'''
                <tr>
                    <td>{result.get('year', 'N/A')}</td>
                    <td>{result.get('meet', 'N/A')}</td>
                    <td>{result.get('overall_place', 'N/A')}</td>
                    <td>{result.get('grade', 'N/A')}</td>
                    <td>{result.get('time', 'N/A')}</td>
                    <td>{result.get('date', 'N/A')}</td>
                    <td>{result.get('comments', 'N/A')}</td>
                </tr>'''

        html_content += '''
                    </tbody>
                </table>
            </section>

            <!-- Favorite Photos Section -->
            <section>
                <h3>Favorite Photos</h3>
                <p>Upload your favorite moments from the season below:</p>
                <form method="POST" action="/upload" enctype="multipart/form-data">
                    <input type="file" name="photo" accept="image/*">
                    <button type="submit">Upload Photo</button>
                </form>
            </section>

            <!-- Accessible Print Option -->
            <section>
                <h3>Printable Version</h3>
                <p>For a clean, printable version of {name}'s progress, <a href="#" onclick="window.print()">click here</a>.</p>
            </section>

        </body>
        </html>
        '''

        output_folder = "output/athletes"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with open(f"{output_folder}/{name}.html", "w", encoding="utf-8") as file:
            file.write(html_content)


def generate_meet_pages(meets):
    for meet_id, meet in meets.items():
        meet_name = meet['info']['meet_name']
        meet_date = meet['info']['meet_date']
        meet_link = meet['info']['meet_link']
        meet_desc = meet['info']['meet_desc']
        teams = meet['team_results']
        athletes = meet['athlete_results']

        athlete_rows = ''.join([
            f'''
            <tr>
                <td>{athlete["place"]}</td>
                <td>{athlete["grade"]}</td>
                <td><a href="{athlete["athlete_link"]}">{athlete["name"]}</a></td>
                <td>{athlete["time"]}</td>
                <td><a href="{athlete["team_link"]}">{athlete["team"]}</a></td>
                <td><img src="{athlete["profile_pic"]}" alt="{athlete["name"]}" width="50" height="50"></td>
            </tr>
            ''' for athlete in athletes.values()
        ])

        # Build HTML content with a table structure for team and athlete results
        html_content = f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="css/reset.css">
            <link rel="stylesheet" href="css/style.css">
            <title>{meet_name} - Country Meet</title>
        </head>
        <body>
            <h1>{meet_name}</h1>
            <p><strong>Date:</strong> {meet_date}</p>
            <p><strong>Link:</strong> <a href="{meet_link}">{meet_link}</a></p>
            <p><strong>Description:</strong> {meet_desc}</p>
            
            <h2>Team Results</h2>
            <table border="1" cellpadding="5" cellspacing="0">
                <thead>
                    <tr>
                        <th>Place</th>
                        <th>Team</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join([f'<tr><td>{team["place"]}</td><td>{team_name}</td><td>{team["score"]}</td></tr>' for team_name, team in teams.items()])}
                </tbody>
            </table>

            <h2>Athlete Results</h2>
            <table border="1" cellpadding="5" cellspacing="0">
                <thead>
                    <tr>
                        <th>Place</th>
                        <th>Grade</th>
                        <th>Name</th>
                        <th>Time</th>
                        <th>Team</th>
                        <th>Profile</th>
                    </tr>
                </thead>
                <tbody>
                    {athlete_rows}
                </tbody>
            </table>

        </body>
        </html>
        '''

        output_folder = "output/meets"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with open(f"{output_folder}/{meet_name}.html", "w", encoding="utf-8") as file:
            file.write(html_content)

if __name__ == "__main__":
    athletes = process_athletes()
    meets = process_meets()

    generate_athlete_pages(athletes)
    generate_meet_pages(meets)
