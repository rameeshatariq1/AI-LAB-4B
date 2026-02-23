# Water Jug Problem using DFS

def dfs_water_jug(capA, capB, goal):
    visited = set()
    path = []

    def dfs(a, b):
        # If already visited, return False
        if (a, b) in visited:
            return False
        
        visited.add((a, b))
        path.append((a, b))

        print(f"Current State: ({a}, {b})")

        # Goal check
        if a == goal or b == goal:
            print("\n Goal Reached!")
            return True

        # Rule 1: Fill Jug A
        print("Applying Rule: Fill Jug A")
        if dfs(capA, b):
            return True

        # Rule 2: Fill Jug B
        print("Applying Rule: Fill Jug B")
        if dfs(a, capB):
            return True

        # Rule 3: Empty Jug A
        print("Applying Rule: Empty Jug A")
        if dfs(0, b):
            return True

        # Rule 4: Empty Jug B
        print("Applying Rule: Empty Jug B")
        if dfs(a, 0):
            return True

        # Rule 5: Pour A → B
        print("Applying Rule: Pour A → B")
        pour = min(a, capB - b)
        if dfs(a - pour, b + pour):
            return True

        # Rule 6: Pour B → A
        print("Applying Rule: Pour B → A")
        pour = min(b, capA - a)
        if dfs(a + pour, b - pour):
            return True

        path.pop()
        return False

    dfs(0, 0)

# Run the function
dfs_water_jug(4, 3, 2)