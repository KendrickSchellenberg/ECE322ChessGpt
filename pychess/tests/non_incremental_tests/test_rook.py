from unittest.mock import Mock

from chess_engine import game_state
from enums import Player
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

# Mocking the Rook class (and other piece classes if needed) since it's used in the initialization
Rook = Mock(spec=Rook)
Knight = Mock(spec=Knight)
Bishop = Mock(spec=Bishop)
Queen = Mock(spec=Queen)
King = Mock(spec=King)
Pawn = Mock(spec=Pawn)

class MockGameState(Mock):
    def __init__(self):
        super(MockGameState, self).__init__(spec=game_state)

        self.move_log = []
        self.white_turn = True
        self.valid_moves = {}

        self.can_en_passant_bool = False
        self._en_passant_previous = (-1, -1)

        self.checkmate = False
        self.stalemate = False
        self._is_check = False

        self._white_king_location = [0, 3]
        self._black_king_location = [7, 3]

        # Has king not moved, has Rook1(col=0) not moved, has Rook2(col=7) not moved
        self.white_king_can_castle = [True, True, True]
        self.black_king_can_castle = [True, True, True]

        # Initialize White pieces
        white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
        white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)
        white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
        white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
        white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)
        white_pawn_4 = Pawn('p', 1, 3, Player.PLAYER_1)
        white_pawn_5 = Pawn('p', 1, 4, Player.PLAYER_1)
        white_pawn_6 = Pawn('p', 1, 5, Player.PLAYER_1)
        white_pawn_7 = Pawn('p', 1, 6, Player.PLAYER_1)
        white_pawn_8 = Pawn('p', 1, 7, Player.PLAYER_1)

        # Initialize Black Pieces
        black_rook_1 = Rook('r', 7, 0, Player.PLAYER_2)
        black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_queen = Queen('q', 7, 4, Player.PLAYER_2)
        black_king = King('k', 7, 3, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)

        self.board = [
            [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
             white_rook_2],
            [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
             white_pawn_8],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
             Player.EMPTY],
            [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7,
             black_pawn_8],
            [black_rook_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
             black_rook_2]
        ]

    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        else:
            return None

    def is_valid_piece(self, row, col):
        evaluated_piece = self.get_piece(row, col)
        return evaluated_piece is not None and evaluated_piece != Player.EMPTY

# Replace references to game_state with MockGameState in your tests
import unittest
from unittest.mock import MagicMock, patch
from enums import Player
from rook import Rook  # Assuming your Rook class is in a file named rook.py

class TestRookGetValidPieceMoves(unittest.TestCase):
    def setUp(self):
        self.mocked_game_state = MockGameState()
        self.mock_white = Mock(spec=Player)
        self.mock_black = Mock(spec=Player)
        self.mock_white.name = "WHITE"
        self.mock_black.name = "BLACK"

    def test_get_valid_piece_moves_left(self):
        rook = Rook('r', 3, 3, self.mock_white)
        with patch.object(rook, 'get_col_number', return_value=3):
            moves = rook.get_valid_piece_moves(self.mocked_game_state)
        expected_moves = [(3, 0), (3, 1), (3, 2)]
        for move in expected_moves:
            self.assertIn(move, moves)

    def test_get_valid_piece_moves_right(self):
        rook = Rook('r', 3, 3, self.mock_white)
        with patch.object(rook, 'get_col_number', return_value=3):
            moves = rook.get_valid_piece_moves(self.mocked_game_state)
        expected_moves = [(3, 4), (3, 5), (3, 6), (3, 7)]
        for move in expected_moves:
            self.assertIn(move, moves)

    def test_get_valid_piece_moves_above(self):
        rook = Rook('r', 3, 3, self.mock_white)
        with patch.object(rook, 'get_row_number', return_value=3):
            moves = rook.get_valid_piece_moves(self.mocked_game_state)
        expected_moves = [(2, 3)]
        for move in expected_moves:
            self.assertIn(move, moves)

    def test_get_valid_piece_moves_below(self):
        rook = Rook('r', 3, 3, self.mock_white)
        with patch.object(rook, 'get_row_number', return_value=3):
            moves = rook.get_valid_piece_moves(self.mocked_game_state)
        expected_moves = [(4, 3), (5, 3)]
        for move in expected_moves:
            self.assertIn(move, moves)

    def test_get_valid_piece_moves_all(self):
        rook = Rook('r', 3, 3, self.mock_white)
        with patch.object(rook, 'get_row_number', return_value=3), \
                patch.object(rook, 'get_col_number', return_value=3):
            moves = rook.get_valid_piece_moves(self.mocked_game_state)
        expected_moves = [
            (4, 3), (5, 3),  # Above
            (2, 3),  # Below
            (3, 2), (3, 1), (3, 0),  # Left
            (3, 4), (3, 5), (3, 6), (3, 7),  # Right
        ]

        for move in expected_moves:
            self.assertIn(move, moves)

if __name__ == '__main__':
    unittest.main()
