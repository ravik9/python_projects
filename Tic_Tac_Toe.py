# first create a list of 10 spaces and show
print('GET ready to Play TIC-TAC-TOE Dual player')
value = [''] * 10
value[0] = 1


class Player:
    def __init__(self, marker, wins):
        self.marker = marker
        self.wins = wins

    def win(self):
        self.wins += 1


def display():
    print('Tic-Tac-Toe')
    print(value[1] + ' | ' + value[2] + ' | ' + value[3])
    print('------')
    print(value[4] + ' | ' + value[5] + ' | ' + value[6])
    print('------')
    print(value[7] + ' | ' + value[8] + ' | ' + value[9])


marker_validation = True
winner_validation = True
Playing = True
while marker_validation:
    marker = input('Player1 please choose X or O to play')
    if marker == 'X' or 'x' or 'o' or 'O':
        if marker == 'X' or 'x':
            Player1 = Player('X', 0)
            Player2 = Player('O', 0)
        else:
            Player1 = Player('O', 0)
            Player2 = Player('X', 0)
        marker_validation = False
    else:
        print('Please enter a valid marker "X" or "O" to continue')


# check for win after every entry
def win_check(play):
    if (value[1] == value[2] == value[3] == play.marker) or (value[4] == value[5] == value[6] == play.marker) or (
            value[7] == value[8] == value[9] == play.marker):
        return True
    elif (value[1] == value[4] == value[7] == play.marker) or (value[2] == value[5] == value[8] == play.marker) or (
            value[3] == value[6] == value[9] == play.marker):
        play.win()
        return True
    elif (value[1] == value[5] == value[9] == play.marker) or (value[3] == value[5] == value[7] == play.marker):
        play.win()
        return True
    else:
        return False


def ContPlaying():
    while True:
        cont = input('Do u want to continue playing [y]/n')
        if cont == 'y' or 'y' or 'n' or 'N':
            if cont == 'Y' or 'y':
                value[1:10] = [''] * 9
                print('Scores of Player1 is ' + str(Player1.wins) + ' and Player2 is ' + str(Player2.wins))
                break
            else:
                print('Final scores of Player1 is ' + str(Player1.wins) + ' and Player2 is ' + str(Player2.wins))
                Playing = False
        else:
            print('Enter a valid option y/n')


# take inputs from the players till some one wins or draws
while Playing:
    display()
    if '' in value:
        position_validation1 = True
        position_validation2 = True
        while position_validation1:
            try:
                position = int(input('Player1 please choose a value from 1 to 9 to play'))
                if position in range(1, 10):
                    # write some logic
                    if value[position] == '':
                        value[position] = Player1.marker
                        position_validation1 = False
                        display()
                        win_c = win_check(Player1)
                        if win_c:
                            print('Player1 has won the game')
                            ContPlaying()
                    else:
                        print('Please choose a position which is free')
                else:
                    print('PLease enter only values from 1 to 9')
            except:
                print('Player1 please enter a valid number')

        while position_validation2:
            try:
                position = int(input('Player2 please choose a value from 1 to 9 to play'))
                if position in range(1, 10):
                    # write some logic
                    if value[position] == '':
                        value[position] = Player2.marker
                        position_validation2 = False
                        win_c = win_check(Player2)
                        if win_c:
                            print('Player2 has won the game')
                            ContPlaying()
                        display()
                    else:
                        print('Please choose a position which is free')
                else:
                    print('PLease enter only values from 1 to 9')
            except:
                print('Player2 please enter a valid number through 1-9 only')
    else:
        print('Match draws')
        ContPlaying()
