from __future__ import generators
import copy
from collections import OrderedDict, deque
import numpy as np
import queue as Q
# try:
#     import Queue as Q
# except ImportError:
#     import queue as Q


'''
Sudoku Solver!

syntax:
    answer, method = sudoku_solver(#board)
       # answer = final board
       # method = either 'AC3' or 'BTS' (How the puzzle was solved)
       
ENJOY!!

'''

#################################################
# UTILITY FUNCTIONS
################################################

# Function to return list of all keys within 
# sudoku dict in the same row as 'key1'
def return_row(key1):
    output = []
    for key2 in sudoku:
        # If the first letter is not the same, continue
        if key2[0] != key1[0]: continue
        # If the key is the same as the input, continue
        if key1[1] == key2[1]: continue
        # If both conditions satisfied, append resulting key to output
        output.append(key2)
    # Return the output
    return output

# Function to return list of all keys within 
# sudoku dict in the same column as 'key1'
def return_col(key1):
    output = []
    for key2 in sudoku:
        # If the number is not the same, continue
        if key2[1] != key1[1]: continue
        # Then, if the letter is the same, continue
        if key2[0] == key1[0]: continue
        # if both conditions met, append to output
        output.append(key2)
    # Return the output
    return output

def return_box(key1):
    idx = [0, 0]              # Init top left coordinates of containing box
    output = []               # Output list of tiles within same box
    # Figure out which row
    if key1[0] in letters[0:3]: idx[0] = 0
    if key1[0] in letters[3:6]: idx[0] = 1
    if key1[0] in letters[6:9]: idx[0] = 2
    # Figure out which column
    if key1[1] in default[0:3]: idx[1] = 0
    if key1[1] in default[3:6]: idx[1] = 1
    if key1[1] in default[6:9]: idx[1] = 2
    # Convert sudoku dict keys to list
    x = list(sudoku)[ 27*idx[0]+3*idx[1] : 27*idx[0]+3*idx[1] + 21]
    # iter through and add keys to output
    for i in range(3): output.extend(x[i*9:i*9+3])
    if key1 in output: output.remove(key1)
    # Return output
    return output
   
# RETURNS ALL IMPLIED STATES, XJ, GIVEN XI
def return_implied(key1):
    output = []
    output.extend(return_col(key1))
    output.extend(return_row(key1))
    output.extend(return_box(key1))
    output = list(set(output))
    return output
   

# PRINT FIRST 5 ITEMS IN PRIORITY QUEUE
def print_priorityQ(q):
    holding = []
    for i in range(5):
        x = q.get()
        print (x.remaining, x.position, x.values)
        holding.append(x)
    for x in holding: q.put(x)


#####################################
# PUT INITIAL CONSTRAINTS IN CSP
#####################################
    
# ac3_solveable = True       # GLOBAL VARIABLE, WATCH OUT!!

def ac_3(sudoku):
    # print 'STARTING AC3 ALGO...'
    # for x in sudoku.items(): print x
    # global ac3_solveable
    # ac3_solveable = True
    # dequeue to hold pairs of arcs
    csp = deque()
    # explored set to keep track of previous arcs
    csp_explored = set()
    ### enter all starting arcs into csp dequeue
    # list of all states not auto assigned...
    active_states = [x for x in sudoku.keys() if len(sudoku.get(x)) != 1]
    for Xi in active_states:
        implied = return_implied(Xi)
        for Xj in implied:
            csp.append( (Xi, Xj) )
    # for x in csp: print x
    # Loop through queue of arcs
    # print 'starting csp length:\t{}'.format(len(csp))
    while len(csp) > 0:
        # Pop arc from queue and add to explored
        arc = csp.popleft()
        csp_explored.add(arc)
        # Check for consistency
        if revise(arc, sudoku):
            # print 'revision made'
            # List of arcs which are Xk --> Xi
            foo = [ x for x in csp_explored if x[1]==arc[0] ]
            # print 'foo:\t{}'.format(foo)
            # print 'foo:\t{}'.format(foo)
            for Xk_Xi in foo:
                # print 're-adding {} to csp dequeue'.format(Xk_Xi)
                # Remove relevant arcs from set
                csp_explored.remove(Xk_Xi)
                # Put them back in the queue
                csp.append(Xk_Xi)
        # print '\n:::::::'
        # print 'current board:'
        # for x in sudoku.items(): print x
        # time.sleep(1)
    # print 'ending csp length:\t{}'.format(len(csp))
    # print 'ending csp_explored length:\t{}'.format(len(csp_explored))
    # print 'ENDING AC3 ALGO...'
    # result = ac3_solveable
    return (sudoku)         
                
def revise(arc, sudoku):
    # Define variables as global
    # global ac3_solveable
    # Check if pair has consistency
    # Xi --> Xj
    Xi_c = sudoku.get( arc[0] )
    Xj_c = sudoku.get( arc[1] )
    # print '\nchecking {} and {}'.format(arc[0], arc[1])
    # time.sleep(1)
    # If more than one possible value
    # In Xj, then the arc is consistent
    if len(Xj_c) > 1:                       # If length of Xj is not 1, no revision
        return False            
    if len(Xj_c) == 0:                      # If len Xj is 0, no revision
        # ac3_solveable = False             # Cannot be solved
        return False
    if len(Xj_c) == 1:
        if Xj_c[0] in Xi_c:                 # else, if only one choice for Xj
            Xi_c.remove( Xj_c[0] )          # Remove value of Xj from Xi
            # sudoku[arc[0]] = Xi_c         # Set value in sudoku to new constraints
            return True
        return False
       
    return False
   
