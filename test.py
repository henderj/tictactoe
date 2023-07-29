import unittest
import tictactoe


class TestGameMethods(unittest.TestCase):
    def test_tie(self):
        gameState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = tictactoe.GameState.RUNNING
        actual = tictactoe.checkForTie(gameState)
        self.assertEqual(actual, expected)

        gameState = [1, 0, 1, 2, 2, 0, 1, 0, 0]
        expected = tictactoe.GameState.RUNNING
        actual = tictactoe.checkForTie(gameState)
        self.assertEqual(actual, expected)

        gameState = [1, 1, 2, 2, 1, 1, 1, 2, 2]
        expected = tictactoe.GameState.TIE
        actual = tictactoe.checkForTie(gameState)
        self.assertEqual(actual, expected)
    
    def test_checkForWins(self):
        gameState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = tictactoe.GameState.RUNNING
        actual = tictactoe.checkForWins(gameState, True)
        self.assertEqual(actual, expected)

        gameState = [0,0,0,
                     1,1,1,
                     2,0,2]
        expected = tictactoe.GameState.PLAYER_WON
        actual = tictactoe.checkForWins(gameState, True)
        self.assertEqual(actual, expected)

        gameState = [0,1,2,
                     1,1,2,
                     2,0,2]
        expected = tictactoe.GameState.COMPUTER_WON
        actual = tictactoe.checkForWins(gameState, False)
        self.assertEqual(actual, expected)

        gameState = [0,1,2,
                     1,1,2,
                     2,1,0]
        expected = tictactoe.GameState.PLAYER_WON
        actual = tictactoe.checkForWins(gameState, True)
        self.assertEqual(actual, expected)

        gameState = [0,1,2,
                     1,2,2,
                     2,1,0]
        expected = tictactoe.GameState.COMPUTER_WON
        actual = tictactoe.checkForWins(gameState, False)
        self.assertEqual(actual, expected)

    def test_checkForComputerWins(self):
        gameState = [0,1,2,
                     2,0,1,
                     0,0,0]
        expected = -1
        actual = tictactoe.checkForPotentialWinsForComputer(gameState, [0,4,6,7,8])
        self.assertEqual(actual, expected)

        gameState = [0,0,0,
                     1,2,1,
                     0,2,0]
        expected = 1
        actual = tictactoe.checkForPotentialWinsForComputer(gameState, [0,1,2,6,8])
        self.assertEqual(actual, expected)
    
    def test_checkForComputerWins(self):
        gameState = [0,1,2,
                     2,0,1,
                     0,0,0]
        expected = -1
        actual = tictactoe.checkForPotentialWinsForPlayer(gameState, [0,4,6,7,8])
        self.assertEqual(actual, expected)

        gameState = [0,0,0,
                     1,0,1,
                     0,2,0]
        expected = 4
        actual = tictactoe.checkForPotentialWinsForPlayer(gameState, [0,1,2,4,6,8])
        self.assertEqual(actual, expected)
        

if __name__ == "__main__":
    unittest.main()
