import unittest
import main
class TestQuizScorer(unittest.TestCase):
    
    def setUp(self):
        self.score = []
        print("\nEnter 5 scores for testing: ")
        self.score = main.collect(self.score, 5)
    
    
    def test_avg(self):
        self.assertEqual(main.avg(self.score),sum(self.score)/len(self.score))
        
    def test_empty_list(self):
        scores = []
        with self.assertRaises(ZeroDivisionError):
            main.avg(scores)
            
        
    def test_highest(self):
        result = main.highest(self.score)
        self.assertEqual(result, max(self.score))
        
    def test_lowest(self):
        result = main.lowest(self.score)
        self.assertEqual(result, min(self.score))
        
if __name__ == "__main__":
    unittest.main()