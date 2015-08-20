from bs4 import BeautifulSoup
import urlparse
import requests

class Extract_links(object):

    unvisited_for_current_link=[]				#this list is used to store all the unvisited links in this class then will be merged with main unvisited list
    def __init__(self,get_soup, visited, old_unvisited_links, url):		
		self.get_soup = get_soup
		self.visited = visited
		self.url = url
		self.old_unvisited_links = old_unvisited_links

    def fetch_links(self):
        for link in self.get_soup.find_all("a"):					#looks for links with <a> in that link 
            new_tag=urlparse.urljoin(self.url,link.get("href"))		#link.get() is used to take the href info of the link and then url join is used to join it to the prefix of the "url" in case it don't have it
            if self.url in new_tag and new_tag not in self.visited:
				link=[new_tag]											#makes the new_tag a list called link
				if new_tag not in self.unvisited_for_current_link and new_tag not in self.old_unvisited_links: 		#this condition avoids repetitions
					self.unvisited_for_current_link = self.unvisited_for_current_link + link						# to merge all the unvisited links together
        return self.unvisited_for_current_link
