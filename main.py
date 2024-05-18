# m would be equal to 3
# eventually we would have m as a parameter to generate strings of length 'm'

alphabet = "abcdefghijklmnopqrstuvwxyz"

#def generate_input_strings()

# we assume that string1 and string2 have the same length
def hamming_dist(string1, string2):
    count = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1

    return count

def populate_freq_dict(strings, m):
    chars = {}

    # for i in range(m):

    for string in strings:
        for letter in string:
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1
    return chars


def closest_string(strings):
    m = len(strings[0])
    print(strings)

    generated_string = "csta"
    for string in strings:
        print(hamming_dist(string, generated_string))

    chars = populate_freq_dict(strings, m)

    # for letter in string
    for i in range(m):
        char_freqency = 0
    #    for string in strings:
            

    print(str(chars))

    return generated_string

strings = ["cata", "cota", "sstb"] #csta


generated_string = closest_string(strings)
print(generated_string)

# asdb rxty fmza -> axzy, fxdy
# 3
# 2
# 3

#i think there could be multiple strings that have the same 'hamming distance'
#in others word, multiple 'closest string'
#ask if it's possible

#is it possible to check if the generated string this algo gives is indeed the 'closest string'?

# asdb axty fmza -> amdy, amda
# asdb - amdy: 2, asdb - amda: 2 
# axty - amdy: 2, axty - amda: 3
# fmza - amdy: 3, fmza - amda: 2

# k = 2

# -iterate through alfabets letters
# -change letter of 'generate_string'
# to current letter from alfabet
# -count of how many times does the letter appear
# in the current position of each string
# -if frequency of the letter in the current
# position of 'generated_string' is the biggest
# we keep the letter in the string.
# maybe we would have like a dictionary for each
# position (holy shit, an array of dictionaries)
# -we print the hamming distance between each
# string in 'strings' and the generated string