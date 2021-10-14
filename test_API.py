# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:44:08 2021

@author: Tim
"""
import unittest

import API

class TestAPI(unittest.TestCase):
    
    def test_correct_url(self):
        
        
        self.assertEqual(API.api('TWT1989'), "https://api.github.com/users/TWT1989/repos")
        self.assertEqual(API.api('richkempinski'), "https://api.github.com/users/richkempinski/repos")
        
if __name__ == '__main__':
    unittest.main()
    