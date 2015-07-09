#Victor Stolle MapTocsv.py
import csv

class CSVGenerator:



    def __init__(self, maps, path, sizes = None):
        self.maps = maps
        self.path = path
        self.sizes = sizes # sizes are [len(DT), len(HR), len(HD), len(NM), len(TB)
            
    
    def write(self):
        #csv write 
        with open(self.path, "wb") as csv_file:
            self.writer = csv.writer(csv_file, delimiter=',')
            self.writer.writerow(['Artist', 'Title', 'Difficulty', 'Link', 'Mod', 'Length', 'Star', 'Song No.'])
            if self.sizes == None:
                for line in self.maps:
                    self.writer.writerow(line)
            else:
                for i in range(self.sizes[0]):
                    self.line = self.maps[i] #file line
                    self.line[-1] = i
                    self.writer.writerow(self.line)


                for i in range(self.sizes[1]):
                    self.line = self.maps[i]
                    self.line[-1] = i
                    self.writer.writerow(self.line)

                for i in range(self.sizes[2]):
                    self.line = self.maps[i] #file line
                    self.line[-1] = i
                    self.writer.writerow(self.line)


                for i in range(self.sizes[3]):
                    self.line = self.maps[i] #file line
                    self.line[-1] = i
                    self.writer.writerow(self.line)


                for i in range(self.sizes[4]):
                    self.line = self.maps[i] #file line
                    self.line[-1] = i
                    self.writer.writerow(self.line)

