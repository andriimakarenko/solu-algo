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
