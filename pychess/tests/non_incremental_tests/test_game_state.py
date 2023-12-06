import unittest
from unittest import mock

from enums import Player
from chess_engine import game_state
from piece import Piece
from queen import Queen
from pawn import Pawn
from rook import Rook
from king import King
from knight import Knight
from bishop import Bishop


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.game_state = game_state()

    def test_get_piece(self):
        # Test getting a piece at a valid position
        piece = self.game_state.get_piece(0, 0)
        self.assertIsInstance(piece, Piece)

        # Test getting a piece at an invalid position
        piece = self.game_state.get_piece(8, 8)
        self.assertIsNone(piece)

    def test_is_valid_piece(self):
        # Test checking validity of a piece at a valid position
        valid = self.game_state.is_valid_piece(0, 0)
        self.assertTrue(valid)

        # Test checking validity of a piece at an invalid position
        valid = self.game_state.is_valid_piece(8, 8)
        self.assertFalse(valid)

    def test_get_valid_moves(self):
        # Test getting valid moves for a piece
        moves = self.game_state.get_valid_moves((1, 0))
        expected_moves = [(2, 0), (3, 0)]
        self.assertEqual(moves, expected_moves)

        # Test getting valid moves for an empty square
        moves = self.game_state.get_valid_moves((2, 0))
        self.assertIsNone(moves)

    def test_checkmate_stalemate_checker(self):
        # Test for no checkmate or stalemate
        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 3)

    def test_king_can_castle_left(self):
        # Test king can castle left for both players
        white_can_castle = self.game_state.king_can_castle_left(Player.PLAYER_1)
        black_can_castle = self.game_state.king_can_castle_left(Player.PLAYER_2)

        self.assertFalse(white_can_castle)
        self.assertFalse(black_can_castle)

    def test_king_can_castle_right(self):
        # Test king can castle right for both players
        white_can_castle = self.game_state.king_can_castle_right(Player.PLAYER_1)
        black_can_castle = self.game_state.king_can_castle_right(Player.PLAYER_2)

        self.assertFalse(white_can_castle)
        self.assertFalse(black_can_castle)

    def test_promote_pawn_valid_input(self):
        # Set up the initial game state with a pawn that can be promoted
        # (update the board accordingly)

        # Mock user input to choose a valid piece for promotion
        with mock.patch('builtins.input', return_value='q'):
            self.game_state.promote_pawn((1, 0), self.game_state.get_piece(1, 0), (0, 0))

        # Check that the pawn was successfully promoted to a queen
        promoted_piece = self.game_state.get_piece(0, 0)
        self.assertIsInstance(promoted_piece, Queen)
        self.assertEqual(promoted_piece.get_player(), Player.PLAYER_1)

    def test_promote_pawn_invalid_input_then_valid_input(self):
        # Set up the initial game state with a pawn that can be promoted
        # (update the board accordingly)

        # Mock user input to choose an invalid piece first and then a valid piece
        with mock.patch('builtins.input', side_effect=['k', 'q']):
            self.game_state.promote_pawn((6, 0), self.game_state.get_piece(6, 0), (7, 0))

        # Check that the pawn was successfully promoted to a queen
        promoted_piece = self.game_state.get_piece(7, 0)
        self.assertIsInstance(promoted_piece, Queen)
        self.assertEqual(promoted_piece.get_player(), Player.PLAYER_2)

    def test_checkmate_stalemate_checker_no_check(self):
        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 3)

    def test_checkmate_stalemate_checker_checkmate_white(self):
        # Set up a checkmate scenario for white
        # Customize the board to represent a checkmate scenario for white

        # Initialize White pieces
        white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)  # White king is in checkmate
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
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
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_king = King('k', 7, 3, Player.PLAYER_2)
        black_queen = Queen('q', 7, 4, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)

        # Black Queen delivers checkmate to White King
        black_queen_attack_positions = [(0, 3), (1, 3), (2, 3)]
        for position in black_queen_attack_positions:
            self.game_state.board[position[0]][position[1]] = black_queen

        self.game_state.board = [
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
            [black_rook_1, black_knight_1, black_bishop_1, black_king, Player.EMPTY, black_bishop_2, black_knight_2,
             black_rook_2]
        ]

        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 0)

    def test_checkmate_stalemate_checker_checkmate_black(self):
        # Set up a checkmate scenario for black
        # Customize the board to represent a checkmate scenario for black

        # Initialize White pieces
        white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
        white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
        white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
        white_king = King('k', 0, 3, Player.PLAYER_1)
        white_queen = Queen('q', 0, 4, Player.PLAYER_1)
        white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
        white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
        white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
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
        black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
        black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
        black_king = King('k', 7, 3, Player.PLAYER_2)  # Black king is in checkmate
        black_queen = Queen('q', 7, 4, Player.PLAYER_2)
        black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
        black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
        black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
        black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
        black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
        black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
        black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
        black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
        black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
        black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
        black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)

        # White Queen delivers checkmate to Black King
        white_queen_attack_positions = [(7, 3), (6, 3), (5, 3)]
        for position in white_queen_attack_positions:
            self.game_state.board[position[0]][position[1]] = white_queen

        self.game_state.board = [
            [white_rook_1, white_knight_1, white_bishop_1, white_king, Player.EMPTY, white_bishop_2, white_knight_2,
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

        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 1)

    def test_checkmate_stalemate_checker_stalemate(self):
        # Set up a stalemate scenario
        # For example, remove all major pieces (except kings) from the board
        self.game_state.board = [
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
            [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY],
        ]

        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
