# check if string has some letters

class String:
    def __init__(self,string):
        self.string = string
    def check_letter(self,lettr):
            if lettr in self.string:
                return True
            else:
                return False
    def count(self,lettr):
        count = 0
        for l in self.string:
            if l is lettr:
                count +=1
        return count
    def frequency(self):
        count = 0
        freq = {}
        print(freq)
        for i in self.string:
            for j in self.string:
                if i is j:
                    count +=1
                    freq[i] = count
            count = 0
        
        return freq
                    
    

le = String("Can you offer me a plate of rice served with tear?")
h = le.frequency()

print(h)