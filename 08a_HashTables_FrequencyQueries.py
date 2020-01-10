"""
https://www.hackerrank.com/challenges/frequency-queries/
"""


# Complete the freqQuery function below.
def freqQuery(queries):
    counter_dict = {}
    hist_dict = {}
    ans_arr = []
    for query in queries:
        element = query[1]
        if query[0] == 1:
            # add element to data structure
            if element not in counter_dict:
                counter_dict[element] = 1
            else:
                counter_dict[element] += 1
            # add element to histogram dict
            freq = counter_dict[element]
            if freq not in hist_dict:
                hist_dict[freq] = []  # create bin for a frequency
            hist_dict[freq].append(element)  # add element to its corresponding freq entry in histogram dict
            if freq > 1:
                hist_dict[freq - 1].remove(element)  # remove element from the bin it was in before
        elif query[0] == 2:
            # delete element from data structure
            if element in counter_dict:
                if counter_dict[element] >= 1:
                    counter_dict[element] -= 1
                # remove element from histogram dict
                freq = counter_dict[element]
                if freq > 0:
                   hist_dict[freq].append(element)
                hist_dict[freq + 1].remove(element)
            else:
                pass
        elif query[0] == 3:
            # find element with given frequency
            res = 0
            if element in hist_dict:
                if len(hist_dict[element]) > 0:
                    res = 1
            ans_arr.append(res)
        else:
            print("invalid operation")
    #print(counter_dict)
    #print(hist_dict)
    #print(ans_arr)
    return ans_arr


# queries = [[1, 5], [1, 6], [1, 6], [2, 6]]

# queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
queries = [[3, 4], [2, 1003], [1, 16], [3, 1]]
freqQuery(queries)