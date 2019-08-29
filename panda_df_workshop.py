import pandas as pd


# %% read file into a df
df= pd.read_csv("data/titles.csv")


#%% print sample head and tail

print(df.head(5))
print(df.tail(5))
# %% how many movies are listed in the titles df?
print(len(df))

# %% what are the earliest two films listed in the df?

print(df.sort_values('year').head(2))

#%% how many movies have the title "Hamlet"?
print(df[df.title=="Hamlet"].sort_values('year'))
print(len(df[df.title=="Hamlet"]))

#%% how many movies were made in the year 1950?
print(len(df[df.year==1950]))


#%% how many movies were made from 1950 through 1959?
print(len(df[(df.year>=1950) & (df.year<=1959)]))
print(len(df[df.year//10 == 195]))

#%% what are the ten most common movies names of all time?
print(df.title.value_counts().head(10))

#%% plot the number of films that have been released each decade
#over the history of cinema.
(df.year//10*10).value_counts().sort_index().plot(kind="bar")

#%% plot the number of hamlet movie made each decade
h= df[df.title=="Hamlet"]
(h.year//10*10).value_counts().sort_index().plot(kind="bar")


