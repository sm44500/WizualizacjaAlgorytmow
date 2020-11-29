from Algorithms.BasicAlgorithm import BasicAlgorithm

class MinSearch(BasicAlgorithm):
    """
    Klasa reprezentująca algorytm wyszukiwania minimum w tablicy
    
    Przykład:
    >>> min_search = MinSearch()
    """
    def __init__(self):
        super().__init__("MinSearch", "Wyszukiwanie wartosci minimalnej")
                
    def execute(self):
        """
        Metoda uruchamiająca algorytm.
        """
        current_min=self.data[0]
        current_min_index=0
        self.save_snapshot("Na początek ustalamy najmniejszy element na pierwszą wartosć z tablicy (%i)" %current_min,{0:'g'})
        for i in range(1,len(self.data)):
            self.save_snapshot("Porównujemy %i element o wartoci %i z tablicy z aktualnym minimum (%i)" %(i,self.data[i],current_min),{current_min_index:'g', i:'r'})
            if(self.data[i]<current_min):
                self.save_snapshot("%i jest mniejsze od %i, więc zapamiętujemy nową wartosć minimalną" %(self.data[i],current_min),{i:'g',current_min_index:'r'})
                current_min=self.data[i]
                current_min_index=i
            else:
                self.save_snapshot("%i nie jest mniejsze od %i, więc przechodzimy dalej" %(self.data[i],current_min),{current_min_index:'g',i:'r'})
        self.save_snapshot("Znaleziona wartosć minimalna wynosi %i" %current_min,{current_min_index:'y'})
        

def __init__():
    return MinSearch()
                  