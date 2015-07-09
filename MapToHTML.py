#Victor Stolle MapGenerator.py

'''
MapGenerator will be a program that will printing and filewriting functions for a pool of maps

'''

from MapPicker import MapPicker



class HTMLGenerator:

    def __init__(self):

        self.MapPicker = MapPicker()


    def cout(self):
        self.output = open("mappool.html", "w")
        self.output.write("<table>\n<tr>\n<td>Mod</td>\n<td>Title</td>\n<td>Artist</td>\n<td>Difficulty</td>\n<td>Length</td>\n<td>Stars</td>\n</tr>\n")

        #writes the NMmaps
        for i in self.MapPicker.get_NM():
            self.output.write(i[1])
        #writes the DTmaps
        for i in self.MapPicker.get_DT():
            self.output.write(i[1])
        #writes the HDmaps
        for i in self.MapPicker.get_HD():
            self.output.write(i[1])
        #writes the HRmaps
        for i in self.MapPicker.get_HR():
            self.output.write(i[1])
        #writes the TieBreaker
        self.output.write(self.MapPicker.get_TB()[1])
        
        self.output.write("</table>\n")
        self.output.close()


    def run(self):

        #print("Randomizer Finished. Writing values to mappool.html...")
        self.cout()
        #print("Writing Finished. Printing maps to console...")
        self.MapPicker.print_maps()
        #print("Done.")

    def get_maps(self): return self.MapPicker.get_maps()
    def get_sizes(self): return self.MapPicker.get_sizes()


if __name__ == "__main__":

    h = HTMLGenerator()
    h.run()
