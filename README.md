This repository includes:

  - python file to read and populate html templates (main.py and helper functions: generate files)
  - csv files (meets and athletes)
  - images folder
  - index.html (populated html template for a user posted on github pages)
  - Juan_Luis_Llanes.html (second populated html template)

The python program contains two generate files: generate_athletes.py and generate_meets.py to read in csv content from both athletes and meets.
They work by first creating a list to hold all of the file data, then creating a dictionary to hold the results of each csv file. 
The csv.reader function reads in the file and creates a list of the data. This data is iterated through by row and given a variable name based on its position. 
Then it populates the created html template by replacing placeholders with the correct data. If there is no data in a row/col, the empty data will be replaced with 'n/a'

To run the program, type in 'python3 main.py' in the terminal. An output folder will be created with two sub folders of html content: athletes and meets. 
All data from the csv files outlined in the folder 'meets' and 'athletes' will be utilized.

'main.py' creates two populated templates. The athletes files is the main html file, while users will be able to click on meet links within the progress report to open the other populated template created for meets. This functionality has not yet been implemented, but an example is in the repository as "37th Early Bird Open Mens 5000 Meters HS..."
