def hasSingleCycle(array):
    # Write your code here.
    bitmap = [False] * len(array)
    index = 0
    while True :
        if (bitmap[index] is True) :
            for bool in bitmap :
                if bool is False :
                    return False
            return True
        bitmap[index] = True
        index += array[index]
        while (index < 0) :
            index = len(array - index)
        while (index >= len(array)) :
            index -= len(array) 


