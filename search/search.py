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
  

  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  explored = []
  solution = []

  def recursiveDFS(node):
    if problem.isGoalState(node):
      print node , "IS GOAL STATE"
      return solution
    else:
      print node, "HAS BEEN SEARCHED" 
      explored.append(node) #We have visited the node
      successors = problem.getSuccessors(node) #Get the successors
      for x in successors:#For each successor
        if x[0] not in explored:#If we havent visited the node
          done = recursiveDFS(x[0])#Recurse on the new node, set done equal to the output
          if done is not None:#If done is not empty, ei: If at any point we found a goal state, add the direction to the start of the solution list
            if x[1] == "North":
              solution.insert(0,n)
            elif x[1] == "South":
              solution.insert(0,s)
            elif x[1] == "East":
              solution.insert(0,e)
            elif x[1] == "West":
              solution.insert(0,w)
            return done 
              
  currentNode = problem.getStartState()
  explored.append(currentNode)
  done = recursiveDFS(currentNode)
  print "Length: ", len(done)
  print "Done: " , done
  return done
  
  

  util.raiseNotDefined()

def breadthFirstSearch(problem):
  from game import Directions
  from util import Queue
  

  n=Directions.NORTH
  s=Directions.SOUTH
  e=Directions.EAST
  w=Directions.WEST
  explored = []
  solution = []
  prev = []
  curr=[]
  queue = Queue()

  def BFS(node):
    firstRun = True #If this is the first pass through the while loop
    if problem.isGoalState(node): #if the inital node is the goal state, then pacman starts on the goal state
      print "START STATE IS THE GOAL STATE"
      return solution
    while queue: #As long as there are still nodes to explore
      currentNode = queue.pop() #Get the next node in line

      if firstRun is True:#If this is our first run through the loop
        explored.append(currentNode)#Add it to explored
        firstRun = False
        successors = problem.getSuccessors(currentNode)#Get the successors
        for x in successors:#Add the successors to the list
          if x[0] not in explored:
            prev.append((currentNode,0)) # prev and curr are used to keep a child/parent relationship between nodes to allow backtracking the path when the goal is found
            curr.append(x)               #
            queue.push(x)
      else: #If it isnt our first run
        explored.append(currentNode[0])#Add the current node to explored
        if problem.isGoalState(currentNode[0]):# If we found the goal state, return the solution
          print currentNode[0], "IS GOAL STATE"
          
          solution.insert(0,currentNode[1])#Add the final step to the solution
          while currentNode not in problem.getSuccessors(problem.getStartState()): #Until we reach the starting position
            currentNode = prev[curr.index(currentNode)] #Set the current node to the parent of the current node
            solution.insert(0,currentNode[1])#Add the instruction to the solution.
          return solution

        successors = problem.getSuccessors(currentNode[0]) #Get the successors to the current state
        for x in successors:#Add each successor to the queue, add the parent node to prev, and the successors to curr
          if x[0] not in explored:
            prev.append(currentNode)
            curr.append(x)
            queue.push(x)

  currentNode = problem.getStartState()
  explored.append(currentNode)
  queue.push(currentNode)
  done = BFS(currentNode)
  return done

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