#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[3]:


def player_input():
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input('Player1: choose X or O:').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


# In[4]:


player1_marker , player2_marker = player_input()


# In[5]:


def place_marker(board, marker, position):
    board[position] = marker


# In[6]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[7]:


def win_check(board, mark):
    return((board[7]==mark and board[8]== mark and board[9] or board[4]==mark and board[5]==mark and board[6]==mark
            or board[1]==mark and board[2]==mark and board[3]==mark or 
            board[7]== board[4]== board[1]==mark or board[8]== board[5]== board[2]==mark or
            board[9]== board[6]== board[3]==mark or board[7]== board[5]== board[3]==mark or
            board[9]== board[5]== board[1]==mark))


# In[8]:


import random
def choose_first():
     
        flip = random.randint(0,1)
        if (flip == 0):
            return 'Player1'
        else:
            return 'Player2'


# In[9]:


def space_check(board,position):
    return board[position] == ' '


# In[10]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[11]:


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9)"))
    return position


# In[12]:


def replay():
    choice = input("Play again : Yes or No")
    return choice == 'Yes'


# In[ ]:


#While loop to keep running the game
print('Welcome to Tic-Tac-Toe')
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game = input('Ready to play: y or n')
    if play_game == 'y':
        game_on = True
    else:
        game_on == False
    while game_on:
                    if turn == 'Player1':
                                          #Show the board
                                            display_board(the_board)
                                           #Choose a position
                                            position = player_choice(the_board)
                                           #Place the marker on the position
                                            place_marker(the_board,player1_marker,position)
                                           #Check if they won
                                            if win_check(the_board,player1_marker): 
                                                                               display_board(the_board)
                                                                               print('PLAYER1 HAS WON!!')
                                                                               game_on = False
                                            else:
                                                if full_board_check(the_board):
                                                                               display_board(the_board)
                                                                               print('TIE GAME!!')
                                                                               game_on = False
                                                else:
                                                      turn = 'Player2'
                    else: 
                               #Show the board
                                display_board(the_board)
                               #Choose a position
                                position = player_choice(the_board)
                               #Place the marker on the position
                                place_marker(the_board,player2_marker,position)
                               #Check if they won
                                if win_check(the_board,player2_marker):
                                                                     display_board(the_board)
                                                                     print('PLAYER2 HAS WON!!')
                                                                     game_on = False
                                else:
                                                            if full_board_check(the_board):
                                                                        display_board(the_board)
                                                                        print('TIE GAME!!')
                                                                        game_on = False
                                                            else:
                                                                   turn = 'Player1'
if not replay():
                    break
    #BREAK OUT OF WHILE LOOP ON replay()
        


# In[ ]:




