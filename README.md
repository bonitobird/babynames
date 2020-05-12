# Baby Names
Playing with the Social Security Administration's published baby names data. 

https://www.ssa.gov/oact/babynames/limits.html

# Two main applications

### Jupyter Notebook - babynames_analysis.ipynb
This is my orginal file used to analysis baby names. 
1) Looped over the .txt files to create on large dataframe
2) User input a name and a year of interest
3) Prints some data about the name
    - total number born since 1880 of each gender
    - total number born in the year of interest of each gender
    - total number born since the year of interest of each gender
4) Plots the number of babies born with chosen name each year of each gender

### Flask web app
This is my very first flask web app. User inputs a name and it generates the plot from (4) above.
 
Bugs fixed to date:
1) Name can now be entered in any from of lower/upper cases and it still works
2) The placeholder in the text box always shows "Enter Name". (Note: Intially, this filled with the previous name entered.)
3) Instead of generating the dataframe of all the names each time a name is entered, I made a large file (type hdf5) with all the names that is only read in once. Reduced the processing time from 25 seconds down to 2-3 secs.
