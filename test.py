import unittest
import main


class TestGameMethods(unittest.TestCase):
    def test_tie(self):
        gameState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = main.GameState.RUNNING
        actual = main.checkForTie(gameState)
        self.assertEqual(actual, expected)

        gameState = [1, 0, 1, 2, 2, 0, 1, 0, 0]
        expected = main.GameState.RUNNING
        actual = main.checkForTie(gameState)
        self.assertEqual(actual, expected)

        gameState = [1, 1, 2, 2, 1, 1, 1, 2, 2]
        expected = main.GameState.TIE
        actual = main.checkForTie(gameState)
        self.assertEqual(actual, expected)
    
    def test_checkForWins(self):
        gameState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = main.GameState.RUNNING
        actual = main.checkForWins(gameState, True)
        self.assertEqual(actual, expected)

        gameState = [0,0,0,
                     1,1,1,
                     2,0,2]
        expected = main.GameState.PLAYER_WON
        actual = main.checkForWins(gameState, True)
        self.assertEqual(actual, expected)

        gameState = [0,1,2,
                     1,1,2,
                     2,0,2]
        expected = main.GameState.COMPUTER_WON
        actual = main.checkForWins(gameState, False)
        self.assertEqual(actual, expected)

        gameState = [0,1,2,
                     1,1,2,
                     2,1,0]
        expected = main.GameState.PLAYER_WON
        actual = main.checkForWins(gameState, True)
        self.assertEqual(actual, expected)

        gameState = [0,1,2,
                     1,2,2,
                     2,1,0]
        expected = main.GameState.COMPUTER_WON
        actual = main.checkForWins(gameState, False)
        self.assertEqual(actual, expected)

    def test_checkForComputerWins(self):
        gameState = [0,1,2,
                     2,0,1,
                     0,0,0]
        expected = -1
        actual = main.checkForPotentialWinsForComputer(gameState, [0,4,6,7,8])
        self.assertEqual(actual, expected)

        gameState = [0,0,0,
                     1,2,1,
                     0,2,0]
        expected = 1
        actual = main.checkForPotentialWinsForComputer(gameState, [0,1,2,6,8])
        self.assertEqual(actual, expected)
    
    def test_checkForComputerWins(self):
        gameState = [0,1,2,
                     2,0,1,
                     0,0,0]
        expected = -1
        actual = main.checkForPotentialWinsForPlayer(gameState, [0,4,6,7,8])
        self.assertEqual(actual, expected)

        gameState = [0,0,0,
                     1,0,1,
                     0,2,0]
        expected = 4
        actual = main.checkForPotentialWinsForPlayer(gameState, [0,1,2,4,6,8])
        self.assertEqual(actual, expected)
        

if __name__ == "__main__":
    unittest.main()
