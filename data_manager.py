import requests
import os 
import dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, url):
        self.url = url

    def get_data(self) -> dict:
        '''
            This function is responsilble to get data and return that data
        '''
        response = requests.get(url=self.url)
        response.raise_for_status()
        data = response.json()
        return data['prices']
    
    def put_data(self,body: dict, id: int):

        '''
            This function is responsible to put data to sheety and update.
        '''
        body = {
            "price": body
        }
        shitty_post = requests.put(url=f"{self.url}/{id}", json=body)
        shitty_post.raise_for_status()
        return shitty_post.text