from random import randrange

#random generator

class MapPicker:

    def __init__(self, week):

        self.param = 30 - (week - 1) * 3
        self.TBparam = self.param * 4 + 10 - (week - 1)

        self.mapmaker = MapMaker()

        self.DT = [i for i in range(0, self.param)] #Double Time map pool
        self.HR = [i for i in range(self.param, self.param*2)]#No Mod map pool
        self.HD = [i for i in range(self.param*2, self.param*3)]#Hidden map pool
        self.NM = [i for i in range(self.param*3, self.param*4)]#Hard Rock map pool
        self.TB = [i for i in range(self.param*4, self.TBparam)]#Tiebreaker map pool
        
        self.DTmaps = []
        self.NMmaps = []
        self.HDmaps = []
        self.HRmaps = []
        self.TBmap = None
        self.maps = []
        self.set_maps()

    def create_list(self):
        #creates a list of maps
        self.searchfile = open("List of Maps.txt", "r")
        for line in self.searchfile:
            self.maps.append(line.rstrip("\n"))
        self.searchfile.close()
	
        
    def random_search(self, pool):
        # pops the 3 map #s from the pool
        self.map1 = pool.pop(randrange(0, len(pool)))
        self.map2 = pool.pop(randrange(0, len(pool)))
        self.map3 = pool.pop(randrange(0, len(pool)))
        
        return [self.maps[self.map1], self.maps[self.map2], self.maps[self.map3]]

    def run_randomizer(self):
        self.set_DT()
        self.set_NM()
        self.set_HD()
        self.set_HR()
        self.set_TB()
            
    def get_maps(self): return self.maps
    def set_maps(self): self.create_list()
    def get_DT(self): return self.DTmaps
    def set_DT(self): self.DTmaps = self.random_search(self.DT)
    def get_NM(self): return self.NMmaps
    def set_NM(self): self.NMmaps = self.random_search(self.NM)
    def get_HD(self): return self.HDmaps
    def set_HD(self): self.HDmaps = self.random_search(self.HD)
    def get_HR(self): return self.HRmaps
    def set_HR(self): self.HRmaps = self.random_search(self.HR)
    def get_TB(self): return self.TBmap
    def set_TB(self): self.TBmap = self.maps[self.TB.pop(randrange(0, len(self.TB))) - 1]
        
    def print_maps(self):

        print("No Mod: \nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.NMmaps[0], self.NMmaps[1], self.NMmaps[2]))
        print("Double Time:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.DTmaps[0], self.DTmaps[1], self.DTmaps[2]))
        print("Hidden:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.HDmaps[0], self.HDmaps[1], self.HDmaps[2]))
        print("Hard Rock:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.HRmaps[0], self.HRmaps[1], self.HRmaps[2]))
        print("And tiebreaker is: {}".format(self.TBmap))
