#Victor Stolle MapPicker.py
from random import randrange
from csvToMap import MapMaker

#random generator
class MapPicker:

    def __init__(self):

        self.mapmaker = MapMaker()
        '''
        Mapmaker object: defaultdict(list)
        DTmap[num ( 0 -> self.param )] = [[Artist, Title, Difficulty, Link, Mod, Length, Star, Song No.], html]
        '''        
        self.DT = [i for i in range(0, len(self.mapmaker.getDTmaps().items()))]#Double Time map pool
        self.HR = [i for i in range(0, len(self.mapmaker.getHRmaps().items()))]#No Mod map pool
        self.HD = [i for i in range(0, len(self.mapmaker.getHDmaps().items()))]#Hidden map pool
        self.NM = [i for i in range(0, len(self.mapmaker.getNMmaps().items()))]#Hard Rock map pool
        self.TB = [i for i in range(0, len(self.mapmaker.getTBmaps().items()))]#Tiebreaker map pool
        
        self.DTmaps = []
        self.NMmaps = []
        self.HDmaps = []
        self.HRmaps = []
        self.TBmap = None
        self.revisedRaws = self.mapmaker.getRaws()

        self.map1 = 0
        self.map2 = 0
        self.map3 = 0
        
        
        self.run_randomizer()

        self.sizes = [len(self.DT), len(self.HR), len(self.HD), len(self.NM), len(self.TB)]
        
        
    def random_search(self, pool):
        # finds the 3 map #s from the pool
        self.map1 = pool.pop(randrange(0, len(pool)))
        self.map2 = pool.pop(randrange(0, len(pool)))
        self.map3 = pool.pop(randrange(0, len(pool)))

        return [self.map1, self.map2, self.map3]

    def run_randomizer(self):
        self.set_DT()
        self.set_NM()
        self.set_HD()
        self.set_HR()
        self.set_TB()
        self.remove_raws()
        
    def get_sizes(self): return self.sizes
    def get_maps(self): return self.revisedRaws
    def get_DT(self): return self.DTmaps
    def set_DT(self):
        for i in self.random_search(self.DT):
            self.DTmaps.append(self.mapmaker.getDTmaps()[str(i)])
        
    def get_NM(self): return self.NMmaps
    def set_NM(self):
        for i in self.random_search(self.NM):
            self.NMmaps.append(self.mapmaker.getNMmaps()[str(i)])
        
    def get_HD(self): return self.HDmaps
    def set_HD(self):   
        for i in self.random_search(self.HD):
            self.HDmaps.append(self.mapmaker.getHDmaps()[str(i)])

    def get_HR(self): return self.HRmaps
    def set_HR(self):
        for i in self.random_search(self.HR):
            self.HRmaps.append(self.mapmaker.getHRmaps()[str(i)])

    def get_TB(self): return self.TBmap
    def set_TB(self):
        self.TBmap = self.mapmaker.getTBmaps()[str(randrange(0, len(self.TB)))]

    def remove_raws(self):
        #remove the maps from the mods from our pool of raws

        for i in self.get_DT():
            del self.revisedRaws[self.revisedRaws.index(i[0])]
            
        for i in self.get_HR():
            del self.revisedRaws[self.revisedRaws.index(i[0])]

        for i in self.get_HD():
            del self.revisedRaws[self.revisedRaws.index(i[0])]
                                 
        for i in self.get_NM():
            del self.revisedRaws[self.revisedRaws.index(i[0])]


        self.revisedRaws.remove(self.get_TB()[0])
    
        
    
        
    def print_maps(self):

        print("No Mod: \nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.NMmaps[0][0][1], self.NMmaps[1][0][1], self.NMmaps[2][0][1]))
        print("Double Time:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.DTmaps[0][0][1], self.DTmaps[1][0][1], self.DTmaps[2][0][1]))
        print("Hidden:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.HDmaps[0][0][1], self.HDmaps[1][0][1], self.HDmaps[2][0][1]))
        print("Hard Rock:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.HRmaps[0][0][1], self.HRmaps[1][0][1], self.HRmaps[2][0][1]))
        print("And tiebreaker is: {}".format(self.TBmap[0][1]))

