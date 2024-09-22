The python program contains two generate files to read in csv content from both athletes and meets.
They work by first creating a list to hold all of the file data, then 
creating a dictionary to hold the results of each csv file. 
The csv.reader function reads in the file and creates a list of the data. 
This data is iterated through by row and given a variable name based on its position. Then it populates
the created html template by replacing placeholders with the correct data.
