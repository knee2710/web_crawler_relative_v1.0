import file_soup
import file_extract_links
import make_file
import write_to_file


url = raw_input("give a url you want to scrape:\n> ")		#takes the url as input

unvisited = [url]		#creates a list of unvisited links
visited = ["\n"]		#creates a list of visited links

file = make_file.Create_file(url, "visited_list.txt")		#creates object

file.open_file()											#opens a file, or creates a .txt file in case there is no such file 

stopping_condition = raw_input("after visiting how many pages should the code stop fetching pages?\n> ")		#takes stopping condition from user

while len(unvisited) > 0 and len(visited) <= int(stopping_condition):				#while loop wil continue untill both conditions are true
	data = file_soup.Create_soup(unvisited[0])										#creates object
	(get_soup, visited_url) = data.get_soup_data()									#we get data using BeautifulSoup and store in get_soup			
	unvisited.pop(0)																#pops out the 0th position data
	visited.append(visited_url)														#the poped out data is sent to the list visited
	newely_visited=[visited_url]													#the recently visited url is stored	
	write_data = write_to_file.Write(newely_visited, "visited_list.txt") 			#creates object
	write_data.write_links_to_file()												#writes all the visited urls in the file
	print"this link has been visited:\n", visited_url
	print"No. of unvisited links:", len(unvisited)
	list_of_links = file_extract_links.Extract_links(get_soup, visited, unvisited, url)		#creates object
	unvisited = unvisited + list_of_links.fetch_links()										#updates the unvisited list using object list_of_links
	
print"list of visited links:\n", visited
print"list of unvisited links:\n", unvisited
