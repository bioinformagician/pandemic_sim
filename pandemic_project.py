from human_module import *
from world_module import *


influenza = Virus(**influenza_virus_blueprint) 
corona = Virus(**corona_virus_blueprint)        

european = EuropeanPopulation()


europeans = [Person(**european.generate_person_dict()) for _ in range(300000)]

[corona.infect(person) for person in europeans]




world = World(None)

n_columns = 100
n_rows = 100

for column in range(n_columns):
    for row in range(n_rows):
        area = Area(hospital=True, income=100, x_coordinate = column, y_coordinate = row, population = None)    
        world.add_area(area)

for eurpean in europeans:
    patch = random.randint(0,(n_columns*n_rows)-1)
    world.areas[patch].add_person(european)
    european.area = world.areas[patch].get_coordinates()
    
    
    




worldsim = SimulateWorld(corona, europeans)



for i in range(1):
    worldsim.increment_one_day()


dead = 0
alive = 0
infected = 0
for person in europeans:
    if person.alive:
        alive +=1
        
        if person.infected:
            infected +=1
    else:
        dead +=1

print(f"{alive} people are alive and {dead} are dead, death percentage of {round(dead/alive, 2)}% and {infected} are currently infected")

