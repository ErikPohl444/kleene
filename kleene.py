import re


class kleene():
    '''
    common regex usage translation
    '''
    
    def __init__(self):
        pass
    
    def strict_list_of_values(self, list):
        '''
        returns regex expression for list of values
        '''
        return '^(' + ''.join(['\\b'+str(y)+'|' for x, y in enumerate(list) if x != len(list)]) + ')'+'{1}'+'$'


if __name__ == '__main__':
    k = kleene()
    z = [1, 2, 3, 4, 5]
    pattern_str = k.strict_list_of_values(z)
    print(f'pattern {pattern_str}')
    f = re.search(pattern_str, '3')
    print(f)
    z = ['Hello', 'Goodbye', 'Aloha']
    pattern_str = k.strict_list_of_values(z)
    print(f'pattern {pattern_str}')
    import re
    f = re.search(pattern_str, '3')
    print(f)
        
        
