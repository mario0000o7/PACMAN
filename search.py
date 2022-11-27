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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"





    return labirynt(problem, util.Stack())




# Budowanie sciezki od konca do poczatku mamy podany slownik rodzicow i idzemy po rodzicach az na sam koniec czyli trafimy ze droga jest None czyli start
def buildWay(node, parent_list):
    way = node[1]
    if parent_list.get(node) is None:
        return []
    return buildWay(parent_list[node], parent_list) + [way]




def zadanie4(problem,heuristic):
    #slownik rodzicow
    parent_list = {}
    #set odwiedzonych
    visited = set()
    #slownik kosztow aby sobie liczyc z rodzica koszt
    cost = {}
    #kolejka priorytetowa aktualizuje sie ja za pomoca update
    #najmniejszy koszt jest na poczatku
    structure = util.PriorityQueue()
    node = problem.getStartState()
    structure.push(item=(node, None), priority=0)
    cost[node] = 0

    while not structure.isEmpty():
        node = structure.pop()
        state = node[0]

        if problem.isGoalState(state):
            return buildWay(node, parent_list)

        if state not in visited:
            visited.add(state)
            for successor in problem.getSuccessors(state):
                successor_state = successor[0]
                successor_cost = successor[2]
                if successor_state not in visited:
                    g = cost[state] + successor_cost
                    #funckja heurystyczna jest gotowa
                    h=heuristic(successor_state, problem)
                    structure.update(successor, g+h)
                    cost[successor_state] = g
                    parent_list[successor] = node

    return []

def zadanie3(problem):
    #slownik rodzicow
    parent_list = {}
    #set odwiedzonych
    visited = set()
    #slownik kosztow aby sobie liczyc z rodzica koszt
    cost = {}
    #kolejka priorytetowa aktualizuje sie ja za pomoca update
    #najmniejszy koszt jest na poczatku
    structure = util.PriorityQueue()


    node = problem.getStartState()
    structure.push(item=(node, None), priority=0)
    cost[node] = 0

    while not structure.isEmpty():
        node = structure.pop()
        state = node[0]

        if problem.isGoalState(state):
            return buildWay(node, parent_list)

        if state not in visited:
            visited.add(state)
            for successor in problem.getSuccessors(state):
                successor_state = successor[0]
                successor_cost = successor[2]
                if successor_state not in visited:
                    g = cost[state] + successor_cost
                    structure.update(successor, g)
                    cost[successor_state] = g
                    parent_list[successor] = node

    return []
def labirynt(problem, structure):
        #slownik rodzicow
        parent_list = dict()
        #lista odwiedzonych
        visited = set()
        #punkt startowy
        start_state = problem.getStartState()
        #nie ma drogi czyli trzeba dac None albo cos innego
        node = (start_state, None, 0)
        structure.push(node)

        while not structure.isEmpty():
            node = structure.pop()
            state = node[0]

            if problem.isGoalState(state):
                return buildWay(node, parent_list)

            if state not in visited:
                visited.add(state)
                for successor in problem.getSuccessors(state):
                    successor_state = successor[0]
                    if successor_state not in visited:
                        structure.push(successor)
                        parent_list[successor] = node
        return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    return labirynt(problem, util.Queue())





def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    return zadanie3(problem)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    return zadanie4(problem,heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
