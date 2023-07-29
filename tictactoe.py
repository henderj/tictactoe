from enum import Enum
import random
import os
import time

welcomeMessage = "Welcome to the Himalayas! I'll cut right to the chase. To escape your imminent doom,\nyou must win a game of tictactoe against a mysterious snow spirit named Mahana. Good luck!"
yesAnswers = ["y", "Y", "yes", "YES", "Yes"]
noAnswers = ["n", "N", "no", "NO", "No"]


class GameState(Enum):
    RUNNING = 0
    PLAYER_WON = 1
    COMPUTER_WON = 2
    TIE = 3


def doGame() -> bool:
    clearConsole()
    delayed_print(welcomeMessage)
    delayed_print("Mahana shows you mercy and lets you choose if you want to go first.")
    answer = input("Do you want to go first? (y/n)\n")
    while (answer not in yesAnswers) and (answer not in noAnswers):
        print(
            "Mahana does not understand complex human language. Simply reply y (yes) or n (no)"
        )
        answer = input("Do you want to go first? (y/n)\n")
    playersTurn = answer in yesAnswers

    if playersTurn:
        delayed_print(
            "Mahana is impressed with your assertive nature. Prepare to battle..."
        )
    else:
        delayed_print("Mahana appreciates your respect. Prepare to battle...")

    gameState = GameState.RUNNING
    gridState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while gameState == GameState.RUNNING:
        gameState, gridState = gameLoop(playersTurn, gridState)
        playersTurn = not playersTurn

    clearConsole()
    displayGridState(gridState)
    if gameState == GameState.PLAYER_WON:
        delayed_print(
            "You won! Mahana is impressed and grants you passage safely home."
        )
    elif gameState == GameState.COMPUTER_WON:
        delayed_print("Mahana won! He is not impressed with your skills.")
    else:
        delayed_print("It's a tie! Mahana wants to play again.")

    delayed_print("Do you dare challenge Mahana again?")
    answer = input("Do you want to play again? (y/n)\n")
    while (answer not in yesAnswers) and (answer not in noAnswers):
        delayed_print(
            "Mahana does not understand complex human language. Simply reply y (yes) or n (no)"
        )
        answer = input("Do you want to play again? (y/n)\n")
    playAgain = answer in yesAnswers
    return playAgain


def gameLoop(playersTurn: bool, gridState: list[int]) -> tuple[GameState, list[int]]:
    clearConsole()
    displayGridState(gridState)
    if playersTurn:
        gridState = doPlayerInput(gridState)
    else:
        gridState = doComputerInput(gridState)
    gameState = checkForWins(gridState, playersTurn)
    if gameState == GameState.RUNNING:
        gameState = checkForTie(gridState)
    return gameState, gridState


def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")


def doPlayerInput(gridState: list[int]) -> list[int]:
    playerInput = getValidPlayerInput(gridState)
    gridState[playerInput] = 1
    return gridState


def getValidPlayerInput(gridState: list[int]) -> int:
    delayed_print("You're turn. Where do you want to play?")
    while True:
        answer = input("Enter a number 1-9\n")
        while not answer.isdigit() or int(answer) > len(gridState) or int(answer) <= 0:
            print(
                "Mahana does not know what you mean. Please enter a number between 1 and 9."
            )
            answer = input("Enter a number 1-9\n")
        answerNum = int(answer) - 1
        if gridState[answerNum] == 0:
            return answerNum
        print("That position is already taken!")


def doComputerInput(gridState: list[int]) -> list[int]:
    availableIndexes = []
    for index, value in enumerate(gridState):
        if value == 0:
            availableIndexes.append(index)
    index = checkForPotentialWinsForComputer(gridState, availableIndexes)
    if index == -1:
        index = checkForPotentialWinsForPlayer(gridState, availableIndexes)
    if index == -1:
        index = availableIndexes[random.randrange(0, len(availableIndexes))]
    delayed_print("Mahana chooses position " + str(index + 1))
    time.sleep(0.5)
    gridState[index] = 2
    return gridState


def checkForPotentialWinsForComputer(
    gridState: list[int], availableIndexes: list[int]
) -> int:
    for value in availableIndexes:
        copy = gridState.copy()
        copy[value] = 2
        if checkForWins(copy, False) == GameState.COMPUTER_WON:
            return value
    return -1


def checkForPotentialWinsForPlayer(
    gridState: list[int], availableIndexes: list[int]
) -> int:
    for value in availableIndexes:
        copy = gridState.copy()
        copy[value] = 1
        if checkForWins(copy, True) == GameState.PLAYER_WON:
            return value
    return -1


def checkForWins(gridState: list[int], playersTurn: bool) -> GameState:
    winningNum = (
        1 if playersTurn else 2
    )  # only the current player can win, no need to check the other player
    # brute force check all win states
    # rows
    if (
        all(ele == winningNum for ele in gridState[0:3])  # first row
        or all(ele == winningNum for ele in gridState[3:6])  # second row
        or all(ele == winningNum for ele in gridState[6:9])  # third row
        or all(ele == winningNum for ele in gridState[0:9:3])  # first column
        or all(ele == winningNum for ele in gridState[1:9:3])  # second column
        or all(ele == winningNum for ele in gridState[2:9:3])  # thrid column
        or all(
            ele == winningNum for ele in gridState[0:9:4]
        )  # top left to bottom right
        or all(
            ele == winningNum for ele in gridState[2:7:2]
        )  # top right to bottom left
    ):
        return GameState(winningNum)

    return GameState.RUNNING


def checkForTie(gridState: list[int]) -> GameState:
    isTie = all(ele != 0 for ele in gridState)
    return GameState.TIE if isTie else GameState.RUNNING


def displayGridState(gridState: list[int]) -> None:
    stringGrid = ["-" if ele == 0 else "X" if ele == 1 else "O" for ele in gridState]
    delayed_print(
        " ".join(ele for ele in stringGrid[0:3])
        + "\n"
        + " ".join(ele for ele in stringGrid[3:6])
        + "\n"
        + " ".join(ele for ele in stringGrid[6:9])
    )


def delayed_print(
    msg: str,
    delay: float = 0.02,
    pauseAtPunctuation: bool = True,
    punctuationPause: float = 0.30,
    newLineAtEnd: bool = True,
) -> None:
    for char in msg:
        print(char, end="", flush=True)
        if pauseAtPunctuation and char in [".", "!", "?", ","]:
            time.sleep(punctuationPause)
        else:
            time.sleep(delay)
    if newLineAtEnd:
        print("\n", end="", flush=True)


if __name__ == "__main__":
    playAgain = doGame()
    while playAgain:
        playAgain = doGame()
    delayed_print("Mahana thanks you for your time. Until next time.")
    input("(press enter to quit)")
