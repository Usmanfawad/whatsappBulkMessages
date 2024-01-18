import json
import requests
import os
import pandas as pd
import xlrd


class UltraMessage():
    def __init__(self):
        data = pd.read_excel('contacts.xlsx')
        self.data_to_lst = data.values.tolist()
        self.send_response()

    def send_response(self):
        url = "https://api.ultramsg.com/instance53326/messages/chat"

        for each_number in self.data_to_lst:
            message = f"Hi {each_number[0]} \nThis is Usman, looking for {each_number[1]} and let me know if you are interested to work on this."
            payload = f"token=p25i2oy53uwkyte4&to=+923352839515&body={message}"
            payload = payload.encode('utf8').decode('iso-8859-1')
            headers = {'content-type': 'application/x-www-form-urlencoded'}

            response = requests.request("POST", url, data=payload, headers=headers)






if __name__ == "__main__" :
    UltraMessage()