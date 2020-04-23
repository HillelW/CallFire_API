from dotenv import load_dotenv
import os
from os.path import join, dirname, os
import requests
from callfire.client import CallfireClient


class ConnectCallfire:
    '''Connect to the callfire API to update contact lists'''
    def __init__(self):
        # load environment values from .env
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)

        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        # base_api_url = os.getenv("API_BASE_URL")

        self.client = CallfireClient(username, password)

    def create_new_contact_list(self, file_path, name):
        '''given a file path and a name, associates the data in that file with that name'''
        response = self.client.contacts.createContactListFromFile(name='{}'.format(name), file=open('{}'.format(file_path)).result())
        return response

    def delete_contact_list(self, name):
        self.client.contacts.deleteContactList(name=name).result()