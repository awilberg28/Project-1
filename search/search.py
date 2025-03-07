# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    currentStack = util.Stack()
    # current = problem
    start_state = problem.getStartState()
    currentStack.push((start_state, []))
    visitedNodes = set()
    # print("Current stack: \n", currentStack.getElements())
    #while the stack is not empty
    while not currentStack.isEmpty():
        state, path = currentStack.pop()
        # print("Current stack:", currentStack.getElements())
        if problem.isGoalState(state):
            # print("Current stack: \n", currentStack.getElements())
            return path
        if state not in visitedNodes:
            visitedNodes.add(state)
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visitedNodes:
                currentStack.push((successor, path + [action]))
                # print("Current stack: \n", currentStack.getElements())
    return []
  
def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    toVisit = util.Queue()
    start = problem.getStartState()
    visited = set(start)
    toVisit.enqueue((start , []))
    

    while not toVisit.isEmpty():
        state , dirList = toVisit.dequeue()
        if problem.isGoalState(state):
            return dirList

        for successor, dir, cost in problem.getSuccessors(state):
            if successor not in visited:
                toVisit.enqueue((successor, dirList + [dir]))
                visited.add(successor)
                
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    toVisit = util.PriorityQueue()
    totalCost = {}
    toVisit.enqueue((problem.getStartState() , []), 0)
    totalCost[problem.getStartState()] = 0

    while not toVisit.isEmpty():
        state , dirList = toVisit.dequeue()
        
        if problem.isGoalState(state):
            return dirList
        
        for successor, dir, cost in problem.getSuccessors(state):
            newCost = totalCost[state] + cost
            if (successor not in totalCost) or (newCost < totalCost[successor]):
                totalCost[successor] = newCost
                toVisit.enqueue((successor, dirList + [dir]), newCost)
                
    return []


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    toVisit = util.PriorityQueue()
    totalCost = {}
    toVisit.enqueue((problem.getStartState() , []), 0)
    totalCost[problem.getStartState()] = 0

    while not toVisit.isEmpty():
        state , dirList = toVisit.dequeue()
        
        if problem.isGoalState(state):
            return dirList

        for successor, dir, cost in problem.getSuccessors(state):
            newCost = totalCost[state] + cost
            if (successor not in totalCost) or (newCost < totalCost[successor]):
                totalCost[successor] = newCost
                toVisit.enqueue((successor, dirList + [dir]), newCost + heuristic(successor,problem))
                
    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
