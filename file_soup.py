from bs4 import BeautifulSoup
import requests


class Create_soup(object):

    def __init__(self, url):
        self.url = url

    def get_soup_data(self):
        source_code = requests.get(self.url)			#use of requests module to access url  
        data = source_code.text							#from source code we take the data
        soup = BeautifulSoup(data, "html.parser")		#the data taken is not usefull, will use BeautifulSoup to make it usefull		
        return soup, self.url							#return soup data and the url

