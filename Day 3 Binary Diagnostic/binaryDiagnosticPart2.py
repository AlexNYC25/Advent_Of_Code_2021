
def get_common_values(words, position):
    zeros_count = 0
    ones_count = 0
    for w in words:
        if(w[position] == "0"):
            zeros_count += 1
        else:
            ones_count += 1
    
    if(ones_count > zeros_count):
        return (1, 0)
    elif(ones_count < zeros_count):
        return (0, 1)
    else:
        return (1, 1)

with open("input.txt", "r") as file:
    x = file.readlines()

# strip lines of whitespace
x = [i.rstrip() for i in x]

# get copys of lines from text files for each search
possible_oxygen_words = x.copy()
possible_scrubber_words = x.copy()

# inititalize variables for keeping track of the most and least common values
most_common_value = 0
least_common_value = 0

# for each possible position in the binary word
for pos in range(len(x[0])):
    
    # get the most and least common values for the current position
    most_common_value, least_common_value = get_common_values(possible_oxygen_words, pos)

    # for each word in the list of possible oxygen words
    for word in possible_oxygen_words:
        # if the word has the same amount of ones and zeros
        if(most_common_value == least_common_value):
            # for every word in the list of possible oxygen words, remove the ones with zero in the current position
            for pw in possible_oxygen_words:
                if(pw[pos] == "0"):
                    possible_oxygen_words.remove(pw)
        else:
            # for each word in the list of possible oxygen words, remove the ones with the least commmon value in the current position
            for pw in possible_oxygen_words:
                if(pw[pos] == str(least_common_value)):
                    possible_oxygen_words.remove(pw)
    
    # once there is just one word left in the list of possible oxygen words, break the for loop
    if(len(possible_oxygen_words) == 1):
        break

oxygen_rating = int(possible_oxygen_words[0], 2)


for pos in range(len(x[0])):
    
    most_common_value, least_common_value = get_common_values(possible_scrubber_words, pos)

    for word in possible_scrubber_words:
        if(most_common_value == least_common_value):
            for pw in possible_scrubber_words:
                if(pw[pos] == "1"):
                    possible_scrubber_words.remove(pw)
        else:
            for pw in possible_scrubber_words:
                if(pw[pos] == str(most_common_value)):
                    possible_scrubber_words.remove(pw)
    
    if(len(possible_scrubber_words) == 1):
        break
    
scrubber_rating = int(possible_scrubber_words[0], 2)

print(scrubber_rating * oxygen_rating)