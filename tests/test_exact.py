import unittest

class TestExact(unittest.TestCase):
    """Test solver properties and algorithm of particle hopping"""

    @classmethod
    def setUpClass(cls):
        """Run only once for the all class. cf. setUp. (Note the cls rather than self in order to reference the class object)"""
        # get parameters for setting up classes?
        # should I get the parameters from the data file...?
        pass


    # you could have a skip test here for tests that do not require a set up method
    def setUp(self):
        """Load a dataset for reconstruction."""
        """ Create class attributes corresponding to stored data"""
        """Automatically called for every single test we run"""

        # this method for calling the data might be worth doing only 
        # for the final check/once

        return None

    def test_data(self):

        pass

    def test_formula(self):

        return None

    def test_trajectory_reversibility(self):
        """Here you could have a skip method to signal the test has not been set up yet"""

        return None

    def tearDown(self):
        """ Not sure - called only if setUp succeeds nevermind the test function??"""
        """Only called if the setUp method succeeds"""

        pass 