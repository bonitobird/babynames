# Baby Names
Playing with the Social Security Administration's published baby names data. 

https://www.ssa.gov/oact/babynames/limits.html

# Two main applications

### Jupyter Notebook - babynames_analysis.ipynb
This is my original file used to analyze baby names. 
1) Looped over the .txt files to create one large dataframe
2) User inputs a name and a year of interest
3) Prints some data about the name
    - total number born since 1880 of each gender
    - total number born in the year of interest of each gender
    - total number born since the year of interest of each gender
4) Plots the number of babies born with the chosen name each year of each gender

### Flask web app - app.py, data_analysis.py, all_names.h5, /static, /templates
This is my very first flask web app. User inputs a name and it generates the plot from (4) above.  
[Deployed Babyname Web App](http://bonitobird.pythonanywhere.com)


2020/05/10: Initial commit  
2020/05/11: Bugs fixed
1) Name can now be entered in any form of lower/upper cases and it still works
2) The placeholder in the text box always shows "Enter Name". (Note: Initially, this was filled with the previous name entered.)
3) Instead of generating the dataframe of all the names each time a name is entered, I made a large file (type hdf5) with all the names that are only read once. Reduced the processing time from 25 seconds down to 2-3 secs.
