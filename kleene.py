import re


class kleene:
    """
    common regex usage translation
    """
    
    def __init__(self):
        pass
    
    def list_to_xor_regex(self, list):
        """
        returns regex expression for list of values
        """
        return '^(' + ''.join(['\\b'+str(y)+'|' for x, y in enumerate(list) if x != len(list)]) + ')'+'{1}'+'$'

    def list_to_and_regex(self, list):
        return '' + ''.join(['(?=.*'+str(y)+')' for x, y in enumerate(list) if x != len(list)]) + ''


if __name__ == '__main__':
    k = kleene()
    z = [1, 2, 3, 4, 5]
    pattern_str = k.list_to_xor_regex(z)
    print(f'pattern {pattern_str}')
    f = re.search(pattern_str, '3')
    print(f)
    z = ['Hello', 'Goodbye', 'Aloha']
    pattern_str = k.list_to_xor_regex(z)
    print(f'pattern {pattern_str}')
    f = re.search(pattern_str, '3')
    print(f)
    z = [1, 2, 3, 4, 5]
    pattern_str = k.list_to_and_regex(z)
    print(f'pattern {pattern_str}')
    f= re.search(pattern_str, '54321')
    print(f)
    f= re.search(pattern_str, '42513')
    print(f)
    f= re.search(pattern_str, '4251355555')
    print(f)
        
