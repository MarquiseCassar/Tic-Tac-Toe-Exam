
_author_ = 'Marquise Cassar'

import sys
import random
import time
from PyQt5 import QtGui, QtCore

class Tic(QtGui.QMainWindow):

    def __init__(self):
        super(Tic,self).__init__()
        self.setGeometry(50,50,360,400)
        self.setWindowTitle('Tic Tac Toe')
        self.setWindowIcon(QtGui.QIcon('favicon.png'))

        self.winner = ''
        self.board()
        self.new_game()

    def board(self):

        newAction = QtGui.QAction('&New game', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setShortcutTip('Make a new game')
        newAction.triggered.connect(self.new_game)

        # add an exit feature
        exitAction = QtGui.QAction('&Leave', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close_application)

        self.statusBar()

        # menu part of exit feature
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        # new game feature
        fileMenu.addAction(newAction)

        # exit
        fileMenu.addAction(exitAction)

        # set up game board
        self.btn0 = QtGui.QPushButton('', self) # first argument is the text
        self.btn0.clicked.connect(lambda: self.clicked(1, self.playerCoin))
        self.btn0.resize(100,100)
        self.btn0.move(20,280)

        self.btn1 = QtGui.QPushButton('', self)
        self.btn1.clicked.connect(lambda: self.clicked(2, self.playerCoin))
        self.btn1.resize(100,100)
        self.btn1.move(240,280)

        self.btn2 = QtGui.PushButton('', self)
        self.btn2.clicked.connect(lambda: self.clicked(2, self.playerCoin))
        self.btn2.resize(100,100)
        self.btn2.move(240,280)

        self.btn3 = QtGui.QPushButton('', self)
        self.btn3.clicked.connect(lambda: self.clicked(3, self.playerCoin))
        self.btn3.resize(100,100)
        self.btn3.move(20,170)

        self.btn4 = QtGui.QPushButton('', self)
        self.btn4.clicked.connect(lambda: self.clicked(4, self.playerCoin))
        self.btn4.resize(100,100)
        self.btn4.move(130,170)

        self.btn5 = QtGui.QPushButton('', self)
        self.btn5.clicked.connect(lambda: self.clicked(5, self.playerCoin))
        self.btn5.resize(100,100)
        self.btn5.move(240,170)

        self.btn6 = QtGui.QPushButton('', self)
        self.btn6.clicked.connect(lambda: self.clicked(6, self.PlayerCoin))
        self.btn6.resize(100,100)
        self.btn6.move(20,60)

        self.btn7 = QtGui.QPushButton('', self)
        self.btn7.clicked.connect(lambda: self. clicked(7, self.playerCoin))
        self.btn7.resize(100,100)
        self.btn7.move(130,60)

        self.btn8 = QtGui.QPushButton('', self)
        self.btn8.clicked.connect(lambda: self.clicked(8, self.playerCoin))
        self.btn8.resize(100,100)
        self.btn8.move(240,60)

        # list of taken move positions
        self.taken = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.takenBy = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.btnDict = { 0 : lambda x : (self.btn0.setText(x), self.btn0.setFont(QtGui.QFont('Times', 60))),
                1 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                2 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                3 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                4 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                5 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                6 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                7 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                8 : lambda x : (self.btn1.setText(x), self.btn1.setFont(QtGui.QFont('Times', 60))),
                    }
        # this should always be last
        self.show()

    def clicked(self, btnval, player):
        if self.taken[btnval] ==0:
            # update free moves & the screen
            self.btnDict[btnval](player)
            self.taken[btnval] = 1
            # update who-owns-what to check if there's a winner
            if player == 'X':
                self.takenBy[btnval] = 'X'
            else:
                self.takenBy[btnval] = 'O'
            print = self.takenBy
            self.test_for_winner()
            self.computer_move()
            self.show()
        else:
            pass

    def new_game(self):
        #This resets the board
        [self.btnDict[key]("") for key in self.btnDict]
        self.winner = ''


        item, ok = QtGui.QInputDialog.getItem(self, "Choose X or O",
                                              "Would you like to play as X or O?", ('X','O'), 0, False)
        if ok and item:
                self.playerCoin = item

                if self.playerCoin == 'X':
                    self.computerCoin = 'O'
                else:
                    self.computerCoin = 'X'

    def computer_move(self):
        # find moves the computer can make
        legal_moves = []
        for j in range(9):
            if self.taken[j] == 0:
                legal_moves.append(j)

            # for now, pick a random valid move
            btn = legal_moves[random.randint(0,len(legal_moves)-1)]

            # call the clicked method
            time.sleep(1)
            if self.taken[btn] == 0:
                # update free movs & the screen
                self.btnDict[btn](self.computerCoin)
                self.taken[btn] = 1
                # update who-owns-what to check if there's a winner
                if self.computerCoin == 'X':
                    self.takenBy[btn] = 'X'
                else:
                    self.takenBy[btn] = 'O'
                print = self.takenBy
                self.test_for_winner()
                self.show()
            else:
                pass

    def test_for_winner(self):
            # enumerate possible winner configurations
            winning_configs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4,6]
            for j in range(8):
                if self.takenBY[winning_configs[j][0]] == 'X' and \
                   self.takenBy[winning_configs[j][1]] == 'X' and \
                   self.takenBy[winning_configs[j][2]] == 'X':
                    self.winner = 'X';
                if self.takenBy[winning_configs[j][0]] == 'O' and \
                   self.takenBy[winning_configs[j][1]] == 'O' and \
                   self.takenBy[winning_configs[j][2]] == 'O':
                    self.winner = 'O';

            # if there is a winner, report it and end the game
            if self.winner == 'X' or self.winner == '0':
                msg = '{} won the game! Would you like to play?'.format(self.winner)
                choice = QtGui.QMessageBox.question(self,'Game Over!', msg
                                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

                if choice == QtGui.QMessageBox.Yes:
                    self.close();
                    self.__init__();
                else:
                    sys.exit();

            # if there's a draw, handle it here
            if self.winner == '' and sum(self.taken)==9:
                msg = 'It was a draw!  Would you like to play again?';
                choice = QtGui.QMessageBox.question(self, 'Game Over!', msg,
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No);

                if choice == QtGui.QMessageBox.Yes:
                    self.close();
                    self.__init__();
                else:
                    pass
if _name_ =="_main_":
    QCoreApplication.setOrganizationName("Marquise software");
    QCoreApplication.setOrganizationDomain("Marquisesoftware.com");
    QCoreApplication.setApplicationName("Tic Tac Toe");
    if_appSettings.contains('createLogFile');
        createLogFile = appSettings.value('createLogFile');
    else
        logFilename = logFilenameDefault
        appSettings.setValue('logFile', logFilename)
    if createLogFile:
        startingFolderName = 'path'.dirname('path'.realpath('_file_'))
        if asppSettings.contains('logFile'):
            logFilename = 'appSettings'.value('logfile', type=str)
        else:
            logFilename = 'logFilenameDefault'
            appSettings.setValue('logFile', logFilename)
        basicConfig(filename = path.join(startingFolderName, logFilename), level=DEBUG, format='%(asctime)s %(name)&s %(levelname)-












