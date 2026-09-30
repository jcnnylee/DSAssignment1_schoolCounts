"""
    Name: Jenny Lee
    Email: Jenny.lee09@myhunter.cuny.edu
    Resources: Used w3schools for append() function.
    Used GeeksforGeeks as a reminder of how to do incrementation/decrementation in Python ,
    how to iterate key-value pairs , finding the average of a list 
    (using either statistics library / loop / or sum) ,

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
            column = line.split('","')  #splits the row based on ","
            overviews = column[4].split('",', 1)  #splits everything after overview ", one time
            lst.append(overviews[0])  #adds just the overview text to the list

    return lst

def count_lengths(overview_list):
    """
    For each element of the overview_list, the function computes the length 
    (the number of characters in the string). The results are stored in a 
    dictionary of length occurrences where the keys are the lengths seen in 
    overview_list and the values are the number of times each length occurs. 
    Returns the dictionary of length occurrences.
    """
    #dictionary: keys = lengths in list & values = # of times each length occurs
    #ex: 600:2 , length of 600 occurs twice
    counts = {}
    ### map length and count
    # if length once appears, increment the count for that length
    # if it does not appear, set it to 1
    for overview in overview_list:
        length = len(overview)  #stores the length of each overview

        if length in counts:
            counts[length] = counts[length] + 1
        else:
            counts[length] = 1

    return counts


def const_num_sentences(overview_list):
    """
    For each element of the overview_list, the function computes the number of periods (.) 
    (as a proxy for the number of sentences). The results are stored in
    a dictionary of occurrences where the keys are the number of periods 
    seen in overview_list and the values are the number of times each occurs.
    Returns the dictionary of occurrences.
    """
    ### Keys = num of periods in overview_lists , values = num of period occurences
    ### map number of periods and occurences
    # use count() method which counts the number of occurences
    counts = {}
    for overview in overview_list:
        num_of_periods = overview.count(".")
        #print(num_of_periods)

        if num_of_periods in counts:
            counts[num_of_periods] += 1
        else:
            counts[num_of_periods] = 1

    return counts


def compute_mean(counts):
    """
    Computes the mean (average) of counts dictionary weighting each key that occurs by 
    its value (e.g. if the key of 10 has value 8, then the 10 showed up 8 times and adds 
    10*8 to the computation of the average). Returns the mean.
    """
    ### this function computes the average of the counts in the dictionary {key, value}
    # ex: {5:3 , 6:2. 8:3} -> 5 periods appear 3 times, etc 
    # so the average would be (5*3)+(6*2)+(8*3) divided by total values
    mean = 0
    overall_total = 0 # if 2 occurences of 4 are counted, multiply 2*4, etc and add each up
    total_occurences = 0 #if 2 occurences of 4, 2 is counted. add all occurences up to get total

    # check size of dictionary; if empty, return 0
    if len(counts) == 0:
        return 0.0

    for key, value in counts.items():
        overall_total += key * value
        total_occurences += value

    mean = overall_total / total_occurences

    return mean

def compute_mse(theta, counts):
    """
    Computes the Mean Squared Error of the parameter theta and a dictionary, counts.
    Returns the MSE.
    """
    if len(counts) == 0:
        return 0.0
    
    mse = 0
    total_occurences = 0
    for key, value in counts.items():
        mse += ((key - theta) ** 2) * value
        total_occurences += value

    mse = mse / total_occurences

    return mse

def test_compute_mean(mean_fnc=compute_mean):
    """
    Returns True if the mean_fnc performs correctly
    (e.g. computes weighted mean of inputted dictionary) and False otherwise. 
    """
    correct = True

    #5*2 = 10, 8*1 = 8, 10+8 = 18, 18/3 = 6
    test_counts = {5: 2, 8: 1}
    if mean_fnc(test_counts) != 6:
        correct = False
    return correct


def test_mse(mse_fnc=compute_mse):
    """
    Returns True if the extract_fnc performs correctly
    (e.g. computes mean squared error) and False otherwise.
    """

    correct = True
    test_counts = {5: 2, 8: 1}

    if mse_fnc(6, test_counts) != 2:
        correct = False

    return correct

def test_count_lengths(counts_fnc=count_lengths):
    """
    Returns True if the counts_fnc performs correctly
    (e.g. counts lengths of overviews and stores in dictionary) & False otherwise.
    """

    correct = True
    overview_test = ["Python", "Mean", "Length"]
    actual_counts = {6: 2, 4: 1}

    if counts_fnc(overview_test) != actual_counts:
        correct = False

    return correct


def main():
    """
    Some examples of the functions in use:
    """
    ### Test Output for extract_overviews function on Staten Island Schools:
    file_name = '2021_DOE_High_School_Directory_20260925.csv'
    si_overviews = extract_overviews(file_name)
    print(f"Number of SI overviews: {len(si_overviews)}. The the last one is:\n")
    print(textwrap.fill(si_overviews[-1],80))

    ### Test output for constant model functions on Staten Island Schools:
    # Count of total characters in an overview and it's number of occurences
    si_len_counts = count_lengths(si_overviews)
    print(f"The {sum(si_len_counts.values())} entries have lengths:")    
    print(si_len_counts)

    # Count of total periods in an overview and it's number of occurences
    si_dots_counts = const_num_sentences(si_overviews)
    print(f"The {sum(si_dots_counts.values())} entries have lengths:")
    print(si_dots_counts)

    # 
    si_len_mean = compute_mean(si_len_counts)
    si_dots_mean = compute_mean(si_dots_counts)
    print(f"Staten Island high schools overviews had an average of {si_len_mean:.2f}\
    characters in {si_dots_mean:.2f} sentences.")

    ###Computing MSE:
    losses = []
    for theta in range(10):
        loss = compute_mse(theta,si_dots_counts)
        print(f"For theta = {theta}, MSE loss is {loss:.2f}.")
        losses.append(loss)

    ###Testing
    #Trying first on the correct function:
    print(f'test_compute_mean(compute_mean) returns {test_compute_mean(compute_mean)}.')
    #Trying on a function that returns 42 no matter what the output:
    print(f'test_compute_mean( lambda x : 42 ) returns {test_compute_mean(lambda x : 42)}.')

if __name__ == "__main__":
    main()
