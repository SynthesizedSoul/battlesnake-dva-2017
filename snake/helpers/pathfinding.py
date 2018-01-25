"""A* algorithm based on http://www.redblobgames.com/pathfinding/a-star/implementation.html"""

from queue import PriorityQueue

def heuristic(coord_1, coord_2):
    """Determines the approximate cost going from one coord to another"""
    (x_coord_1, y_coord_1) = coord_1
    (x_coord_2, y_coord_2) = coord_2
    return abs(x_coord_1 - x_coord_2) + abs(y_coord_1 - y_coord_2)

def a_star(graph, start_node, goal_node):
    """Determines a good path from start to goal based on heuristic"""
    to_visit = PriorityQueue()
    to_visit.put((0, start_node))
    came_from = {}
    cost_so_far = {}
    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while not to_visit.empty():
        current = to_visit.get()[1]

        if current == goal_node:
            break

        for next_node in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal_node, next_node)
                to_visit.put((priority, next_node))
                came_from[next_node] = current

    return came_from