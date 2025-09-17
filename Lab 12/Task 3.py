import random
import math
import matplotlib.pyplot as plt

def input_sensor_coordinates():
    n = int(input("Enter number of sensors: "))
    coords = []
    for i in range(n):
        x, y = map(float, input(f"Enter coordinates for sensor {i+1} (x y): ").split())
        coords.append((x, y))
    return coords
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])
def total_path_distance(path, coords):
    dist = 0
    for i in range(len(path)):
        dist += euclidean_distance(coords[path[i]], coords[path[(i+1)%len(path)]])
    return dist
def greedy_route(coords):
    n = len(coords)
    unvisited = set(range(n))
    path = []
    current = 0
    path.append(current)
    unvisited.remove(current)
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coords[current], coords[x]))
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    return path
def random_route(n):
    path = list(range(n))
    random.shuffle(path)
    return path
# Simulated Annealing for TSP
def simulated_annealing(coords, initial_path, T=1000, alpha=0.995, stopping_T=1e-8, max_iter=100000):
    n = len(coords)
    current_path = initial_path[:]
    current_distance = total_path_distance(current_path, coords)
    best_path = current_path[:]
    best_distance = current_distance
    iter = 0
    while T > stopping_T and iter < max_iter:
        # 2-opt swap
        i, j = sorted(random.sample(range(n), 2))
        new_path = current_path[:i] + current_path[i:j+1][::-1] + current_path[j+1:]
        new_distance = total_path_distance(new_path, coords)
        delta = new_distance - current_distance
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_path = new_path
            current_distance = new_distance
            if current_distance < best_distance:
                best_path = current_path[:]
                best_distance = current_distance
        T *= alpha
        iter += 1
    return best_path

def plot_routes(coords, routes, labels, colors):
    plt.figure(figsize=(10, 6))
    for route, label, color in zip(routes, labels, colors):
        x = [coords[i][0] for i in route] + [coords[route[0]][0]]
        y = [coords[i][1] for i in route] + [coords[route[0]][1]]
        plt.plot(x, y, marker='o', label=label, color=color)
    for idx, (x, y) in enumerate(coords):
        plt.text(x, y, f"{idx}", fontsize=9, ha='right')
    plt.title("AUV Route Optimization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    coords = input_sensor_coordinates()
    n = len(coords)
    # Random route
    rand_path = random_route(n)
    rand_dist = total_path_distance(rand_path, coords)
    # Greedy route
    greedy_path = greedy_route(coords)
    greedy_dist = total_path_distance(greedy_path, coords)
    # Simulated Annealing
    sa_path = simulated_annealing(coords, greedy_path)
    sa_dist = total_path_distance(sa_path, coords)
    print("\nRoute distances:")
    print(f"Random path distance: {rand_dist:.2f}")
    print(f"Greedy path distance: {greedy_dist:.2f}")
    print(f"Simulated Annealing optimized distance: {sa_dist:.2f}")
    # Plot
    plot_routes(
        coords,
        [rand_path, greedy_path, sa_path],
        ["Random", "Greedy", "Simulated Annealing"],
        ["gray", "blue", "red"]
    )
if __name__ == "__main__":
    main()