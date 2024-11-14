import pandas as pd

#Task2a
url='https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies'

dataFrames=pd.read_html(url)

print(len(dataFrames))

table1=dataFrames[1]

table1.to_csv('Task2_table.csv',index=False)

print(table1)

#Task2b

table_df=pd.read_csv('Task2_table.csv')

print('__________________________________________________________')
release_year=input('Enter the released year to display the details of movies:')
filteed_Data=table_df[table_df['Release year'].astype(str).str.contains(release_year)]

print(f'{release_year} release movies are:')
print(filteed_Data)