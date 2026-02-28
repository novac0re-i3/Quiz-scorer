import unittest
import main
class TestQuizScorer(unittest.TestCase):
    
    def test_avg(self):
        scores=[2,3,2,0,1]
        self.assertEqual(main.avg(scores),sum(scores)/len(scores))
        
    def test_empty_list(self):
        scores = []
        with self.assertRaises(ZeroDivisionError):
            main.avg(scores)
            
        
    def test_highest(self):
        scores=[2,3,2,0,1]
        result = main.highest(scores)
        self.assertEqual(result, max(scores))
        
    def test_lowest(self):
        scores=[2,3,2,0,1]
        result = main.lowest(scores)
        self.assertEqual(result, min(scores))
        
if __name__ == "__main__":
    unittest.main()
    