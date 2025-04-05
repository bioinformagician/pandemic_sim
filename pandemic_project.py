from human_module import *
from world_module import *
from reporting_module import *

influenza = Virus(**influenza_virus_blueprint) 
corona = Virus(**corona_virus_blueprint)        

european = EuropeanPopulation()


europeans = [Person(**european.generate_person_dict()) for _ in range(300000)]


corona.infect(europeans[0])


n_columns = 50
n_rows = 100
world = World(max_x=n_columns, max_y=n_rows)



for column in range(n_columns):
    for row in range(n_rows):
        area = Area(hospital=True, income=100, x_coordinate = column, y_coordinate = row, population = None)    
        world.add_area(area)



for european in europeans:
    random_x = random.randint(0, n_columns - 1)
    random_y = random.randint(0, n_rows - 1)

    world.world_grid[random_x][random_y].add_person(european)
    european.area = world.world_grid[random_x][random_y]






worldsim = SimulateWorld(people = europeans, world = world)




#for i in range(100):
    #worldsim.increment_one_day()

    #report_stats(europeans)




plt.ion()
fig, ax = plt.subplots()
heatmap = np.zeros((world.max_x, world.max_y))
img = ax.imshow(heatmap, origin='lower', cmap='hot', interpolation='nearest')
cbar = plt.colorbar(img, ax=ax)
ax.set_title('Heatmap: Infected People per Area')
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')

for i in range(100):
    worldsim.increment_one_day()

    for x in range(world.max_x):
        for y in range(world.max_y):
            area = world.world_grid[x][y]
            if area is not None:
                heatmap[x, y] = sum(1 for person in area.population if person.active_infection is not None)
            else:
                heatmap[x, y] = 0

    img.set_data(heatmap)
    cbar.update_normal(img)
    plt.pause(0.01)

plt.ioff()
plt.show()








