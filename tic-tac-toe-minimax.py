"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    plax=[]
    play=[]
    if board.check_win()!=None:
        return SCORES[board.check_win()],(-1,-1)
    else:
        emp=board.get_empty_squares()
        for squ in emp:
            boa=board.clone()
            boa.move(squ[0],squ[1],player)
            pla=provided.switch_player(player)
            val=mm_move(boa,pla)
            #print val[0]
            if player == provided.PLAYERX:
                plax.append((val[0],squ))
            else:
                play.append((val[0],squ))
        if player == provided.PLAYERX:
                maxx= max(plax)
                return maxx
        else:
                maxy= min(play)
                return maxy
          

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]
#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
#print mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERO, provided.PLAYERX], [provided.EMPTY, provided.PLAYERO, provided.EMPTY], [provided.PLAYERX, provided.EMPTY, provided.PLAYERX]]), provided.PLAYERX)
#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)score, position =  mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERX)
#import user36_AQLww3W1YBS5oCt as unit_test
#unit_test.test_mm_move(mm_move)