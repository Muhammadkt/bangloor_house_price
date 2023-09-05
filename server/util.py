# import json
# import pickle
# import numpy as np
# __locations =None
# __data_columns=None
# __model=None


# def load_saved_artifacts():
#     print("loading saved artifacts....start")
#     global __data_columns
#     global __locations

#     # with open("C:/Users/Hp/Desktop/DSprojects/2.House_price/BHP/server/artifacts/columns.json",'r') as f:
#     #     __data_columns=json.load(f)['data_colums']
#     #     __locations = __data_columns[3:]
#     try:
#      with open("C:/Users/Hp/Desktop/DSprojects/2.House_price/BHP/server/artifacts/columns.json", 'r') as f:
#         __data_columns = json.load(f)['data_colums']
#         __locations = __data_columns[3:]
#     except Exception as e:
#      print(f"Error loading data columns: {str(e)}")

#     global __model
#     with open("C:/Users/Hp/Desktop/DSprojects/2.House_price/BHP/server/artifacts/banglore_home_price_model.pickle",'rb') as f:
#         __model=pickle.load(f)
#     print("loading saved artifacts...done")     
#     return __locations


# def get_estimated_price(location,sqft,bhk,bath):
#     load_saved_artifacts()
#     try:
#         loc_index=__data_columns.index(location.lower())
#     except:
#         loc_index=-1
#     X=np.zeros(len(__data_columns))
#     X[0]=sqft
#     X[1]=bath
#     X[2]=bhk
#     if loc_index >=0:
#         X[loc_index]=1
#     return round(__model.predict([X])[0],2) 

# def get_location_names():
#     print("_________________________________________________________________________")
#     print(__locations)
#     return __locations


# if __name__=='__main__':
#      load_saved_artifacts()
#      print(get_location_names())
# #     print(get_estimated_price('1st block jayanagar',1000,3,3))
# #     print(get_estimated_price('1st block jayanagar',1000,2,2))
# #     print(get_estimated_price('banaswadi',1000,2,2))
# #     print(get_estimated_price('ambalipura',1000,2,2))


import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    try:
        with open("C:/Users/Hp/Desktop/DSprojects/2.House_price/BHP/server/artifacts/columns.json", "r") as f:
         __data_columns = json.load(f)['data_colums']
         __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    except Exception as e:
        print(f"Error loading data column:{str(e)}")    

    global __model
    if __model is None:
        try:
            with open('C:/Users/Hp/Desktop/DSprojects/2.House_price/BHP/server/artifacts/banglore_home_price_model.pickle', 'rb') as f:
             __model = pickle.load(f)
        except Exception as e:
            print(f"model_load_error:{str(e)}")     
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location