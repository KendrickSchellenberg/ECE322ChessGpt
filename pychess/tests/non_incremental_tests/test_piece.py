import unittest
from unittest.mock import Mock
from piece import Piece  # Assuming your Piece class is in a separate file named piece.py

class TestPieceInitialization(unittest.TestCase):
    def test_init(self):
        # Mock the Player enum for testing
        mocked_player = Mock()

        # Create a Piece instance with mocked player
        piece = Piece(name="TestPiece", row_number=0, col_number=0, player=mocked_player)

        # Assert that the attributes are set correctly
        self.assertEqual(piece.get_name(), "TestPiece")
        self.assertEqual(piece.get_row_number(), 0)
        self.assertEqual(piece.get_col_number(), 0)
        self.assertEqual(piece.get_player(), mocked_player)

    def test_change_position(self):
        # Mock the Player enum for testing
        mocked_player = Mock()

        # Create a Piece instance with mocked player
        piece = Piece(name="TestPiece", row_number=0, col_number=0, player=mocked_player)

        # Change the position
        piece.change_position((1, 2))

        # Assert that the position is changed correctly
        self.assertEqual(piece.get_row_number(), 1)
        self.assertEqual(piece.get_col_number(), 2)

if __name__ == '__main__':
    unittest.main()
