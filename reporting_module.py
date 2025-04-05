import numpy as np
import matplotlib.pyplot as plt


def report_stats(population):
    dead = 0
    alive = 0
    infected = 0

    for person in population:
        if person.alive:
            alive +=1
            
            if person.active_infection is not None:
                infected +=1
        else:
            dead +=1
    print(f"{alive} people are alive and {dead} are dead, death percentage of {round(dead/alive, 2)}% and {infected} are currently infected")


def plot_infected_heatmap(world):
    # Create a matrix with dimensions (max_x, max_y)
    heatmap = np.zeros((world.max_x, world.max_y))
    
    for x in range(world.max_x):
        for y in range(world.max_y):
            area = world.world_grid[x][y]
            if area is not None:
                # Count infected people in the area (i.e., people with an active infection)
                count = sum(1 for person in area.population if person.active_infection is not None)
                heatmap[x, y] = count
    
    # Plot the heatmap
    plt.imshow(heatmap, origin='lower', cmap='hot', interpolation='nearest')
    plt.colorbar(label='Number of Infected')
    plt.title('Heatmap: Infected People per Area')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()
