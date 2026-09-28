"""
    Name: Jenny Lee
    Email: Jenny.lee09@myhunter.cuny.edu
    Resources:  w3schools for append()
"""

import textwrap

def extract_overviews(file_name):
    """
        Opens the file_name and from each line of the file, keeps the overview
        description of the school (the fifth "column": overview_paragraph.
        Returns a list of the paragraphs.
    """
    #an empty list for the overviews
    lst = []

    # Open the file_name
    with open(file_name, encoding="utf-8") as md:
        #ignore the first row
        next(md)
        for line in md:
            column = line.split('","') #splits the row based on ","
            overviews = column[4].split('",',1) #splits everything after overview ", one time
            lst.append(overviews[0]) #adds just the overview text to the list

    return lst

def count_lengths(overview_list):
    """
    For each element of the overview_list, the function computes the length 
    (the number of characters in the string). The results are stored in a 
    dictionary of length occurrences where the keys are the lengths seen in 
    overview_list and the values are the number of times each length occurs. 
    Returns the dictionary of length occurrences.
    """
    #dictionary, keys = lengths in list & values = # of times each length occurs
    #ex: 600:2 , length of 600 occurs twice
    counts = {}
    ### map length and count
    # if length once appears, increment the count for that length
    # if it does not appear, set it to 1
    for overview in overview_list:
        length = len(overview) #stores the length of each overview

        if length in counts:
            counts[length] = counts[length]+1
        else:
            counts[length] = 1

    return counts


def const_num_sentences(overview_list):
    """
    For each element of the overview_list, the function computes the number of periods (.) (as a proxy for the number of sentences). The results are stored in a dictionary of occurrences where the keys are the number of periods seen in overview_list and the values are the number of times each occurs. Returns the dictionary of occurrences.
    """


def compute_mean(counts):
    """
    Computes the mean (average) of counts dictionary weighting each key that occurs by its value (e.g. if the key of 10 has value 8, then the 10 showed up 8 times and adds 10*8 to the computation of the average). Returns the mean.
    """

def main():
    ###Test Output for extract_overviews function on Staten Island Schools:
    file_name = '2021_DOE_High_School_Directory_20260925.csv'
    si_overviews = extract_overviews(file_name)
    print(f"Number of SI overviews: {len(si_overviews)}. The the last one is:\n")
    print(textwrap.fill(si_overviews[-1],80))

    #Test output for constant model functions on Staten Island Schools:
    si_len_counts = count_lengths(si_overviews)
    print(f"The {sum(si_len_counts.values())} entries have lengths:")    
    print(si_len_counts)


if __name__ == "__main__":
    main()