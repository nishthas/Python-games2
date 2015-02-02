"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided
import codeskulptor
codeskulptor.set_timeout(20)

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 30    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board,player):
    """
    vh
    """
    emp=board.get_empty_squares()
    while(board.check_win()==None):
        rand=random.choice(emp)
        row1=rand[0]
        col1=rand[1]
        board.move(row1,col1,player)
        player=provided.switch_player(player)
        emp=board.get_empty_squares()
    
    
def mc_update_scores(scores, board, player):
    """
    score update
    """
    won=board.check_win()
    rang=board.get_dim()
    if won==provided.DRAW:
         for row in range(rang):
            for col in range(rang):
                scores[row][col] +=0
    else:
        for row in range(rang):
            for col in range(rang):
                status = board.square(row, col)
                if status==provided.EMPTY:
                    pass
                elif status == player and won == player:
                    scores[row][col] += MCMATCH
                elif status != player and won == player:
                    scores[row][col] -= MCOTHER
                elif status == player and won != player:
                    scores[row][col] -= MCMATCH
                elif status != player and won != player:
                    scores[row][col] += MCOTHER 

def get_best_move(board, scores):
    """
    move
    """
    rang=board.get_dim()
    maxscore=[]
    emp=board.get_empty_squares()
    for row in range(rang):
        for col in range(rang):
            cord=(row,col)
            if cord in emp:
                maxval=scores[row][col]
                if (len(maxscore))==0:
                    maxscore.append((row,col))
                    item=maxval
                
                elif maxval==item:
                    maxscore.append((row,col))
                
                elif maxval>item:
                    maxscore=[(row,col)]
                    item=scores[row][col]
                
    return random.choice(maxscore)

def mc_move(board, player, trials):
    """
    final
    """
    scorey=[ [0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_num in range(trials):
        boardc=board.clone()
        mc_trial(boardc,player)
        mc_update_scores(scorey, boardc, player)
    return get_best_move(board, scorey)
    

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
