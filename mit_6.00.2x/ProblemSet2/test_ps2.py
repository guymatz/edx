import unittest
import ps2
from ps2 import Position
from ps2 import RectangularRoom

class TddPosition(unittest.TestCase):

    def test_new_nonempty_position(self):
        pos = Position(3,4)
        self.assertEqual('(3.00, 4.00)', str(pos))

    def test_get_new_position(self):
        pos = Position(4,4)
        new_pos = pos.getNewPosition(90, 5)
        print str(new_pos)
        self.assertEqual('(9.00, 4.00)', str(new_pos))

class TddRectangularRoom(unittest.TestCase):

    def test_new_rec_room(self):
        room = RectangularRoom(3,4)

    def test_get_num_tiles(self):
        room = RectangularRoom(3,4)
        num_tiles = room.getNumTiles()
        self.assertEqual(12, num_tiles)

    def test_get_random_position(self):
        room = RectangularRoom(3,4)
        rand_pos = room.getRandomPosition()
        self.assertEqual('(2.00, 3.00)', str(rand_pos))

    def test_is_position_in_room(self):
        room = RectangularRoom(3,4)
        pos = Position(1,2)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertTrue(pos_in_room)

    def test_is_position_in_room_on_outer_corner(self):
        room = RectangularRoom(3,4)
        pos = Position(3,4)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertTrue(pos_in_room)

    def test_is_position_in_room_on_origin(self):
        room = RectangularRoom(3,4)
        pos = Position(0,0)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertTrue(pos_in_room)

    def test_is_position_in_room_on_side_edge(self):
        room = RectangularRoom(3,4)
        pos = Position(0,4)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertTrue(pos_in_room)

    def test_is_position_in_room_on_top_edge(self):
        room = RectangularRoom(3,4)
        pos = Position(3,0)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertTrue(pos_in_room)

    def test_is_position_in_room_outside_of_corner(self):
        room = RectangularRoom(3,4)
        pos = Position(4,4)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertFalse(pos_in_room)

    def test_is_position_in_room_outside_of_top_edge(self):
        room = RectangularRoom(3,4)
        pos = Position(3,5)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertFalse(pos_in_room)

    def test_is_position_in_room_left_of_side(self):
        room = RectangularRoom(3,4)
        pos = Position(-1,4)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertFalse(pos_in_room)

    def test_is_position_in_room_outide_of_origin(self):
        room = RectangularRoom(3,4)
        pos = Position(-1,-2)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertFalse(pos_in_room)

    def test_is_position_in_room_way_outside_of_origin(self):
        room = RectangularRoom(3,4)
        pos = Position(-5,-7)
        pos_in_room  = room.isPositionInRoom(pos)
        self.assertFalse(pos_in_room)

    def test_clean_tile_at_position(self):
        room = RectangularRoom(3,4)
        pos = Position(2,1)
        room.cleanTileAtPosition(pos)
        self.assertEqual('(2.00, 1.00)',str(room.clean_tiles[0]))

    def test_clean_tile_at_decimal_position(self):
        room = RectangularRoom(3,4)
        pos = Position(1.6,1.1)
        room.cleanTileAtPosition(pos)
        self.assertEqual('(1.00, 1.00)',str(room.clean_tiles[0]))

    def test_clean_tile_at_decimal_position(self):
        room = RectangularRoom(3,4)
        pos = Position(0.6,0.1)
        room.cleanTileAtPosition(pos)
        for t in room.clean_tiles:
            print str(t)
        self.assertTrue(room.isTileCleaned(0,0))
        
    def test_is_tile_cleaned_empty(self):
        room = RectangularRoom(3,4)
        #pos = Position(2,1)
        #room.cleanTileAtPosition(pos)
        self.assertEqual(room.clean_tiles, [])
        
    def test_is_tile_cleaned_not_empty(self):
        room = RectangularRoom(3,4)
        pos = Position(2,1)
        room.cleanTileAtPosition(pos)
        self.assertNotEqual(room.clean_tiles, [])
        
    def test_is_tile_cleaned(self):
        room = RectangularRoom(3,4)
        pos = Position(2,1)
        room.cleanTileAtPosition(pos)
        self.assertNotEqual(room.clean_tiles, ['(2.00,1.00)'])
