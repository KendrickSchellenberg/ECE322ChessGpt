import unittest
from unittest.mock import Mock

from enums import Player
from piece import Piece
from rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        # Create mock instances for Player.WHITE and Player.BLACK
        self.mock_white = Mock(spec=Player)
        self.mock_black = Mock(spec=Player)
        self.mock_white.name = "WHITE"
        self.mock_black.name = "BLACK"

    def test_get_valid_piece_moves_empty_board(self):
        # Test Rook moves on an empty board
        rook = Rook("Rook", 3, 3, self.mock_white)
        game_state = MockGameState(Player.EMPTY)
        moves = rook.get_valid_piece_moves(game_state)

        # Define the expected moves based on the Rook's position (3, 3) on an empty board
        expected_moves = [
            (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7),
            (0, 3), (1, 3), (2, 3), (4, 3), (5, 3), (6, 3), (7, 3),
        ]

        # Assertions
        self.assertCountEqual(moves, expected_moves)
        # Add more specific assertions based on your expected behavior

    def test_get_valid_piece_moves_with_opponent_pieces(self):
        # Test Rook moves with opponent pieces on the board
        rook = Rook("Rook", 4, 4, self.mock_black)
        game_state = MockGameStateWithPieces(self.mock_white)
        moves = rook.get_valid_piece_moves(game_state)

        # Define the expected moves and takes based on the Rook's position (4, 4) with opponents nearby
        expected_moves = [
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7),
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
        ]

        # Assertions
        self.assertCountEqual(moves, expected_moves)
        # Add more specific assertions based on your expected behavior

# Mock class for testing
class MockGameState:
    def __init__(self, mock_player):
        self.mock_player = mock_player

    def get_piece(self, row, col):
        return self.mock_player

    def is_valid_piece(self, row, col):
        return True

# Mock class for testing with opponent pieces
class MockGameStateWithPieces(MockGameState):
    def get_piece(self, row, col):
        if row == 4 and col == 3:
            return Piece("Opponent", row, col, Player.WHITE)
        elif row == 4 and col == 5:
            return Piece("Opponent", row, col, Player.WHITE)
        elif row == 3 and col == 4:
            return Piece("Opponent", row, col, Player.WHITE)
        elif row == 5 and col == 4:
            return Piece("Opponent", row, col, Player.WHITE)
        else:
            return Player.EMPTY

if __name__ == '__main__':
    unittest.main()
