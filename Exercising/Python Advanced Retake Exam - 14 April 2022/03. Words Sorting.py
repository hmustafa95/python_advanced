def words_sorting(*args):
    my_dict = {}
    sum_of_all_values = 0
    for word in args:
        total = 0
        for letter in word:
            total += ord(letter)
            sum_of_all_values += ord(letter)
        my_dict[word] = total
    if sum_of_all_values % 2 != 0:
        sorted_dict = sorted(my_dict.items(), key=lambda x: -x[1])
    else:
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
    result = ''
    for k, v in sorted_dict:
        result += f"{k} - {v}" +'\n'
    return result
