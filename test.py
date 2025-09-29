import unittest
from boggle_solver import Boggle

class TestBoggleSolver(unittest.TestCase):

    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        solver = Boggle(grid, dictionary)
        self.assertEqual(solver.getSolution(), [])

    def test_empty_grid(self):
        grid = []
        dictionary = ["a", "ab", "abc"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(solver.getSolution(), [])

    def test_single_cell_grid(self):
        grid = [["A"]]
        dictionary = ["a", "aa"]
        solver = Boggle(grid, dictionary)
        # no word ≥ 3 letters possible
        self.assertEqual(solver.getSolution(), [])

    def test_word_entire_grid(self):
        grid = [["C","A"],["T","S"]]
        dictionary = ["cats"]
        solver = Boggle(grid, dictionary)
        self.assertIn("cats", solver.getSolution())

    def test_no_words_found(self):
        grid = [["X","Y"],["Z","W"]]
        dictionary = ["cat", "dog"]
        solver = Boggle(grid, dictionary)
        self.assertEqual(solver.getSolution(), [])

    def test_duplicate_letters(self):
        grid = [["A","A"],["A","A"]]
        dictionary = ["aaa", "aaaa"]
        solver = Boggle(grid, dictionary)
        result = solver.getSolution()
        self.assertIn("aaa", result)
        self.assertIn("aaaa", result)

    def test_multiple_valid_words(self):
        grid = [["T","E"],["N","D"]]
        dictionary = ["ten","end","tend"]
        solver = Boggle(grid, dictionary)
        result = solver.getSolution()
        self.assertCountEqual(result, ["end","ten","tend"])

    def test_qu_special_case(self):
        grid = [["Qu","A"],["R","T"]]
        dictionary = ["quart","qua"]
        solver = Boggle(grid, dictionary)
        result = solver.getSolution()
        self.assertIn("quart", result)
        self.assertIn("qua", result)

    def test_minimum_word_length(self):
        grid = [["C","A"],["T","S"]]
        dictionary = ["ca","cat","cats"]
        solver = Boggle(grid, dictionary)
        result = solver.getSolution()
        self.assertNotIn("ca", result)  # shorter than 3
        self.assertIn("cat", result)
        self.assertIn("cats", result)

    def test_case_insensitivity(self):
        grid = [["T","E"],["N","D"]]
        dictionary = ["Ten","End","TEND"]
        solver = Boggle(grid, dictionary)
        result = solver.getSolution()
        # should match regardless of case
        self.assertCountEqual(result, ["end","ten","tend"])


if __name__ == "__main__":
    unittest.main()
