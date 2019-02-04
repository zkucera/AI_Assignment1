# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
    """
    Returns the start state for the search problem 
    """
    util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
          

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  
          
  print problem
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getSuccessors(problem.getStartState())[1][0])
  from game import Directions
  from util import Stack
  

  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  frontier = Stack()
  explored = []
  solution = []

  def recursiveDFS(node):
    if problem.isGoalState(node):
      print node , "IS GOAL STATE"
      print "RETURNING SOLUTION :", solution
      return solution
    else:
      explored.append(node) #We have visited the node
      successors = problem.getSuccessors(node) #Get the successors
      for x in successors:#For each successor
        if x[0] not in explored:#If we havent visited the node
          frontier.push(x[0])#Add the node to the frontier
          print node, "-->",x[0]
          done = recursiveDFS(x[0])#Recurse on the new node, set done equal to the output
          if done is not None:#If done is not empty, ei: If at the end of the recursion we found a goal state, add the direction to the start of the solution list
            if x[1] == "North":
              solution.insert(0,n)
            elif x[1] == "South":
              solution.insert(0,s)
            elif x[1] == "East":
              solution.insert(0,e)
            elif x[1] == "West":
              solution.insert(0,w)
            return done
              
  frontier.push(problem.getStartState())
            

  currentNode = frontier.pop()
  explored.append(currentNode)
  #done = recursiveDFS(currentNode)
  #print "Length: ", len(done)
  #print "Done: " , done
  #return done
  successors = problem.getSuccessors(currentNode)
  
  while successors is not None:
    for x in successors:
      if x not in explored:
        explored.append(x)
        frontier.push(x)

  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch