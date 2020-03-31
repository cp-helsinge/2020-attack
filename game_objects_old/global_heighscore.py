"""============================================================================
  Global heighscore

  Access external key value store 

  By Simon Rigét @Paragi 2020

============================================================================"""
import requests
import json

class GlobalHeighscore:
    def __init__(self, key):
        self.url = 'https://paragi.dk/api/heighscore.php'
        # Set service id to access key value store
        self.service_id = 'KDCTY9560F3E3563A6SERWERWEW875EVYVRI'
        # Set key, unique to this game
        self.key = key
        self.list = {}
        self.get()
        
    def get(self):
        response = requests.post(self.url, { 'service': self.service_id, 'key': self.key })
        self.process_response(response)
        return self.list

    def set(self, name, score):    
        post = {
            'service': self.service_id,
            'key': self.key,
            'value': json.dumps({'name':name, 'score':score}),
        }

        response = requests.post(self.url, post)
        self.process_response(response)
        return self.list

    def process_response(self, response):
        if response.status_code == 200:
            self.list = response.json()
            #self.list.sort(key=lambda operator: operator['score'] , reverse = True)
        elif response.status_code == 404:
            raise Exception('No global heighscore service at ',self.url)
        else:
            raise Exception('Global heighscore service is off-line')


