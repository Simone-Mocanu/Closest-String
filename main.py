alphabet = "abcdefghijklmnopqrstuvwxyz"
# m - length of strings
# n - number of strings (size of the array)
# output -> a generated string (s)
# the closest string d(s,si) ≤ k (d - Hamming distance)

# eventually we would have m as a parameter to generate strings of length 'm'
#def generate_input_strings()

# we assume that string1 and string2 have the same length
def hamming_dist(string1, string2):
    count = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1

    return count

def populate_chars_arr(strings):
    arr = []
    for string in strings:
        for letter in string:
            if letter not in arr:
                arr.append(letter)
    return arr;


def populate_freq_dict_arr(strings, m):
    freq_chars_dict_arr = [] 

    for i in range(m):
        freq_dict = {}
        for string in strings:
            if string[i] not in freq_dict:
                freq_dict[string[i]] = 1
            else:
                freq_dict[string[i]] += 1
        freq_chars_dict_arr.append(freq_dict)

    return freq_chars_dict_arr

    # for string in strings:
    #     for letter in string:
    #         if letter in freq_chars:
    #             freq_chars[letter] += 1
    #         else:
    #             freq_chars[letter] = 1
    # return freq_chars



def closest_string(strings):
    # m would be equal to 3
    m = len(strings[0])
    print(strings)
    generated_string = ""
    # for string in strings:
    #     print(hamming_dist(string, generated_string))

    freq_dict_arr = populate_freq_dict_arr(strings, m)
    char_arr = populate_chars_arr(strings)

    print(char_arr)
    print(freq_dict_arr)

    for dictionary in freq_dict_arr:
        highest_freq = 0
        for letter, value in dictionary.items():
            if highest_freq < value:
                highest_freq = value

        for letter, value in dictionary.items():
            if value == highest_freq:
                generated_string += letter
            
            print(letter, value)
        print("highest freq value:" + str(highest_freq))


    return generated_string

strings = ["cata", "cota", "sstb"] #csta
generated_string = closest_string(strings)
print(generated_string)

# asdb rxty fmza -> axzy, fxdy
# 3
# 2
# 3
# k would be equal to 3 (should be the smallest for this input)

#i think there could be multiple strings that have the same 'hamming distance'
#in others word, multiple 'closest string'
#ask if it's possible

#is it possible to check if the generated string this algo gives is indeed the 'closest string'?

# asdb axty fmza -> amdy, amda
# asdb - amdy: 2, asdb - amda: 2 
# axty - amdy: 2, axty - amda: 3
# fmza - amdy: 3, fmza - amda: 2

# k = 2

# [] change letter of 'generate_string'
# to current letter from alfabet
# [] count of how many times does the letter appear
# in the current position of each string
# [] if frequency of the letter in the current
# position of 'generated_string' is the biggest
# we keep the letter in the string.
# maybe we would have like a dictionary for each
# position (holy shit, an array of dictionaries)
# [] we print the hamming distance between each
# string in 'strings' and the generated string
