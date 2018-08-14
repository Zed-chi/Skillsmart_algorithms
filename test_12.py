import unittest
from Cache import Cache

class CacheTest(unittest.TestCase):

  #===============Initial==========================
  def setUp(self):
    self.c = Cache(5,1)
    keys = list(map(lambda x:chr(x),range(97,102)))
    values = list(range(2,7))
    for i in range(5):
      self.c.put(keys[i],values[i])

  def tearDown(self):
    del self.c
  
  #==============Testing===================
  def test_request_increment(self):
    id = self.c.find("a", self.c.keys)
    before = self.c.hits[id]
    self.c.get("a")
    after = self.c.hits[id]
    self.assertTrue(after == before+1)

  def test_put(self):
    x = Cache(5,1)
    x.put("key","value")
    self.assertTrue(x.get("key") == "value")

  def test_remove(self):
    self.c.get("a")
    self.c.get("b")
    self.c.get("c")
    self.c.get("e")
    self.c.remove()
    self.assertEqual(self.c.get("d"), None)

  def test_put_in_full(self):
    self.c.get("a")
    self.c.get("b")
    self.c.get("c")
    self.c.get("e")
    self.assertTrue(self.c.get("key") == None)
    self.c.put("key","value")
    self.assertFalse(self.c.get("key") == None)
    self.assertTrue(self.c.get("d") == None)    

if __name__ == "__main__":
    unittest.main()