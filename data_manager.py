import requests
import os 
import dotenv

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.load = dotenv.load_dotenv()
        os.getenv(key="END_POINT")

        