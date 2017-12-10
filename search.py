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
from sets import Set
from collections import deque

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
  """ DFS search
  """
  # Initialize explored:
  explored = Set()

  # Initialize actions:
  actions = []

  # Initialize frontier:
  frontier = []

  # Initialize search:
  frontier.append(
    (
        problem.getStartState(),
        list(actions)
    )
  )

  # Explore frontier:
  while frontier:
      (current, actions) = frontier.pop()

      # Goal state test:
      if problem.isGoalState(current):
          break

      # Add to explored:
      explored.add(current)

      # Expand frontier:
      for (successor, action, _) in problem.getSuccessors(current):
          if not (successor in explored):
              # Update actions:
              successorActions = list(actions)
              successorActions.append(action)

              # Update frontier:
              frontier.append(
                (
                    successor,
                    successorActions
                )
              )

  return actions

def breadthFirstSearch(problem):
  """ BFS search
  """
  # Initialize explored:
  explored = Set()

  # Initialize actions:
  actions = []

  # Initialize frontier:
  frontier = deque()

  # Initialize search:
  frontier.append(
    (
        problem.getStartState(),
        list(actions)
    )
  )

  # Explore frontier:
  while frontier:
      (current, actions) = frontier.popleft()

      # Goal state test:
      if problem.isGoalState(current):
          break

      # Add to explored:
      explored.add(current)

      # Expand frontier:
      for (successor, action, _) in problem.getSuccessors(current):
          if not (successor in explored):
              # Update actions:
              successorActions = list(actions)
              successorActions.append(action)

              # Update frontier:
              frontier.append(
                (
                    successor,
                    successorActions
                )
              )

  return actions

def uniformCostSearch(problem):
  """ Dijkstra shorest path with null heuristic
  """
  # Initialize explored:
  explored = Set()

  # Initialize actions:
  actions = []

  # Initialize total cost:
  totalCost = 0

  # Initialize frontier:
  frontier = util.PriorityQueue()

  # Initialize search:
  frontier.push(
    (
        problem.getStartState(),
        list(actions),
        totalCost
    ),
    totalCost
  )

  # Explore frontier:
  while frontier:
      # Expand frontier:
      (current, actions, totalCost) = frontier.pop()

      # Goal state test:
      if problem.isGoalState(current):
          break

      # Remove sub-optimal already explored:
      if current in explored:
          continue
      # Add to explored:
      else:
          explored.add(current)

      # Expand frontier:
      for (successor, action, cost) in problem.getSuccessors(current):
          if not (successor in explored):
              # Update actions:
              successorActions = list(actions)
              successorActions.append(action)

              # Update total cost:
              successorCost = totalCost + cost

              # Update frontier:
              frontier.push(
                (
                    successor,
                    successorActions,
                    successorCost
                ),
                successorCost
              )

  return actions

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  """ A* search with L1 & L2 heuristic
  """
  # Initialize explored:
  explored = Set()

  # Initialize actions:
  actions = []

  # Initialize total cost:
  totalCost = 0

  # Initialize frontier:
  frontier = util.PriorityQueue()

  # Initialize search:
  frontier.push(
    (
        problem.getStartState(),
        list(actions),
        totalCost
    ),
    totalCost
  )

  # Explore frontier:
  while frontier:
      # Expand frontier:
      (current, actions, totalCost) = frontier.pop()

      # Goal state test:
      if problem.isGoalState(current):
          break

      # Remove sub-optimal already explored:
      if current in explored:
          continue
      # Add to explored:
      else:
          explored.add(current)

      # Expand frontier:
      for (successor, action, cost) in problem.getSuccessors(current):
          if not (successor in explored):
              # Update actions:
              successorActions = list(actions)
              successorActions.append(action)

              # Update total cost:
              successorCost = totalCost + cost + heuristic(successor, problem)

              # Update frontier:
              frontier.push(
                (
                    successor,
                    successorActions,
                    successorCost
                ),
                successorCost
              )

  return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
