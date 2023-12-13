from problem import NQueens

def main():
    size = 8  # Change this to the size of the N-Queens problem you want to solve
    n_queens = NQueens(size)

    print("Solving N-Queens problem using Breadth-First Search...")
    bfs_solution = n_queens.bfs()
    print("Breadth-First Search Solution:", bfs_solution)

    print("Solving N-Queens problem using Depth-First Search...")
    dfs_solution = n_queens.dfs()
    print("Depth-First Search Solution:", dfs_solution)

    print("Solving N-Queens problem using Backtracking Search...")
    backtracking_solution = n_queens.backtracking_search()
    print("Backtracking Search Solution:", backtracking_solution)

    print("Solving N-Queens problem using Simulated Annealing...")
    sa_solution = n_queens.simulated_annealing()
    print("Simulated Annealing Solution:", sa_solution)

if __name__ == "__main__":
    main()
