#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
'''
Created on 31 ‎October ‎2019, ‏‎09:30:45
@author: Sunil Kumar Swarna
Export Container Class
'''
import unittest
from HW09_Sunil_Swarna import Container

file_path = 'Testing-Files'  ## Change this file_path


class TestContainer(unittest.TestCase):
    """ Unit testing File Generators """

    def test_student_table(self):
        """ Verifying student pretty table functionality """

        test_path = Container(file_path)

        students_pretty_table = test_path.students_summary()
        expected = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540'}, {'SSW 555'}], ['11658', 'Kelly, P', 'SYEN', [], {'SYS 800', 'SYS 612'}, {'SSW 810'}]]
        self.assertEqual(students_pretty_table, expected) 

    def test_instructor_table(self):
        """ Verifying instructors pretty table functionality """

        test_path = Container(file_path)

        instructors_pretty_table = test_path.instructor_summary()
        expected = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 1], 
        ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 1], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 1], 
        ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1]]
        self.assertEqual(instructors_pretty_table, expected)

    def test_majors_table(self):

        """ Verifying majors pretty table functionality """

        test_path = Container(file_path)

        majors_pretty_table = test_path.major_summary()
        expected = [['SFEN', ['SSW 540', 'SSW 564'], ['SSW 555']], 
        ['SYEN', ['SYS 612', 'SYS 800'], ['SSW 810']]]
        self.assertEqual(majors_pretty_table, expected)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
