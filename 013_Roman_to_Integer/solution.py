def romanToInt(s: str) -> int:
    result = 0

    symbol_value_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    modifier_map = {'I':('V','X'), 'X':('L','C'), 'C':('D','M')}
    modifiers = list(modifier_map.keys())

    modify_next = ''
    for symbol in s:
        result += symbol_value_map[symbol]
        if modify_next and (symbol in modifier_map[modify_next]):
            result -= 2 * symbol_value_map[modify_next]
            modify_next = ''
            continue
        if symbol in modifiers:
            modify_next = symbol

    return result
            
