#!/usr/bin/python3
# written by: atholcomb
# correct_stream.py
# Create a function that takes in two lists: the list of user-typed words, 
# and the list of correctly-typed words and outputs a list 
# containing 1s (correctly-typed words) and -1s (incorrectly-typed words).

def correct_stream(correctlist, userlist):
    count = []
    
    for cl in correctlist:
        if cl in userlist:
            count.append(1)
        else:
            count.append(-1)

    return count


print(correct_stream(["it", "is", "find"], ["it", "is", "fine"])) # [1, 1, -1]
print(correct_stream(["april", "showrs", "bring", "may", "flowers"], ["april", "showers", "bring", "may", "flowers"])) # [1, -1, 1, 1, 1]
