class Write(object):	

    def __init__(self, visited_url, file_name):
		#self.url=url
		#self.visited = visited
		self.file_name = file_name
		self.visited_url=visited_url

    def write_links_to_file(self):
		file = open(self.file_name, 'a')					#opens the file to write links in it
		file.writelines(self.visited_url[:] + ["\n"])		#new url that is visited is written in the file with file_name.txt	
