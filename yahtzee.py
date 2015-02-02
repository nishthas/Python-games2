"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set=temp_set   
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    scor=[0,0,0,0,0,0]
    for item in hand:
        if item==1:
            scor[0]+=1
        if item==2:
            scor[1]+=2
        if item==3:
            scor[2]+=3
        if item==4:
            scor[3]+=4
        if item==5:
            scor[4]+=5
        if item==6:
            scor[5]+=6
    return max(scor)



def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    total=0.0
    scory=[]
    newdic=gen_all_sequences(range(1,num_die_sides+1), num_free_dice)
    for item in newdic:
        handy=[]
        handy=list(held_dice)+list(item)
        num=score(handy)
        scory.append(num)
        total+=num
    return total/len(newdic)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])
    for item in list(hand):
        temp_set = set()
        for partial_sequence in answer_set:
            for bnr in [0, 1]:
                if bnr:
                    
                    temp_set.add(tuple(partial_sequence))
                else:
                    new_sequence=list(partial_sequence)
                    new_sequence.append(item)
                   
                    temp_set.add(tuple(new_sequence))
        answer_set=temp_set   
    return answer_set

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    allho=gen_all_holds(hand)
    maxv=0.0
    tup=()
    for item in allho:
        new=expected_value(item, num_die_sides, len(hand)-len(item))
        if new>maxv:
            maxv=new
            tup=item
        
    
    
    return (maxv, tup)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()

#import user35_oGFuhcPNLh_0 as score_testsuite
#score_testsuite.run_suite(score)
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
#import user35_mGREPnDxbs_0 as strategy_testsuite
#strategy_testsuite.run_suite(strategy)                                       
#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#expected_value_testsuite.run_suite(expected_value)    
#import user35_U2vQEq960r_0 as tests
#tests.test_expected_value(expected_value)
#tests.test_strategy(strategy)     


