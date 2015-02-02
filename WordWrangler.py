"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    
    ans=[]
    if list1!=[]:
        ind=0
        length=len(list1)
        while(ind<length-1):
            if list1[ind]!=list1[ind+1]:
                ans.append(list1[ind])
            ind+=1
        ans.append(list1[length-1])
    return ans


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    ans=[]
    len1=len(list1)
    len2=len(list2)
    if len1<len2:
        lst=list(list1)
        ano=list(list2)
    else:
        lst=list(list2)
        ano=list(list1)
    for itm in lst:
        if itm in ano:
           ans.append(itm) 
    return ans

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    ans=[]
    len1=len(list1)
    len2=len(list2)
    if len1>len2:
        lst=list(list1)
        ano=list(list2)
    else:
        lst=list(list2)
        ano=list(list1)
    for itm in lst:
        while ano and (ano[0]<itm):
            ans.append(ano[0])
            ano.pop(0)
        ans.append(itm)
    ans.extend(ano)
    return ans
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    leng=len(list1)
    if leng>1:
        mid=leng/2
        left=list1[0:mid]
        right=list1[mid:leng]
        left=merge_sort(left)
        right=merge_sort(right)
        return merge(left,right)
    else:
        return list1

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if word=="":
        return [""]
    ans=[]
    leng=len(word)
    print leng
    if leng==1:
        ans.append("")
        ans.append(word)
        return ans
    first=word[0]
    print first
    rest=word[1:leng]
    print rest
    rest_strings=gen_all_strings(rest)
    print rest_strings
    for wrd in rest_strings:
        if wrd==" ":
            ans.append(first)
        else:
            for num in range(len(wrd)+1):
                print "wrd=",wrd
                exa=list(wrd)
                print "exa=", exa
                print num
                exa.insert(num,first)
                con=''.join(exa)
                ans.append(con)
                print "ans=",ans
    return rest_strings+ans

# Function to load words from a file