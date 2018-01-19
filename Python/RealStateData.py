#Extracting the house price index data using quandl module
import quandl
import pandas as pd
import pickle

api_key = open("quandlapikey.txt",'r').read()

def state_list():
    fifty_states = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states")
    return fifty_states[0][0][1:]

def state_initial_data():
    states = state_list()
    main_df = pd.DataFrame()


    for stateName in states:
        query = "FMAC/HPI_"+str(stateName)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(stateName)},inplace = True)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    
    print(main_df.head())

#Data pickling i.e storing data in the form of bytes
    pickle_out = open('fifty_states.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()
    

#state_initial_data()

# Data Unpickling
pickle_in = open('fifty_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)
