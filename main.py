# import packages
from fastapi import FastAPI,HTTPException,Header
from pydantic import BaseModel
import pandas as pd

# create FastAPI object
app = FastAPI()

#password
password="kopinikmatnyamandilambung2000"

class Profile(BaseModel):
    '''
    Profile class - used for making request body
    '''
    name: str
    location: str


@app.get('/')
def getHome():
    '''
    endpoint 1 - home page
    '''

    return {
        "msg": "Hello world hiya hiya hiya"
    }


@app.get('/profiles')
def getProfiles():
    # membaca isi CSV
    df = pd.read_csv('dataset.csv')
    return {
        "data":df.to_dict(orient='records')
    }  
    '''
    endpoint 2 - get all profiles
    '''
#url/path parameter
@app.get('/profiles/{id}')
def getProfile(id: int):
    #membaca datasource
    df = pd.read_csv('dataset.csv')

    #memfilter data sesuai ID
    result = df.query(F"id=={id}")
    #ketika result kosong ->data kosong
    if len(result)==0:
        #tampilkan pesan eror ->raise
        raise HTTPException(status_code=404,detail="data not found!" \
        "")


    return {
        "data":result.to_dict(orient='records')
    }
    '''
    endpoint 3 - get profile by id
    '''

    # complete this endpoint
    


@app.delete('/profiles/{id}')
def deleteProfile(id: int, api_key:str=Header(None)):
    if (api_key ==None) or (api_key!=password):
        raise HTTPException(status_code=401,detail="Unauthorized Access!")
    
    df = pd.read_csv('dataset.csv')

    result = df[df.id != id]
    
    #replace data dengan data yang baru
    result.to_csv('dataset.csv',index=False)
  
    return {
        "data":result.to_dict(orient='records')
    } 

    ''' 
    endpoint 4 - delete profile by id
    '''

    # complete this endpoint
    


@app.put('/profiles/{id}')
def updateProfile(id: int, profile: Profile):
    '''
    endpoint 4 - update profile by id
    '''

    # complete this endpoint
    pass


@app.post('/profiles/')
def createProfile(profile: Profile):
    '''
    endpoint 6 - create new profile

    '''

    # membaca isi datasource
    df = pd.read_csv('dataset.csv')
    # buat databaru
    NewDf = pd.DataFrame({
        "id": [len(df) + 1],
        "name": [profile.name],
        "location": [profile.location]
    })
    # concat- gabung 2 dataframe yang berbeda menjadi 1
    df= pd.concat([df,NewDf])

    df.to_csv('dataset.csv', index=False)

    return{
        "msg": "data has created succesfully"
    }

