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

    return longest_common_prefix

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
    """Just trying to get creative here tbh"""

    # If there already are duplicates, the longest of them is what we're looking for.
    # Also this scheme ensures there will never be a case like this: ['']
    # which would break the solution of max(common_prefixes, key=len) 
    common_prefixes = get_duplicates(str_list)
    
    # Cut away the last character only from the longest strings,
    # then check for duplicates.
    # Example:
    # Iteration 1: ['abc', 'abcd', 'abcdef', 'hello']
    # Iteration 2: ['abc', 'abcd', 'abcde', 'hello']
    # Iteration 3: ['abc', 'abcd', 'abcd', 'hell']
    # In iteration 3, 'abcd' is found
    comparison = [] # Save resources, compare the longest string only
    buffer = []
    while len(buffer_list) > 0:
        longest_str_len = len(max(str_list, key=len))
        for i, string in enumerate(str_list):
            match len(string):
                case _ as length if length == longest_str_len:
                    print('lol')
                case _ as length if length == 0:
                    print('kek')
                case _:
                    print('Jack The Sparrow? No, Captain Jack The Sparrow!')
            if len(string) > 0:
                buffer_list.append(string[:-1])
            else:
                str_list.pop(i)

        discovered_prefixes = get_duplicates(buffer_list)
        if len(discovered_prefixes) > 0:
            return max(discovered_prefixes, key=len)
        
        str_list = buffer_list
        buffer_list = []

    return max(common_prefixes, key=len)
        
str_list = ['asd', 'asdf', 'asdfg', '', 'asdfgk' 'ase', '']
print(longest_common_prefix_v2(str_list))