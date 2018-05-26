#! shebang
from collections import deque
import numpy as np
import sys
import copy
import time
import resource
import heapq


frontier = deque()
frontier_ast = []
frontier_list = set()
explored_states = set()
path = {}
goal_matrix = np.matrix([[0, 1, 2],
                         [3, 4, 5],
                         [6, 7, 8]])


########################
#     BFS - SEARCH     #
########################

def bfs(initial_state_matrix, goal_matrix, shape):
    # define global variables
    global frontier
    global frontier_ast
    global path
    global explored_states
    
    start_time = time.time()
    
    # create initial state object
    initial_state = State(matrix=initial_state_matrix)
    
    # put the initial state in the frontier
    frontier.append(initial_state)
    frontier_list.add(str( initial_state.get_list() ))
    
    node_number = 0
    expanded_count = 0
    max_depth = 1
    # iterate through the frontier
    while frontier:
        node_number += 1
        # pop state object from stack
        state = frontier.popleft()
        # pop state matrix from stack
        state_matrix = state.get_matrix()
        state_cost = state.get_cost()
        state_list = state.get_list()
        
        # remove from frontier set and add to the explored set
        frontier_list.remove(str(state_list))
        explored_states.add(str(state_list))
        # add the last move and parent node to the path dict
        path[node_number] = [state.get_parent(), state.get_move()]
        
        # check if the current state is the goal state
        if (state_matrix == goal_matrix).all():
            true_path = find_root(node_number, path)
            time_elapsed = time.time() - start_time
            memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            return "SUCCESS", state, time_elapsed, expanded_count, memory, true_path[1:], max_depth, state_cost
           
        # get list of child nodes
        child_nodes = state.generate_children_nodes(node_number)
        expanded_count += 1
        
        # iterate through children nodes
        for child in child_nodes:
            child_matrix = child.get_matrix()
            child_list = child.get_list()
           
            # check if matrix already explored
            if (str(child_list) in explored_states) or (str(child_list) in frontier_list):
                continue
              
            # update the max-depth
            if child.get_level() > max_depth:
                max_depth = child.get_level()
              
            # heappush child to frontier_ast
            frontier.append(child)
            frontier_list.add(str(child_list))
                         
    true_path = find_root(node_number, path)
    memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    time_elapsed = time.time() - start_time           
    return "FAILURE", state, time_elapsed, expanded_count, memory, true_path, max_depth, state_cost



########################
#     DFS - SEARCH     #
########################

def dfs(initial_state_matrix, goal_matrix, shape):
    # define global variables
    global frontier
    global frontier_ast
    global path
    global explored_states
    
    start_time = time.time()
    
    # create initial state object
    initial_state = State(matrix=initial_state_matrix)
    
    # put the initial state in the frontier
    frontier.append(initial_state)
    frontier_list.add(str( initial_state.get_list() ))
    
    node_number = 0
    expanded_count = 0
    max_depth = 1
    # iterate through the frontier
    while frontier:
        node_number += 1
        # pop state object from stack
        state = frontier.pop()
        # pop state matrix from stack
        state_matrix = state.get_matrix()
        state_cost = state.get_cost()
        state_list = state.get_list()
        
        # remove from frontier set and add to the explored set
        frontier_list.remove(str(state_list))
        explored_states.add(str(state_list))
        # add the last move and parent node to the path dict
        path[node_number] = [state.get_parent(), state.get_move()]
        
        # check if the current state is the goal state
        if (state_matrix == goal_matrix).all():
            true_path = find_root(node_number, path)
            time_elapsed = time.time() - start_time
            memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            return "SUCCESS", state, time_elapsed, expanded_count, memory, true_path[1:], max_depth, state_cost
           
        # get list of child nodes
        child_nodes = state.generate_children_nodes(node_number)
        expanded_count += 1
        
        # iterate through children nodes
        for child in reversed(child_nodes):
            child_matrix = child.get_matrix()
            child_list = child.get_list()
           
            # check if matrix already explored
            if (str(child_list) in explored_states) or (str(child_list) in frontier_list):
                continue
              
            # update the max-depth
            if child.get_level() > max_depth:
                max_depth = child.get_level()
              
            # heappush child to frontier_ast
            frontier.append(child)
            frontier_list.add(str(child_list))
                         
    true_path = find_root(node_number, path)
    memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    time_elapsed = time.time() - start_time           
    return "FAILURE", state, time_elapsed, expanded_count, memory, true_path, max_depth, state_cost



   
   
########################
#      A* SEARCH       #
########################

