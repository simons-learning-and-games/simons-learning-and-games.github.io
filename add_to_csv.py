import pandas as pd
import os

fname = input("Choose schedule to append to: (seminar/reading-group-1/reading-group-2) :")
date = input("Date in format dd/mm/yyyy : ")
time = input("Time of the talk in format HH:MM : ")
speaker = input("Name and Surname of the speaker: ")
affiliation = input("Affiliation of the speaker: ")
url = input("Homepage of the speaker: ")
title = input("Title of the talk: ")
abstract = input("Abstract of the talk: ")
bio = input("Short bio of the speaker: ")
related = input("Papers connected to the talk (List all titles separated by semicolon(;) :")
location = input("Location of the talk: ")
imgfile = input("Name of the image file you added to the img folder with a portrat of the speaker :")
zoom = input("Zoom link of the talk: ")




print(row)
ans = input("Make sure all previous info is correct. Should it be appended to the csv file? [y/n]:")
if ans == 'y':
    fname = os.path.join('csv', fname+'.csv')
    df = pd.read_csv(fname)
    df = df.append(row, ignore_index = True)
    print(df)
    df.to_csv(fname, index=False, )
else:
    pass
