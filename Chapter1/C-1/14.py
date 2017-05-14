def odds_multiple(data):
    numOfOdds = 0
    for num in data:
        if num % 2 == 1:
            numOfOdds += 1
        
        '''
        The multiple of two odds is odd. 
        For that reason,  we only have to search 
        for two odds in the list.
        '''
        if numOfOdds == 2:
            return True

    return False