def ast(initial_state_matrix, goal_matrix, shape):
    # define global variables
    global frontier
    global frontier_ast
    global path
    global explored_states
    start_time = time.time()
    # create initial state object
    initial_state = State(matrix=initial_state_matrix)
    # put the initial state in the frontier
    heapq.heappush(frontier_ast, initial_state)
    
    frontier_list.add(str( initial_state.get_list() ))
    node_number = 0
    expanded_count = 0
    max_depth = 1
    # iterate through the frontier
    while frontier_ast:
        node_number += 1
        # print ("node number:\t", node_number)
        # pop state object from stack
        state = heapq.heappop(frontier_ast)
        # pop state matrix from stack
        state_matrix = state.get_matrix()
        state_cost = state.get_cost()
        state_list = state.get_list()
        
        # remove from frontier set and add to the explored set
        frontier_list.remove(str(state_list))
        explored_states.add(str(state_list))
        # add the last move and parent node to the path dict
        path[node_number] = [state.get_parent(), state.get_move()]
        
        # check if the current state is the goal state
        if (state_matrix == goal_matrix).all():
            true_path = find_root(node_number, path)
            time_elapsed = time.time() - start_time
            memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            return "SUCCESS", state, time_elapsed, expanded_count, memory, true_path[1:], max_depth, state_cost
           
        # get list of child nodes
        child_nodes = state.generate_children_nodes(node_number)
        expanded_count += 1
        
        # iterate through children nodes
        for child in child_nodes:
            child_matrix = child.get_matrix()
            child_list = child.get_list()
           
            # check if matrix already explored
            if (str(child_list) in explored_states) or (str(child_list) in frontier_list):
                continue
              
            # update the max-depth
            if child.get_level() > max_depth:
                max_depth = child.get_level()
              
            # heappush child to frontier_ast
            heapq.heappush(frontier_ast, child)
            frontier_list.add(str(child_list))
                         
    true_path = find_root(node_number, path)
    memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    time_elapsed = time.time() - start_time           
    return "FAILURE", state, time_elapsed, expanded_count, memory, true_path, max_depth, state_cost

   
   
   
#####################################
#  OBJECT CLASS TO STORE NODE INFO  #
#####################################
   
class State(object):
    
    # global variables
    global goal_matrix
  
    # constructor
    def __init__(self, matrix, parent=0, level=0, move="Start"):
        self.matrix = matrix
        self.parent = parent
        self.cost = self.ast_cost() + level
        self.level = level
        self.move = move
        self.list = self.matrix_to_list(matrix)
        
    def __lt__(self, other):
        move_set = ['Up', 'Down', 'Left', 'Right']
        return (self.cost, move_set.index(self.move)) < (other.cost, move_set.index(other.move))
        
    def get_cost(self):
        return self.cost
     
    def get_matrix(self):
        return self.matrix
     
    def get_list(self):
        return self.list
     
    def get_parent(self):
        return self.parent
     
    def get_move(self):
        return self.move
     
    def get_level(self):
        return self.level
       
    # method to return the manhatten cost value
    def ast_cost(self):
        global goal_matrix
        total_sum = 0
        for i in range(1,9):
            # get index of i
            g_index = np.where(goal_matrix==i)
            s_index = np.where(self.matrix==i)
            # print ('i index: {}'.format(i))
            # print ('g_index:\n{}'.format(g_index))
            # print ('s_index:\n{}'.format(s_index))
            current_cost = abs(g_index[0][0]-s_index[0][0]) + abs(g_index[1][0]-s_index[1][0])
            total_sum += current_cost
        return total_sum
       
    # convert matrix to list
    def matrix_to_list(self, matrix):
        output = matrix.reshape(-1,9)
        output = list(output[0])
        return output
      
    # method to generate children nodes
    def generate_children_nodes(self, parent_number):
        # make copy of self.matrix
        state_matrix = np.array(self.matrix)
        # create empty list for child nodes
        child_nodes = []
        # get index of 0
        itemindex = np.where(state_matrix==0)
        # assign to variables to make easier
        i_row = itemindex[0][0]
        j_col = itemindex[1][0]
        
        # check if moves possible
        if i_row > 0:
            child_node = self.move_up(i_row, j_col, parent_number)
            child_nodes.append(child_node)
          
        if i_row < 2:
            child_node = self.move_down(i_row, j_col, parent_number)
            child_nodes.append(child_node)
          
        if j_col > 0:
            child_node = self.move_left(i_row, j_col, parent_number)
            child_nodes.append(child_node)
           
        if j_col < 2:
            child_node = self.move_right(i_row, j_col, parent_number)
            child_nodes.append(child_node)
        return child_nodes   
       
    def move_up(self, i_row, j_col, parent_number):
        # assign matrix to new variable
        # change indices
        next_matrix = np.array(self.matrix)
        next_matrix[i_row][j_col] = next_matrix[i_row-1][j_col]
        next_matrix[i_row-1][j_col] = 0
        child_node = State(next_matrix, parent_number, self.level+1, 'Up')
        return child_node
   
    def move_down(self, i_row, j_col, parent_number):
        # assign matrix to new variable
        # change indices
        next_matrix = np.array(self.matrix)
        next_matrix[i_row][j_col] = next_matrix[i_row+1][j_col]
        next_matrix[i_row+1][j_col] = 0
        child_node = State(next_matrix, parent_number, self.level+1, 'Down')
        return child_node   
   
    def move_left(self, i_row, j_col, parent_number):
        # assign matrix to new variable
        # change indices
        next_matrix = np.array(self.matrix)
        next_matrix[i_row][j_col] = next_matrix[i_row][j_col-1]
        next_matrix[i_row][j_col-1] = 0
        child_node = State(next_matrix, parent_number, self.level+1, 'Left')
        return child_node   
   
    def move_right(self, i_row, j_col, parent_number):
        # assign matrix to new variable
        # change indices
        next_matrix = np.array(self.matrix)
        next_matrix[i_row][j_col] = next_matrix[i_row][j_col+1]
        next_matrix[i_row][j_col+1] = 0
        child_node = State(next_matrix, parent_number, self.level+1, 'Right')
        return child_node
       
       
   
