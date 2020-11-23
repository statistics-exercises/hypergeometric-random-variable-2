import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for M in range(10,15) :
            for N in range(5,8) : 
                for R in range(1,N) : 
                    mean = 0 
                    for k in range(100) : mean = mean + choice_with_replacement(M,R,N) 
                    prob = R/N
                    bar = np.sqrt(M*prob*(1-prob)/100)*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean/100 - M*prob )<bar, "Your function for generating the variables is not working" )
