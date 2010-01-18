# -*- coding: utf-8 -*-
from notifier import is_profane
from unittest import TestCase

class NoProfanityTest(TestCase):

    def test_is_profane__with_empty_string(self):
        self.assertEqual(is_profane(''), False)

    def test_is_profane__with_whitespace(self):
        self.assertEqual(is_profane('          '), False)

    def test_is_profane__with_a_normal_word(self):
        self.assertEqual(is_profane('sana'), False)

    def test_is_profane__with_a_normal_sentence(self):
        self.assertEqual(is_profane('Joku lause jeejee.'), False)

    def test_is_profane__with_part_of_word(self):
        """Don't report swear words that are a part of some longer word."""
        self.assertEqual(is_profane('vittukaan'), False)

    def test_is_profane__with_part_of_word_english(self):
        """Don't report swear words that are a part of some longer word."""
        self.assertEqual(is_profane('analitarian'), False)

    def test_is_profane__with_part_of_word_in_sentence(self):
        """Don't report swear words that are a part of some longer word."""
        self.assertEqual(is_profane('No vittukaan ei toimi.'), False)

    def test_is_profane__with_part_of_word_in_sentence(self):
        """Don't report swear words that are a part of some longer word."""
        self.assertEqual(is_profane('Our government is analitarian indeed.'), False)


class ProfanityTest(TestCase):

    def test_is_profane__with_swear_word(self):
        self.assertEqual(is_profane('vittu'), True)

    def test_is_profane__with_other_swear_word(self):
        self.assertEqual(is_profane('perkele'), True)

    def test_is_profane__with_scandinavian_swear_word(self):
        self.assertEqual(is_profane('perkelettä'), True)

    def test_is_profane__with_scandinavian_swear_word_unicode(self):
        self.assertEqual(is_profane(u'perkelettä'), True)

    def test_is_profane__with_swear_word_in_sentence(self):
        self.assertEqual(is_profane('No johan on vittu kun testit toimii.'), True)

    def test_is_profane__with_scandinavian_swear_word_in_sentence(self):
        self.assertEqual(is_profane('No mitäs perkelettä täällä tapahtuu.'), True)

    def test_is_profane__with_scandinavian_swear_word_in_sentence_unicode(self):
        self.assertEqual(is_profane(u'No mitäs perkelettä täällä tapahtuu.'), True)

    def test_is_profane_with_english_swear_word(self):
        self.assertEqual(is_profane('fucking'), True)

    def test_is_profane_with_english_swear_word_in_sentence(self):
        self.assertEqual(is_profane('That girl is fucking like a man.'), True)
