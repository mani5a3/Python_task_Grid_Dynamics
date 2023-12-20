import unittest
from justify_paragraph.paragraph_formatter import justify_paragraph

class TestParagraphFormatter(unittest.TestCase):

    def test_justify_paragraph(self):
        paragraph = "this is manikanta gaddam from epam system and working as devops engineer"
        width = 20

        expected_result = [
            "this is manikanta   ",
            "gaddam from epam    ",
            "system and working  ",
            "as devops engineer  "
        ]

        result = justify_paragraph(paragraph, width)
        self.assertEqual(result, expected_result)

    def test_missing_arguments(self):
        with self.assertRaises(ValueError) as cm:
            justify_paragraph(None, 20)

        self.assertEqual(str(cm.exception), "Input paragraph string cannot be empty.")

if __name__ == '__main__':
    unittest.main()
