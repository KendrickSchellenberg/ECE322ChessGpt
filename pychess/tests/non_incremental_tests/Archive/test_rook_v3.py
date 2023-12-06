import unittest
from unittest.mock import Mock
from enums import Player
from piece import Piece
from rook import Rook  # Assuming your Rook class is in a separate file named rook.py

class TestRookInitialization(unittest.TestCase):
    def test_init(self):
        # Mock the Player enum for testing
        mocked_player = Mock(spec=Player)

        # Create a Rook instance with mocked player
        rook = Rook(name="Rook", row_number=0, col_number=0, player=mocked_player)

        # Assert that the attributes are set correctly
        self.assertEqual(rook.get_name(), "Rook")
        self.assertEqual(rook.get_row_number(), 0)
        self.assertEqual(rook.get_col_number(), 0)
        self.assertEqual(rook.get_player(), mocked_player)
        self.assertFalse(rook.has_moved)

if __name__ == '__main__':
    unittest.main()
