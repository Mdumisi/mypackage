def top_n (items, n):
    """Return the top n items in an array, in desc order.

    Args:
        items (array): list of array-like object 
        n (int): num of items to return

    Return:
        array: top n items, in desc order

    Egs:
      >>> top_n([8,3,2,7,4], 3) 
      [8,7,3]
    """
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]: # if this items is bigger than next item..
                item[j], item[j+1] = item[j] # swap the two!

# get last two items
top_n = item[-n:]

# return in descending order
return top_n[::-1]