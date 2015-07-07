#Victor Stolle MapGenerator.py

'''
MapGenerator will be a program that will printing and filewriting functions for a pool of maps

'''

from MapPicker import MapPicker



class MapPoolGenerator:

    def __init__(self, week):
        self.mappool = {}        
        self.generate_pool()
        self.MapPicker = MapPicker(week)
        


    def generate_pool(self):
        self.csv = open("swiss.csv", "r")
        
        for line in self.csv:
            self.split = line.split(",")
            self.html = ("<tr>\n<td>\n" + self.split[4] + '</td>\n<td>\n<a href="' + self.split[3] + '">' + self.split[1] + "</a>\n</td>\n<td>\n" + self.split[0] + "</td>\n<td>" + self.split[2] + "</td>\n<td>" + self.split[5] + "</td>\n<td>" + self.split[6] + "</td>\n</tr>\n")
            self.mappool[self.split[1]] = self.html

        self.csv.close()

    def cout(self):
        self.output = open("mappool.html", "w")
        self.output.write("<table>\n<tr>\n<td>Mod</td>\n<td>Title</td>\n<td>Artist</td>\n<td>Difficulty</td>\n<td>Length</td>\n<td>Stars</td>\n</tr>\n")

        #writes the NMmaps
        for i in self.MapPicker.get_NM():
            self.output.write(self.mappool[i])
        #writes the DTmaps
        for i in self.MapPicker.get_DT():
            self.output.write(self.mappool[i])
        #writes the HDmaps
        for i in self.MapPicker.get_HD():
            self.output.write(self.mappool[i])
        #writes the HRmaps
        for i in self.MapPicker.get_HR():
            self.output.write(self.mappool[i])
        #writes the TieBreaker
        self.output.write(self.mappool[self.MapPicker.get_TB()])
        
        self.output.write("</table>\n")
        self.output.close()


    def run(self):

        #print("Running Randomizer...")
        self.MapPicker.run_randomizer()
        #print("Randomizer Finished. Writing values to mappool.html...")
        self.cout()
        #print("Writing Finished. Printing maps to console...")
        self.MapPicker.print_maps()
        #print("Done.")
    
