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
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    dice_set = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    max_num = 0
    if hand != ():
      for dummy_num in hand:
        dice_set[dummy_num - 1] += dummy_num
      max_num = max(dice_set)   
        
    return max_num 


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """    
    outcomes = set([])
    for dummy_i in range(1,num_die_sides+1):
        outcomes.add(dummy_i)

    score_roll = 0.0
    set_after_roll_all = gen_all_sequences(outcomes, num_free_dice)
    for dummy_dice in set_after_roll_all:
        final_dice = dummy_dice + held_dice 
        score_roll += score(final_dice) * 1.0/ len(set_after_roll_all)
    

    return score_roll


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    result = set([()])
    outcomes = set([0,1])
    answer_set = gen_all_sequences(outcomes, len(hand))
    for item in answer_set:
        new_sequence = list()
        for dummy_ind in range(0,len(item)):
            if item[dummy_ind]:          
                new_sequence.append(hand[dummy_ind])
                result.add(tuple(new_sequence))
            
    return result


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    #print "hand is:", hand
    #print "numof die sides:", num_die_sides
    #print "test:", gen_all_holds(hand)
    value_int = 0
    for item in gen_all_holds(hand):
        value = expected_value(item, num_die_sides, len(hand) - len(item))
        if value > value_int:
            value_int = value
            hold_item = item    
    
    #return (0.0, ())
    #print value_int, hold_item
    return (value_int,hold_item)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
#import user35_oGFuhcPNLh_0 as score_testsuite
#score_testsuite.run_suite(score)    
#    
#import user35_uLOFnLQSJV29rFh_5 as expected_value_testsuite
#expected_value_testsuite.run_suite(expected_value)   
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)

#import user35_mGREPnDxbs_0 as strategy_testsuite
#strategy_testsuite.run_suite(strategy)