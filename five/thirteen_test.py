import thirteen
import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.n = 10
        self.k = 3
        self.num_trials = 10000
        self.dev_pct_thresh = 10
    
    def dev_over_thresh(self, sampler_name):
        packet_counts = thirteen.get_simulated_distribution(n=self.n, k=self.k, sampler_name=sampler_name, num_trials=self.num_trials)
        num_exp = self.num_trials / self.n * self.k
        for count in packet_counts.itervalues():
            pct_dev = 100.0 * abs(num_exp - count) / num_exp
            self.assertGreater(self.dev_pct_thresh, pct_dev)
    
    def test_wrong(self):
        self.dev_over_thresh('wrong')
    
    def test_right(self):
        self.dev_over_thresh('right')
