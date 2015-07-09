    #Victor Stolle csvToMap.py

from collections import defaultdict
from MapTocsv import CSVGenerator

class MapMaker:

    def __init__(self):
        #map lists for each mod

        self.DTmaps = defaultdict(list)
        self.HRmaps = defaultdict(list)
        self.HDmaps = defaultdict(list)
        self.NMmaps = defaultdict(list)
        self.TBmaps = defaultdict(list)
        self.raw_maps = []

        self.generate_pool()
        self.backup = CSVGenerator(self.raw_maps, 'swiss - Backup.csv', [len(self.DTmaps.items()), len(self.HRmaps.items()), len(self.HDmaps.items()), len(self.NMmaps.items()), len(self.TBmaps.items())])
        self.backup.write()

    def generate_pool(self):
        self.csv = open("swiss.csv", "r")
        next(self.csv)
        for line in self.csv:
            self.split = line.split(",")
            self.raw_maps.append(self.split)
            self.html = ("<tr>\n<td>\n" + self.split[4] + '</td>\n<td>\n<a href="' + self.split[3] + '">' +
                         self.split[1] + "</a>\n</td>\n<td>\n" + self.split[0] + "</td>\n<td>" + self.split[2] +
                         "</td>\n<td>" + self.split[5] + "</td>\n<td>" + self.split[6] + "</td>\n</tr>\n")
            if self.split[4] == 'Double Time':
                self.DTmaps[self.split[7].rstrip('\n')] = [self.split, self.html]
            if self.split[4] == 'Hard Rock':
                self.HRmaps[self.split[7].rstrip('\n')] = [self.split, self.html]
            if self.split[4] == 'Hidden':
                self.HDmaps[self.split[7].rstrip('\n')] = [self.split, self.html]
            if self.split[4] == 'None':
                self.NMmaps[self.split[7].rstrip('\n')] = [self.split, self.html]
            if self.split[4] == 'Tiebreaker':
                self.TBmaps[self.split[7].rstrip('\n')] = [self.split, self.html]

        self.csv.close()

    def getDTmaps(self): return self.DTmaps
    def getHRmaps(self): return self.HRmaps
    def getHDmaps(self): return self.HDmaps
    def getNMmaps(self): return self.NMmaps
    def getTBmaps(self): return self.TBmaps
    def getRaws(self): return self.raw_maps



