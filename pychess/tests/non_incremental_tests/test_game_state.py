import unittest
from unittest import mock

from enums import Player
from chess_engine import game_state
from piece import Piece
from queen import Queen


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
        # (update the board accordingly)

        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 0)

    def test_checkmate_stalemate_checker_checkmate_black(self):
        # Set up a checkmate scenario for black
        # (update the board accordingly)

        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 1)

    def test_checkmate_stalemate_checker_stalemate(self):
        # Set up a stalemate scenario
        # (update the board accordingly)

        result = self.game_state.checkmate_stalemate_checker()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
