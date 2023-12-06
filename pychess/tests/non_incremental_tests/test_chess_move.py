import unittest
from enums import Player
from chess_engine import game_state
from enums import Player
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn
from chess_engine import chess_move  # Assuming your chess_move class is in a file named chess_move.py
from chess_engine import game_state  # Assuming your game_state class is in a file named game_state.py

class TestChessMove(unittest.TestCase):
    def test_regular_move(self):
        # Create a game state with a pawn in the starting position
        initial_board = [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Pawn('p', 1, 1, Player.PLAYER_1), Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY]
        ]
        initial_game_state = game_state()
        initial_game_state.board = initial_board

        # Create a chess move from (1, 1) to (2, 1)
        move = chess_move((1, 1), (2, 1), initial_game_state, False)

        # Assert the attributes of the chess move
        self.assertEqual(move.starting_square_row, 1)
        self.assertEqual(move.starting_square_col, 1)
        self.assertIsInstance(move.moving_piece, Pawn)
        self.assertFalse(move.in_check)
        self.assertEqual(move.ending_square_row, 2)
        self.assertEqual(move.ending_square_col, 1)
        self.assertEqual(move.removed_piece, Player.EMPTY)
        self.assertFalse(move.castled)
        self.assertIsNone(move.rook_starting_square)
        self.assertIsNone(move.rook_ending_square)
        self.assertIsNone(move.moving_rook)
        self.assertFalse(move.pawn_promoted)
        self.assertIsNone(move.replacement_piece)
        self.assertFalse(move.en_passaned)
        self.assertIsNone(move.en_passant_eaten_piece)
        self.assertIsNone(move.en_passant_eaten_square)

    def test_castling_move(self):
        # Create a game state with a king and rook for castling
        initial_board = [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, King('k', 0, 3, Player.PLAYER_1), Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Rook('r', 0, 0, Player.PLAYER_1), Player.EMPTY]
        ]
        initial_game_state = game_state()
        initial_game_state.board = initial_board

        # Create a chess move for castling
        move = chess_move((0, 3), (0, 1), initial_game_state, False)
        move.castling_move((0, 0), (0, 2), initial_game_state)

        # Assert the attributes of the chess move after castling
        self.assertTrue(move.castled)
        self.assertEqual(move.rook_starting_square, (0, 0))
        self.assertEqual(move.rook_ending_square, (0, 2))

    def test_pawn_promotion_move(self):
        # Create a game state with a pawn reaching the promotion square
        initial_board = [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Pawn('p', 6, 3, Player.PLAYER_1), Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY]
        ]
        initial_game_state = game_state()
        initial_game_state.board = initial_board

        # Ensure that the starting square is within the bounds of the game board
        starting_square = (1, 2)  # Choose a valid starting square
        move = chess_move(starting_square, (2, 2), initial_game_state, False)
        move.pawn_promotion_move(Queen('q', 7, 3, Player.PLAYER_1))

        # Assert the attributes of the chess move after pawn promotion
        self.assertTrue(move.pawn_promoted)
        self.assertIsInstance(move.replacement_piece, Queen)

    def test_en_passant_move(self):
        # Create a game state with a pawn and an opponent's pawn for en passant
        initial_board = [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Pawn('p', 2, 2, Player.PLAYER_1), Player.EMPTY],
            [Player.EMPTY, Pawn('p', 3, 1, Player.PLAYER_2), Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY]
        ]
        initial_game_state = game_state()
        initial_game_state.board = initial_board

        # Create a chess move for en passant
        move = chess_move((3, 1), (2, 2), initial_game_state, False)
        move.en_passant_move(Pawn('p', 2, 2, Player.PLAYER_1), (2, 2))

        # Assert the attributes of the chess move after en passant
        self.assertTrue(move.en_passaned)
        self.assertIsInstance(move.en_passant_eaten_piece, Pawn)
        self.assertEqual(move.en_passant_eaten_square, (2, 2))


if __name__ == '__main__':
    unittest.main()
