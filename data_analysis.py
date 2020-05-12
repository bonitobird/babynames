import pandas as pd
import glob
import os
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# import h5py

""" Prepping some functions """
# Read multiple files into one dataframe whilst adding custom columns
def my_csv_reader(path, year):
    d = pd.read_csv(path, names = ['Name', 'Gender', 'Quantity'] )
    d['Year'] = year # adding column for multi/single thread
    return d

def natural_sort_key2(s):
    """
    This function provides natural sorting of values
    Adapted from: Jeff Atwood (https://blog.codinghorror.com/sorting-for-humans-natural-sort-order/)
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split(re.compile('([0-9]+)'),s)]

""" Import baby name files """
def name_plot(n):
    n = n.lower()
    n = n.capitalize()
    years = list(range(1880, 2019, 1))

    # df = pd.DataFrame()

    # path_base = 'namesnational' # use your base path
    # all_files = glob.glob(os.path.join('namesnational', "*.txt"))
    # all_files = sorted(all_files, key=natural_sort_key2)
    # year_index = 0
    # for f in all_files:
    #     df = pd.concat([df, my_csv_reader(f, years[year_index])], ignore_index = True)
    #     year_index += 1
    # export_csv = df.to_csv('all_names_db.csv', index=None, header=True)
    
    # export_hdf5 = df.to_hdf('all_names.h5', key='df', mode='w')
    df = pd.read_hdf('all_names.h5', 'df')
    
    """ Create df with just one name """
    # Look up specifics for name and year of interest across both genders
    genders = ['M', 'F']
    df_onename = [0, 1]
    df_onename_since = [0, 1]
    for (g, i) in zip(genders, range(len(df_onename))):
        df_onename[i] = df.loc[(df['Name'] == n) & (df['Gender'] == g) ]
        # export_csv = df_onename[i].to_csv ('numOf' + n +'sTable_' + g + '.csv', index = None, header=True) 
        tot_num = df_onename[i]['Quantity'].sum(axis = 0, skipna = True)
    #     # print('Number of '+ g + ' ' + n + "'s born since 1880 =", tot_num)
    #     if ((df['Name'] == n) & (df['Gender'] == g) & (df['Year'] == birth_year)).any():
    #         num_in_birth_year_df = df.loc[(df['Name'] == n) & (df['Gender'] == g) & (df['Year'] == birth_year)]
    #         num_in_birth_year = num_in_birth_year_df.iloc[0]['Quantity']
    #     else:
    #         num_in_birth_year = '< 5'
    #     # print('Number of '+ g + ' ' + n + "'s born in " + str(birth_year) + ' = ' + str(num_in_birth_year))
    #     df_onename_since[i] = df.loc[(df['Name'] == n) & (df['Gender'] == g) & (df['Year'] > birth_year) ]
    #     tot_num_since = df_onename_since[i]['Quantity'].sum(axis = 0, skipna = True)
    #     # print('Number of '+ g + ' ' + n + "'s born since " + str(birth_year) + ' = ' + str(tot_num_since))

    """ Create plot """
    plt.ioff() # this prevents the plots from rendering below

    fig, ax = plt.subplots()
    fontsize = 30
    if not df_onename[0].empty:
        ax = df_onename[0].plot(x = "Year", y = "Quantity", 
                                    figsize=(20,10), fontsize=fontsize, 
                                    legend = False, ax=ax, 
                                    linestyle='-', marker='o', color='blue', label='boys')
    if not df_onename[1].empty:
        df_onename[1].plot(x = "Year", y = "Quantity", 
                                    figsize=(20,10), fontsize=fontsize, 
                                    legend = False, ax=ax, 
                                    linestyle='-', marker='o', color='pink', label='girls')
    ax.minorticks_on()
    ax.legend(fontsize=fontsize*0.75)
    ax.set_title('Quantity of '+ n +"'s per year", fontsize=fontsize)
    ax.set_xlabel("Year", fontsize=fontsize)
    ax.set_ylabel("Number of babies", fontsize=fontsize)

    ax.set_ylim(ymin=0)
    ax.set_xlim(xmin=1880, xmax=2020)

    # # Customize the major grid
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    # # Customize the minor grid
    ax.grid(which='minor', linestyle='--', linewidth='0.5', color='gray')
    
    ax.figure.savefig('static/plot.png', format = "PNG", bbox_inches = 'tight', pad_inches = 0.1)
    
    # # Customize the major grid
    # ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    # # Customize the minor grid
    # ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    # ax.grid('on', which='minor', axis='x' )
    # ax.grid('on', which='major', axis='x' )
    # ax.grid('on', which='minor', axis='y' )
    # ax.grid('on', which='major', axis='y' )



    # print('done')



    return (True)
