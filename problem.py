from collections import deque
import random
import math

class NQueens:
    def __init__(self, size):
        self.size = size

    def initial_state(self):
        # Start with no queens on the board
        return tuple([-1] * self.size)

    def is_valid_state(self, state):
        # Check if the current state is valid (no conflicts)
        for i in range(self.size):
            if state[i] == -1:
                continue
            for j in range(i + 1, self.size):
                if state[j] == -1:
                    continue
                if state[i] == state[j] or \
                   abs(state[i] - state[j]) == j - i:
                    return False
        return True

    def goal_test(self, state):
        # Check if all queens are placed without conflicts
        return self.is_valid_state(state) and state.count(-1) == 0

    def successors(self, state):
        row = state.count(-1)
        if row == 0:
            return []  # All queens are placed

        successors = []
        for col in range(self.size):
            new_state = list(state)
            new_state[row - 1] = col
            if self.is_valid_state(new_state):
                successors.append(tuple(new_state))
        return successors

    def value(self, state):
        # Number of conflicts as the heuristic value
        conflicts = 0
        for i in range(self.size):
            if state[i] == -1:
                continue
            for j in range(i + 1, self.size):
                if state[j] == -1:
                    continue
                if state[i] == state[j] or \
                   abs(state[i] - state[j]) == j - i:
                    conflicts += 1
        return -conflicts

    def bfs(self):
        queue = deque([self.initial_state()])
        while queue:
            state = queue.popleft()
            if self.goal_test(state):
                return state
            for successor in self.successors(state):
                queue.append(successor)
        return None

    def dfs(self):
        stack = deque([self.initial_state()])
        while stack:
            state = stack.pop()
            if self.goal_test(state):
                return state
            for successor in self.successors(state):
                stack.append(successor)
        return None

    def backtracking_search(self):
        def backtrack(row, state):
            if row == self.size:
                return state if self.goal_test(state) else None

            for col in range(self.size):
                new_state = list(state)
                new_state[row] = col
                if self.is_valid_state(new_state):
                    result = backtrack(row + 1, tuple(new_state))
                    if result:
                        return result
            return None

        return backtrack(0, self.initial_state())

    def simulated_annealing(self):
        def temperature_schedule(time):
            return 1.0 / (1 + 0.0001 * time)
        
        initial_state = list(range(self.size))
        random.shuffle(initial_state)
        current = tuple(initial_state)

        for t in range(1, 200000):
            temp = temperature_schedule(t)
            if temp <= 0.00001:
                return current if self.goal_test(current) else None

            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            next_state = list(current)
            next_state[row] = col
            next_state = tuple(next_state)

            delta_e = self.value(next_state) - self.value(current)
            if delta_e > 0 or random.uniform(0, 1) < math.exp(delta_e / temp):
                current = next_state

        return current if self.goal_test(current) else None