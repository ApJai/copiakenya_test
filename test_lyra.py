result =[]
class MovingTotal:
    
    
    def append(self, numbers):
        
        """
        :param numbers: (list) The list of numbers.
        """
        if type(numbers) == list:
            l = numbers
            pass
        else:
            l = list(range(1, numbers+1))                
        range1 = len(l)-2
        total = 0
        a=0
        b=3
        for k in range(range1): 
            for i in l[a:b]:
                total = total+i
            pass
            result.append(total)
            total = 0
            a+=1
            b+=1
        
    

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if total in result:
            return "S"
        else:
            return "no"
        
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    result.clear()
    movingtotal.append(7)
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(18))  