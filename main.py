#alphabet = "abcdefghijklmnopqrstuvwxyz"
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

index_dict = {}    

def populate_freq_dict_arr(strings, m):
    freq_chars_dict_arr = [] 

    for i in range(m):
        index = 0
        freq_dict = {}
        index_dict[i] = []
        index_dict[i].append(0)
        for string in strings:
            if string[i] not in freq_dict:
                freq_dict[string[i]] = 1
            else:
                index += 1
                freq_dict[string[i]] += 1
                index_dict[i].append(index) 
        freq_chars_dict_arr.append(freq_dict)
    print("index dict: " + str(index_dict))

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
    n = len(strings)
    m = len(strings[0])
    print(strings)
    generated_string = ""
    # for string in strings:
    #     print(hamming_dist(string, generated_string))

    freq_dict_arr = populate_freq_dict_arr(strings, m)
    char_arr = populate_chars_arr(strings)

    print(char_arr)
    print(freq_dict_arr)

    highest_freq_arr = []
    index = 0
    for dictionary in freq_dict_arr:
        highest_freq = 0
        same_values = True
        same_value = list(dictionary.values())[0]
        for letter, value in dictionary.items():

            if len(dictionary)>1:
                if value != same_value:
                    same_values = False 
            else:
                same_values = False

            if highest_freq < value:
                highest_freq = value

        if same_values:
            highest_freq_arr.append(0)
        else:
            highest_freq_arr.append(highest_freq)

        #TODO!!!!!!!
        #generating string..
        # print("highest_freq_arr[" +str(index)+"]: " + str(highest_freq_arr[index]))
        if(highest_freq_arr[index] != 0):
            value = {i for i in dictionary if dictionary[i]==int(highest_freq_arr[index])}
            generated_string += str(list(value)[0])
        else:
        #print("index: " + str(index))
            if index != 0:
                temp_arr = []
                for i in range(n):
                    temp_arr.append(i)

                for el in temp_arr:
                    if el not in index_dict[index-1]:
                        arr = list(dictionary)
                        generated_string += str(arr[el])
            #else:
                

        index += 1
    print("high:" + str(highest_freq_arr))
    return generated_string

strings = ["cata", "cota", "sstb", "bbns"] #csts
#strings = ["cata", "cota", "sstb"] #csta
#strings = ["cxta", "cyta", "sytb"] #cyta
#strings = ["asdb", "rxty", "fmza"] #axzy
generated_string = closest_string(strings)
generated_string = "csts"

print(generated_string)
for string in strings:
    print(hamming_dist(generated_string, string))


# try a brute force algo after this

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
