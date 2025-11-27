#!/usr/bin/env python3

import rospy
import heapq
import math
from algorithms.neighbors import find_neighbors


def a_star(start, goal, width, height, costmap, resolution, origin, grid_visualisation):

    epsilon = 1.5  # between 1.2-2.0. can make it greedier to speed it up

    # Basic validation
    if start < 0 or start >= len(costmap):
        rospy.logerr("Start node out of bounds.")
        return [], 0

    if goal < 0 or goal >= len(costmap):
        rospy.logerr("Goal node out of bounds.")
        return [], 0

    if costmap[start] > 150:
        rospy.logwarn("Start may be inside an obstacle (cost > 150).")

    if costmap[goal] > 150:
        rospy.logwarn("Goal may be inside an obstacle (cost > 150).")

    open_set = []
    closed_set = set()
    g_costs = {start: 0.0}
    parents = {start: None}
    examined_nodes = 0

    # Heuristic
    def heuristic(n1, n2):
        x1, y1 = n1 % width, n1 // width
        x2, y2 = n2 % width, n2 // width
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Push start node
    h = heuristic(start, goal)
    f = epsilon * h
    heapq.heappush(open_set, (f, h, start))

    max_iterations = 100000
    iteration = 0

    while open_set and iteration < max_iterations:
        iteration += 1

        f_cost, h_cost, current = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)
        examined_nodes += 1

        try:
            grid_visualisation.set_color(current, "pale yellow")
        except Exception:
            pass

        if current == goal:
            # Build path
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()

            for p in path:
                try:
                    grid_visualisation.set_color(p, "green")
                except Exception:
                    pass

            return path, examined_nodes

        current_g = g_costs[current]

        neighbors = find_neighbors(
            current, width, height, costmap, orthogonal_step_cost=1.0
        )

        for neighbor_index, move_cost in neighbors:

            if neighbor_index in closed_set:
                continue

            tentative_g = current_g + move_cost

            if neighbor_index not in g_costs or tentative_g < g_costs[neighbor_index]:
                g_costs[neighbor_index] = tentative_g
                parents[neighbor_index] = current

                h = heuristic(neighbor_index, goal)
                f = tentative_g + epsilon * h

                heapq.heappush(open_set, (f, h, neighbor_index))

                try:
                    grid_visualisation.set_color(neighbor_index, "orange")
                except Exception:
                    pass

    rospy.logwarn("A* failed to find a path after %d nodes.", examined_nodes)
    return [], examined_nodes
