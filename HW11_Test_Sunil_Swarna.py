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
        expected = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 555'}, None],
         ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 555'}, {'CS 501'}]]
        self.assertEqual(students_pretty_table, expected)


    def test_instructor_table(self):
        """ Verifying instructors pretty table functionality """

        test_path = Container(file_path)

        instructors_pretty_table = test_path.instructor_summary()
        expected = [['98763', 'Rowland, J', 'SFEN', 'SSW 810', 2], 
        ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1]]
        self.assertEqual(instructors_pretty_table, expected)

    def test_majors_table(self):

        """ Verifying majors pretty table functionality """

        test_path = Container(file_path)

        majors_pretty_table = test_path.major_summary()
        expected = [['SFEN', ['SSW 555'], ['CS 501']], 
        ['CS', ['CS 546'], ['SSW 810']]]
        self.assertEqual(majors_pretty_table, expected)

    def test_database_instructor(self):
        """ Verifying instructors database pretty table functionality """
        test_path = Container(file_path)
        db_instructors = test_path.instructor_table_db('810_startup.db')
        expected = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], 
        ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98762', 'Hawking, S', 'CS', 'CS 501', 1],
         ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]
        self.assertEqual(db_instructors, expected)



if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
