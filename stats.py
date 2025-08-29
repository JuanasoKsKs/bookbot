#Takes a STRING and return and INTEGER of the number of words
def words_in_book(file_contents):
    number_of_words = len(file_contents.split())
    return number_of_words

#Takes a STRING and return a DICTIONARY with the number of each character repeated (LOWERCASE)
def get_char(file_contents):
    char_dic = {}
    for char in file_contents:
        ch = char.lower()
        if ch in char_dic:
            char_dic[ch] += 1
        else:
            char_dic[ch] = 1
    return char_dic

def sort_on(d):
    return d["num"]

#Takes a dictionary and return a list of sorted dictionaries
def dict_to_sorted_list(dictionary):
    new_list = []
    for each in dictionary:
        new_list.append({"char": each, "num": dictionary[each]})
    new_list.sort(reverse = True, key = sort_on)
    return new_list