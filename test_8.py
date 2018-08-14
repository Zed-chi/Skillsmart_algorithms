"""
python -m unittest tests.py
"""
import unittest
from OrderedList import Node2, OrderedList, OrderedStringList, fill



class OrderedListTest(unittest.TestCase):
    def test_asc_direction(self):
        a = OrderedList("asc")
        fill([1,5,0,4,23,4,6], a)
        self.assertEqual(str([0, 1, 4, 4, 5, 6, 23]), str(a))
    
    def test_desc_direction(self):
        d = OrderedList("desc")
        fill([1,5,0,4,23,4,6], d)
        self.assertEqual(str([23, 6, 5, 4, 4, 1, 0]), str(d))

    def test_find_item(self):
        a = OrderedList("asc")
        fill([1,5,0,4,23,4,6], a)
        self.assertEqual("Item not found, interrupt", a.find(Node2(2)))

class OrderedStringListTest(unittest.TestCase):
    def test_asc_direction(self):
        a = OrderedStringList("asc")
        fill(["a bta", "bc", "poiuy", "ceda", "eczxc", "zsasasd"], a)
        self.assertEqual(str(['a bta', 'bc', 'ceda', 'eczxc', 'poiuy', 'zsasasd']), str(a))
    
    def test_desc_direction(self):
        d = OrderedStringList("desc")
        fill(["a bta", "bc", "poiuy", "ceda", "eczxc", "zsasasd"], d)
        self.assertEqual(str(['zsasasd', 'poiuy', 'eczxc', 'ceda', 'bc', 'a bta']), str(d))
    
    def test_find_item(self):
        a = OrderedList("asc")
        fill(["a bta", "bc", "poiuy", "ceda", "eczxc", "zsasasd"], a)
        self.assertEqual("Item not found, interrupt", a.find(Node2("c")))
    
if __name__ == "__main__":
    unittest.main()
