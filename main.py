# m would be equal to 3
# eventually we would have m as a parameter to generate strings of length 'm'

# we assume that string1 and string have the same length
alphabet = "abcdefghijklmnopqrstuvwxyz"

def hamming_dist(string1, string2):
    different_letters = 0
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            different_letters += 1

    return different_letters

def closest_string(strings, k):
    print(strings)
    generated_string = "test"
    return generated_string

strings = ["cata", "cota", "sstb"]
k = 2

generated_string = closest_string(strings, k)
print(generated_string)
