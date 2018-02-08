###################################################
# Name: Entity identification unittest
# Target: Test entity_identification script functions
# Receives : A entity_identification.py file
# Return : Nothing (results in console)
# Author: Yonathan Guttel <yesguttel@gmail.com>
# Last Edited: 08.02.2018
# Version: 1.0.0 (apply to entity_identification v.1.0.2)
###################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Imports ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import unittest
from NER_Tagger import phone_tagger
from NER_Tagger import mail_tagger
from NER_Tagger import list_entity_exclude_include
from NER_Tagger import remove_repeated_ent
from NER_Tagger import correct_point_tag_order


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ set parameters ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
case_1 = "0549478934"
case_2 = "zero five four nine four seven eight nine four"
case_2_2 = "zero five nine four and more digits"
case_3 = "o five 4 nine nine seven eight seven eight"
case_4 = "yesguttel@gmail.com"
case_5 = "ddebbie at embassyus dot com"
case_6 = "dmat at Stanford dot ac dot com."
list_1 =  ['Jack']
text = 'Jack loves foo and bar'
case_7 = 'bla bla {PERSON} {LOCATION} bla bla'
case_8 = 'bla more bla {PERSON} {Donald Tramp} bla too bla'
case_9 = 'bla bla {GPE} {GPE} even more bla'
case_10 = 'bla bla. {GPE} even more bla'
case_11 = 'bla bla, {GPE} even more bla'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Define unittest ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class MyTestCase(unittest.TestCase):
    def test_phone_tagger_1(self):
        self.assertEqual(str(case_1+" " + "{PHONE}"), phone_tagger(case_1))
    def test_phone_tagger_2(self):
        self.assertEqual(str(case_2 + " " + "{PHONE}"), phone_tagger(case_2))
    def test_phone_tagger_2_2(self):
        self.assertEqual(str(case_2_2), phone_tagger(case_2_2))
    def test_phone_tagger_3(self):
        self.assertEqual(str(case_3 + " " + "{PHONE}"), phone_tagger(case_3))
    def test_mail_tagger_1(self):
        self.assertEqual(str(case_4+" " + "{MAIL}"), mail_tagger(case_4))
    def test_mail_tagger_2(self):
        self.assertEqual(str(case_5+" " + "{MAIL}"), mail_tagger(case_5))
    def test_mail_tagger_3(self):
        self.assertEqual(str(case_6+" " + "{MAIL}"), mail_tagger(case_6))
    def test_list_entity_exclude_include_1(self):
        self.assertEqual('Jack {PERSON} loves foo and bar', list_entity_exclude_include(text,list_1, exclude=True ,entity='{PERSON}'))
    def test_list_entity_exclude_include_2(self):
        self.assertEqual('Jack loves {OOV} foo {OOV} and {OOV} bar {OOV}', list_entity_exclude_include(text,list_1, exclude=False ,entity='{PERSON}'))
    def test_remove_repeated_ent_1(self):
        self.assertEqual('bla bla {PERSON} bla bla', remove_repeated_ent(case_7))
    def test_remove_repeated_ent_2(self):
        self.assertEqual('bla more bla {PERSON} {Donald Tramp} bla too bla', remove_repeated_ent(case_8))
    def test_remove_repeated_ent_3(self):
        self.assertEqual('bla bla {GPE} even more bla', remove_repeated_ent(case_9))
    def test_correct_point_tag_order_1(self):
        self.assertEqual('bla bla {GPE}. even more bla', correct_point_tag_order(case_10))
    def test_correct_point_tag_order_2(self):
        self.assertEqual('bla bla {GPE}, even more bla', correct_point_tag_order(case_11))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Run tests ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
