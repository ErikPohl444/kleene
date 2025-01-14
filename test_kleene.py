from unittest import TestCase
from kleene import kleene
import re


class testKleene(TestCase):
    
    def test_lov_xor_strings(self):
        print("initiating test lov xor strings")
        lov = ['Hello', 'Goodbye', 'Aloha']
        clean = kleene()
        regex_pattern_string = clean.list_to_xor_regex(lov)
        print(f"For lov [{lov}], the following regex pattern string was constructed by Kleene [{regex_pattern_string}]")
        xor_satisfied = bool(re.match(regex_pattern_string, 'Hello'))
        xor_unsatisfied = bool(re.match(regex_pattern_string, 'HelloGoodbye'))
        xor_too_much = bool(re.match(regex_pattern_string, 'AlohaAloah'))
        xor_not_found = bool(re.match(regex_pattern_string, 'Aloah'))
        self.assertEqual(xor_satisfied, True, msg='xor satisfied')
        self.assertEqual(xor_unsatisfied, False, msg='xor unsatisfied')
        self.assertEqual(xor_too_much, False, msg='xor too much')
        self.assertEqual(xor_not_found, False, msg='xor not found')

    def test_lov_xor_numbers(self):
        print("initiating test lov xor numbers")
        lov = [1, 2, 3]
        clean = kleene()
        regex_pattern_string = clean.list_to_xor_regex(lov)
        print(f"For lov [{lov}], the following regex pattern string was constructed by Kleene [{regex_pattern_string}]")
        xor_satisfied = bool(re.match(regex_pattern_string, '1'))
        xor_unsatisfied = bool(re.match(regex_pattern_string, '12'))
        xor_too_much = bool(re.match(regex_pattern_string, '1one'))
        xor_not_found = bool(re.match(regex_pattern_string, 'one'))
        self.assertEqual(xor_satisfied, True, msg='xor satisfied')
        self.assertEqual(xor_unsatisfied, False, msg='xor unsatisfied')
        self.assertEqual(xor_too_much, False, msg='xor too much')
        self.assertEqual(xor_not_found, False, msg='xor not found')


        
