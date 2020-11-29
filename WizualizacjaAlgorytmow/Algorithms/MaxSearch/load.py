from Algorithms.BasicAlgorithm import BasicAlgorithm

class MaxSearch(BasicAlgorithm):
    """
    Klasa reprezentująca algorytm wyszukiwania maximum w tablicy

    Przykład:
    >>> max_search = MaxSearch()
    """
    def __init__(self):
        super().__init__("MaxSearch", "Wyszukiwanie wartosci maksymalnej")
                
    def execute(self):
        """
        Metoda uruchamiająca algorytm.
        """
        current_max=self.data[0]
        current_max_index=0
        self.save_snapshot("Na początek ustalamy majwiększy element na pierwszą wartosć z tablicy (%i)" %current_max,{0:'g'})
        for i in range(1,len(self.data)):
            self.save_snapshot("Porównujemy %i element o wartoci %i z tablicy z aktualnym maksimum (%i)" %(i,self.data[i],current_max),{current_max_index:'g', i:'r'})
            if(self.data[i]>current_max):
                self.save_snapshot("%i jest większe od %i, więc zapamiętujemy nową wartosć maksymalną" %(self.data[i],current_max),{i:'g',current_max_index:'r'})
                current_max=self.data[i]
                current_max_index=i
            else:
                self.save_snapshot("%i nie jest większe od %i, więc przechodzimy dalej" %(self.data[i],current_max),{current_max_index:'g',i:'r'})
        self.save_snapshot("Znaleziona wartosć maksymalna wynosi %i" %current_max,{current_max_index:'y'})
        

def __init__():
    return MaxSearch()
                  