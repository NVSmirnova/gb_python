from abc import ABC, abstractmethod
class Clother(ABC):
    @abstractmethod
    def __init__(self):
        pass
    #    self.size = size
    @property
    def total_tissue(self):
        pass

    def tot_tot_tissue(self):
        pass

class Coat(Clother):
    def __init__(self, size):
        self.size = size

    @property
    def total_tissue(self):
        return self.size / 6.5 + 0.5

    def tot_tot_tissue(self):
        return self.total_tissue + i.total_tissue

class Suite(Clother):
    def __init__(self, height):
        self.height = height

    @property
    def total_tissue(self):
       return 2 * self.height + 0.3

    def tot_tot_tissue(self):
        return self.total_tissue + i.total_tissue


polto = Coat(65)
print(polto.total_tissue)
#print(polto.tot_tot_tissue())
kostum = Suite(170)
print(kostum.total_tissue)
print(polto.total_tissue + kostum.total_tissue)