###########################################################
# Function to determine the path given complete path dict #
###########################################################

def find_root(node, dictionary):
    true_path = []
    while node > 0:
        move = dictionary[node][1]
        # print ("existing path: {0}\nnew move: {1}".format(true_path, move))
        true_path.insert(0, move)
        # print ("new path:\t", true_path)
        node = dictionary[node][0]
    return true_path
        
 

#########################################################
# Function to take the user input and convert to matrix #
#########################################################
      
def create_matrix_from_input(string_starting_input):
    # extract numbers from string input
    list_starting_input = [x.strip() for x in string_starting_input.split(',')]
    # convert entries to ints
    for i in range(len(list_starting_input)):
        list_starting_input[i] = int(list_starting_input[i])
    # determine number of columns
    n_rows = int(np.sqrt(len(list_starting_input)))
    # print for debugging
    # convert list to array for reshaping
    output_matrix = np.array(list_starting_input)
    # reshape to have squared property
    output_matrix = output_matrix[:n_rows*n_rows]
    output_matrix = output_matrix.reshape(n_rows, n_rows)
    # return the reshaped array
    return output_matrix
    

    
    
#if __name__ == "__main__":
def eight_puzzle_ast(starting_board):
    
    initial_state_matrix = create_matrix_from_input(starting_board)
    #initial_state_matrix = create_matrix_from_input('1,4,2,3,0,5,6,7,8')
    
    shape = initial_state_matrix.shape
    goal_matrix = np.matrix([[0, 1, 2],
                             [3, 4, 5],
                             [6, 7, 8]])
    
    
    response, output, completion_time, n_nodes, memory, true_path, search_depth, cost = ast(initial_state_matrix, goal_matrix, shape)
    memory = memory / 1024 / 1024
    return true_path, cost, n_nodes, output.get_level(), search_depth, completion_time, memory
    
# eight_puzzle_ast('1,4,2,3,0,5,6,7,8')
    
'''
    try:
        file = open("output.txt", "w")
        file.write("path_to_goal: {0}\n".format(true_path))
        file.write("cost_of_path: {0}\n".format(cost))
        file.write("nodes_expanded: {0}\n".format(n_nodes) )
        file.write("search_depth: {0}\n".format(output.get_level()) )
        file.write("max_search_depth: {0}\n".format(search_depth) )
        file.write("running_time: {0}\n".format(completion_time) )
        file.write("max_ram_usage: {0}".format(memory))
        file.close()
    except:
        print (response)
    
    
    if sys.argv[1] == 'bfs':
        response, output, completion_time, n_nodes, memory, true_path, search_depth, cost = bfs(initial_state_matrix, goal_matrix, shape)
        memory = memory / 1024 / 1024
        print (response)
        try:
            file = open("output.txt", "w")
            file.write("path_to_goal: {0}\n".format(true_path))
            file.write("cost_of_path: {0}\n".format(cost) )
            file.write("nodes_expanded: {0}\n".format(n_nodes) )
            file.write("search_depth: {0}\n".format(output.get_level()) )
            file.write("max_search_depth: {0}\n".format(search_depth) )
            file.write("running_time: {0}\n".format(completion_time) )
            file.write("max_ram_usage: {0}".format(memory))
            file.close()
        except:
            print (response)
    
    
    if sys.argv[1] == 'dfs':
        response, output, completion_time, n_nodes, memory, true_path, search_depth, cost = dfs(initial_state_matrix, goal_matrix, shape)
        memory = memory / 1024 / 1024
        print (response)
        try:
            file = open("output.txt", "w")
            file.write("path_to_goal: {0}\n".format(true_path))
            file.write("cost_of_path: {0}\n".format(cost) )
            file.write("nodes_expanded: {0}\n".format(n_nodes) )
            file.write("search_depth: {0}\n".format(output.get_level()) )
            file.write("max_search_depth: {0}\n".format(search_depth) )
            file.write("running_time: {0}\n".format(completion_time) )
            file.write("max_ram_usage: {0}".format(memory))
            file.close()
        except:
            print (response)
    
'''
    
    
    