#############################
#############################
# BACK-TRACKING SEARCH      #
#############################
#############################

class CSP(object):
    def __init__(self, vars_list, domains, neighbors, constraints=None):
        self.vars = vars_list            # A list of variables; each is atomic (e.g. 'A1', 'A2', etc...).
        self.domains = domains           # A dict of {var:[possible_value, ...]} entries.
        self.neighbors = neighbors       # A dict of {var:[var,...]} that for each variable lists
        self.constraints = constraints   # ???
        self.curr_domains = None
        self.pruned = None
        self.nassigns=0
        
    def assign(self, var, val, assignment):
        self.nassigns += 1               # Increase assignment counter
        #if self.nassigns % 1000 == 0: print 'Assignments:\t{}'.format(self.nassigns)
        assignment[var] = val            # Adds value to assignment dict
            
    def unassign(self, var, assignment):
        if var in assignment: 
            del assignment[var]
 
 
def backtracking_search(csp, mcv=False, lcv=False, fc=False, mac=False):
    # Auto assign the starting states:
    assignment = {v:d[0] for v,d in csp.domains.items() if len(d)==1}
    # print 'Starting assignment:\n{}'.format(assignment)
    return recursive_backtracking( assignment, csp )

 
 
def recursive_backtracking(assignment, csp):
    # If complete, return the assignment
    if len(assignment) == len(csp.vars): return assignment     # Return the assignment if complete
    var_queue = return_var_queue(assignment, csp)              # Queue of possible values remaining given the setup
    # print_priorityQ(var_queue)                               # DEBUG PRINT
    node = var_queue.get()                                     # Choose the state with the fewest possible values
    if len(node.values) == 0: return None                      # If the node has no possible values, return None
    for val in node.values:                                    # Now iterate through values
        csp.assign(node.position, val, assignment)             # Try assigning said value
        result = recursive_backtracking(assignment, csp)       # recurse down tree
        if result is not None: return result                   # SOLUTION WAS FOUND.. PASS UP
        csp.unassign(node.position, assignment)                # If result is None, unassign the said variable
    return None
          
      
# Returns Priority Queue of states
# based on minimum remaining value heuristic
# CSP is a dict mapping all states to current values
def return_var_queue(assignment, csp):
    queue = Q.PriorityQueue()                                      # Initialize the priority queue to be returned
    # rel_vars = list( csp.keys() )                                # List of all keys
    # for x in assignment.keys(): rel_vars.remove(x)               # Remove keys that have already been assigned
    unassigned = [v for v in csp.vars if v not in assignment]
    for var in unassigned:
        # values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']   # List of possible values for a state to take
        values = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        # Xj = return_implied(var)                                   # Get list of all constraint implied values
        Xj = csp.neighbors.get(var, None)
        for x in Xj:                                             
            value = assignment.get(x, '0')
            if value in values: values.remove(value)               # remove the value held by x in Xj from possible values
        # csp.curr_domains[var] = list(sorted(values))
        entry = PriorityEntry(var, len(values), list(values))
        queue.put(entry)
    return queue
   
   
# Object to be entered into Priorty Queue
class PriorityEntry(object):
    def __init__(self, position, remaining, values):
        self.position = position       # EX: 'A1'
        self.remaining = remaining     # EX: 3
        self.values = values           # EX: [1,4,6,8]  (Not always ordered)           
    # To make the object comparible
    def __lt__(self, other):
        return self.remaining < other.remaining   

    
###########################
# SET UP INITIAL CSP
###########################

def sudoku_solver(input_board):
    # Define global variables (Whoops)
    global starting_board
    global sudoku
    global letters
    global default
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    default = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Initial board
    starting_board = input_board
    
    # Create the sudoku dict
    sudoku = OrderedDict()
    for i in np.arange(9):
        for j in np.arange(1, 10):
            idx = '{}{}'.format(letters[i], j)
            sudoku[idx] = list(default) if starting_board[i*9 + j-1] == '0' else [starting_board[i*9 + j-1]]
            
    # vars_list, domains, neighbors, constraints
    bt_neighbors = {}
    # Fill domain dict
    for key in sudoku.keys():
        implied_neighbors = return_implied(key)
        bt_neighbors[key] = implied_neighbors

    sudoku1 = copy.deepcopy(sudoku) # Used for AC3
    sudoku2 = copy.deepcopy(sudoku) # Used for BT

    # Solve with ac3 first
    ac3_board = ac_3(sudoku)
    ac3_solved = True
    for key, value in ac3_board.items(): ac3_solved = False if len(value) != 1 else ac3_solved
    # If AC3 solved, return answer
    if ac3_solved:
        output = ''
        for var, val in ac3_board.items(): output += val[0]
        return output, 'AC3'

    # AC3 did not solve, move to plan B (Back tracking search)
    if not ac3_solved:
        # print ('AC3 not solved')
        bt_csp = CSP(list(sudoku2.keys()), sudoku2, bt_neighbors)
        bt_board = backtracking_search(bt_csp)
        bt_output = ''
        for key in sorted(bt_board.keys()): bt_output += bt_board[key][0]
        return output, 'BTS'
    