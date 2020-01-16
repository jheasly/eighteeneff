import unittest

from main import get_zipcode_rate_area, get_plans

class Test_get_zipcode_rate_area(unittest.TestCase):
    def test_zipcode(self):
        '''
        Test with a zipcode
        '''
        data = '64148'
        result = get_zipcode_rate_area('64148')
        self.assertEqual(result, ['MO', '3', 'Silver'])


class Test_get_plans(unittest.TestCase):
    def test_st_area_plan(self):
        '''
        Test with a state abbrv, area, plan type
        '''
        data = ['MO', '3', 'Silver']
        result = get_plans(['MO', '3', 'Silver'])
        self.assertEqual(result, '245.2')

if __name__ == '__main__':
    unittest.main()

