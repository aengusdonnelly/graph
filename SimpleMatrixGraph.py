import numpy as np

class Graph:
    '''Klass som inför grafnätverk.'''

    def __init__(self):     
        '''Metod som initierar grafen.'''
        self.matrix = None
        self.values = []
        self.size_ = 0

    def add_vertex(self, value):
        '''Metod som lägger till ett hörn med datan "value" i grafen. Retunerar "None".'''
        if value in self.values:
            pass
        elif self.size_ == 0:
            self.matrix = np.array([[0]])
            self.values.append(value)
            self.size_ += 1
        else:
            self.matrix = np.hstack((self.matrix, np.array([[0]]*self.size_)))
            self.matrix = np.vstack((self.matrix, np.array([[0]*(self.size_+1)])))
            self.values.append(value)
            self.size_ += 1
        return None

    def add_edge(self, value1, value2):
        '''Metod som sammankopplar två hörn: från hörnet med datan
        "value1" till hörnet med datan "value2" med en kant. Retunerar
        "None".'''
        if value1 not in self.values or value2 not in self.values:
            pass
        else:
            idx1 = self.values.index(value1)
            idx2 = self.values.index(value2)
            if idx1 == idx2:
                pass
            else:
                self.matrix[idx1][idx2] = 1
                self.matrix[idx2][idx1] = 1
        return None

    def remove_vertex(self, value):
        '''Metod som tar bort ett hörn med datan "value". Alla kanter till
        och från hörnet försvinner därmed också. Retunerar "None".'''
        if value not in self.values:
            pass
        elif self.size_ == 1:
            self.matrix = None
            self.values = []
            self.size_ = 0
        else:
            idx = self.values.index(value)
            self.matrix = np.delete(self.matrix, idx, axis=0)
            self.matrix = np.delete(self.matrix, idx, axis=1)
            self.values.pop(idx)
            self.size_ -= 1
        return None

    def remove_edge(self, value1, value2):
        '''Metod som tar bort en kant mellan två hörn: från hörnet med
        datan "value1" till hörnet med datan "value2". Retunerar
        "None".'''
        if value1 not in self.values or value2 not in self.values:
            pass
        else:
            idx1 = self.values.index(value1)
            idx2 = self.values.index(value2)
            if idx1 == idx2:
                pass
            else:
                self.matrix[idx1][idx2] = 0
                self.matrix[idx2][idx1] = 0
        return None

    def clear(self):
        '''Metod som tar bort samtliga hörn och kanter i grafen.
        Retunerar "None".'''
        self.matrix = None
        self.values = []
        self.size_ = 0
        return None

    def get_vertices(self):
        '''Metod som retunerar en tuple med alla hörn i grafen (osorterad,
        eftersom det inte nädvändigtvis beföver finnas samma datatyper i
        alla hörn).'''
        return(set(self.values))

    def get_edges(self):
        '''Metod som retunerar en tuple med alla kanter i grafen
        (osorterad, eftersom det inte nädvändigtvis beföver finnas samma
        datatyper i alla hörn) i formen av tupler.'''
        edges = []
        for i in range(0, self.size_):
            for j in range(0, self.size_):
                vali = self.values[i]
                valj = self.values[j]
                if self.matrix[i][j] == 0:
                    pass
                elif (vali, valj) in edges or (valj, vali) in edges:
                    pass
                else:
                    edges.append((vali, valj))
        return set(edges)

    def get_neighbours(self, value):
        '''Metod som retunerar grannarna till hörnet med datan "value" i
        en tuple (osorterad, eftersom det inte nädvändigtvis beföver
        finnas samma datatyper i alla hörn).'''
        if value not in self.values:
            pass
        else:
            neighbours =  []
            idx = self.values.index(value)
            for i in range(0, self.size_):
                if self.matrix[idx][i] != 0:
                    neighbours.append(self.values[i])
        return set(neighbours)

    def get_degree(self, value):
        '''Retunerar graden av hörnet med datan "value".'''
        if value not in self.values:
            pass
        else:
            degree = 0
            idx = self.values.index(value)
            for i in range(0, self.size_):
                if self.matrix[idx][i] != 0:
                    degree += 1
        return degree

    def get_distance(self, value1, value2):
        '''Undersöker storleken på det kortaste avståndet mellan två hörn
        med datan "value1" och "value2". Retunerar värdet som ett heltal
        av hur många kanter som korsas. Om ingen väg finns retuneras
        "None".'''
        if value1 not in self.values or value2 not in self.values:
            return None
        elif self.exist_path(value1, value2) == False:
            return None
        elif value1 == value2:
            return 0
        else:
            idx1 = self.values.index(value1)
            idx2 = self.values.index(value2)
            distance = 1
            d_matirx = self.matrix
            while d_matirx[idx1][idx2] == 0:
                d_matirx = np.matmul(d_matirx, self.matrix)
                distance += 1
            return distance

    def exist_vertex(self, value):
        '''Kollar om ett visst hörn med datan "value" finns i grafen.
        Retunerar "True" i sånna fall, annars "False".'''
        if value in self.values:
            return True
        else:
            return False

    def exist_edge(self, value1, value2):
        '''Kollar om en kant mellan hörnen med ddatan "value1" och
        "value2" finns i grafen. Retunerar "True" i sånna fall, annars
        "False".'''
        if value1 not in self.values or value2 not in self.values:
            pass
        else:
            idx1 = self.values.index(value1)
            idx2 = self.values.index(value2)
            if self.matrix[idx1][idx2] == 0:
                pass
            else:
                return True
        return False

    def e_p(self, vertex, target, memo):
        '''Rekursiv hjälpmetod för metoden "exist_path".'''
        if vertex in memo:
            pass
        elif vertex == target:
            return True
        else:
            memo.append(vertex)
            neis = self.get_neighbours(vertex)
            for nei in neis:
                result = self.e_p(nei, target, memo)
                if result == True:
                    return True
        return False

    def exist_path(self, value1, value2):
        '''Kollar om det finns en eller flera vägar mellan två hörn med
        datan "value1" och "value2". Retunerar "True" i sånna fall, annars
        "False".'''
        if value1 not in self.values or value2 not in self.values:
            return False
        elif value1 == value2:
            return True
        else:
            result = self.e_p(value1, value2, [])
            return result
            
    def size(self):
        '''Metod som retunerar antalet hörn i grafen.'''
        return self.size_