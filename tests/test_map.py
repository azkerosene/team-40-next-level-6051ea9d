from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction
from levelup.map import Map
from levelup.position import Position

class TestMap(TestCase):
    
    def test_init_creates_positions(self):
        testobj = Map()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(10, len(testobj.positions))