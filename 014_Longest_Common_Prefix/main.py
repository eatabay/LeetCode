def longestCommonPrefix(self, strs: List[str]) -> str:
    substr = []
    # "[]" is one of the test cases, apparently
    if strs:
        first_str = strs[0]
        for i in range(len(first_str)):
            match_char = first_str[i]
            # De facto successful if we make it to the end of the loop sans error.
            matched = True
            for this_string in strs[1:]:
                if (i == len(this_string)) or (match_char != this_string[i]):
                    matched = False
                    break
            if matched:
                substr.append(match_char)
            else:
                break
    return ''.join(substr)

# Very elegant solution by someone else:
#
# zip_strs, res = zip(*strs), ""
#
## In the REPL:
# >>> s = ['helm', 'hello', 'hell', 'heel', 'help']
# >>> for zipped_s in zip(*s):
# ...     print(zipped_s)
# ... 
# ('h', 'h', 'h', 'h', 'h')
# ('e', 'e', 'e', 'e', 'e')
# ('l', 'l', 'l', 'e', 'l')
# ('m', 'l', 'l', 'l', 'p')
#
## This is the cool part...
# for item in zip_strs:
#     if len(set(item)) > 1: break
#     res += item[0]
#
# return res
