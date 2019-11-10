#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
'''
Created on 31 ‎October ‎2019, ‏‎09:30:45
@author: Sunil Kumar Swarna
Export Container Class
'''
import unittest
from HW09_Sunil_Swarna import Container

file_path = 'C:/Users/sunil/Downloads/Testing'  ## Change this file_path


class TestContainer(unittest.TestCase):
    """ Unit testing File Generators """

    def test_student_table(self):
        """ Verifying student pretty table functionality """

        test_path = Container(file_path)

        students_pretty_table = test_path.students_summary()
        expected = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']], ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']]]
        self.assertEqual(students_pretty_table, expected) 

    def test_instructor_table(self):
        """ Verifying instrctors pretty table functionality """

        test_path = Container(file_path)

        instructors_pretty_table = test_path.instructor_summary()
        expected = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 2], 
        ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 2], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 2], 
        ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1]]

        self.assertEqual(instructors_pretty_table, expected)

    

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
