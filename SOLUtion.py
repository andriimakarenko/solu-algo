def common_prefix(str1, str2):
    common_prefix_letters = []
    shortest_word, other_word = (str1, str2) if len(str1) < len(str2) else (str2, str1)

    for i, letter in enumerate(shortest_word):
        if other_word[i] == letter:
            common_prefix_letters.append(letter)
    
    return ''.join(common_prefix_letters)


def longest_common_prefix_v1(str_list):
    """Longest common prefix found by overwriting a var"""
    
    longest_common_prefix = ''

    while len(str_list) > 0:
        longest_common_prefix_with_current_word = ''
        popped_str = str_list.pop()
        
        for current_str in str_list:
            current_pair_common_prefix = common_prefix(popped_str, current_str)
            if len(current_pair_common_prefix) > len(longest_common_prefix_with_current_word):
                longest_common_prefix_with_current_word = current_pair_common_prefix
            
        if len(longest_common_prefix_with_current_word) > len(longest_common_prefix):
            longest_common_prefix = longest_common_prefix_with_current_word

    return longest_common_prefix if longest_common_prefix else 'No duplicates found'

str_list = ['asd', 'asdf', 'asdfg', '', 'asdfgk' 'ase', '']
print(longest_common_prefix_v1(str_list))


########################################## SOLUTION 2 ##########################################


def get_duplicates(input_list):
    uniq_list = []
    duplicates_list = []

    for i in input_list:
        if i in uniq_list:
            duplicates_list.append(i)
        else:
            uniq_list.append(i)
    
    return duplicates_list

def longest_common_prefix_v2(str_list):
    """
    Cut away the last character only from the longest strings,
    then check for duplicates.
    Example:
    Iteration 1: ['abc', 'abcd', 'abcdef', 'hello']
    Iteration 2: ['abc', 'abcd', 'abcde', 'hello']
    Iteration 3: ['abc', 'abcd', 'abcd', 'hell']
    In iteration 3, 'abcd' is found
    """

    comparison = [] # Save resources, compare the longest strings only
    while len(str_list) > 0:
        for i, string in enumerate(str_list):
            longest_str_len = len(max(str_list, key=len))
            match len(string):
                case _ as length if length == longest_str_len:
                    comparison.append(string)
                    str_list[i] = str_list[i][:-1]
                case _ as length if length == 0:
                    str_list.pop(i)
                case _:
                    pass

        common_prefixes = get_duplicates(comparison)
        if len(common_prefixes) > 0:
            return max(common_prefixes, key=len)

    return 'No duplicates found'
        
str_list = ['asd', 'asdf', 'asdfg', '', 'asdfgk' 'ase', '']
print(longest_common_prefix_v2(str_list))