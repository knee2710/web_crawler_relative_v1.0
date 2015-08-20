class Create_file(object):						

    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name


    def open_file(self):
        with open(self.file_name, 'a') as file:												#opens the ammendable('a') file with name "file_name"
            file.write("\nfor " + self.url + " :\n" + "\n" + self.file_name + ":\n")		#writes 1st two lines in the file describing about the link
