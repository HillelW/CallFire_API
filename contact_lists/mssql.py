from dotenv import load_dotenv
import os
from os.path import join, dirname, os
import pyodbc
import itertools


class Connect:
    '''provides a database connection and methods to execute SQL to populate facility names'''
    def __init__(self):        
        # load .env values
        dotenv_path = join(dirname(__file__), '../.env')
        load_dotenv(dotenv_path)

        print(dotenv_path)
        # self.execute_sql() traverses this list to hit each database

        driver = os.getenv("MSSQL_DRIVER")
        server = os.getenv("MSSQL_SERVER")
        username = os.getenv("MSSQL_USERNAME")
        password = os.getenv("MSSQL_PASSWORD")
        database = os.getenv("MSSQL_DATABASE")

        # print(self.server, db, username, password, self.driver, self.database_list)

        connection_string = 'DRIVER={};Server={};UID={};PWD={};DATABASE={}'.format(
            driver, 
            server, 
            username, 
            password,
            database)

        print(driver, server, username, password, database)
        # try:
        self.conn = pyodbc.connect(connection_string)
        # except pyodbc.Error as ex:
        #     sqlstate = ex.args[0]
        #     print("Connection Failed Error Code:" + sqlstate)

    def get_cursor(self):
        '''obtain a cursor to execute SQL'''
        return self.conn.cursor()

    def execute_sp_without_params(self, stored_procedure):
        cursor = self.conn.cursor()
        results = cursor.execute("{CALL " + stored_procedure + "}")
        results_list = [row for row in results]
        return self.grouper(10, results_list)

    def grouper(self, n, iterable, fillvalue=None):
        '''grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx'''
        args = [iter(iterable)] * n
        return list(itertools.zip_longest(*args, fillvalue=fillvalue))