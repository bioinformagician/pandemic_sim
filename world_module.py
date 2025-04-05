import random

class Area:
    
    def __init__(self, hospital, income, x_coordinate, y_coordinate, population = None):
        self.hospital = hospital
        self.income = income
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.population = population if population is not None else []
        
    def add_person(self, person):
        self.population.append(person)
    
    def get_coordinates(self):
        return {"x": self.x_coordinate,
                "y": self.x_coordinate}
    
    def __repr__(self):
        return f"The area has {len(self.population)} people, an income of {self.income} and the cooridnates {self.x_coordinate, self.y_coordinate}, and hospital = {self.hospital}"
    

class World:
    
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        #initiate as empty dict of dicts
        self.world_grid = {}

        for i in range(max_x):
            self.world_grid[i] = {}
            for j in range(max_y):
                self.world_grid[i][j] = None
        
    def add_area(self, area):
        x = area.x_coordinate
        y = area.y_coordinate

        if x > self.max_x or y > self.max_y:
            raise ValueError("Coordinates are out of bounds")
        
        if self.world_grid[x][y] is not None:
            raise ValueError("Area already exists at these coordinates")
        
        self.world_grid[x][y] = area


    def get_area_by_coordinates(self, x, y):
        return self.world_grid.get(x, {}).get(y, None)

    
    def __repr__(self):
        return f"The world has {self.max_x} x {self.max_y} areas, and the areas are {self.world_grid}"
        
    

class SimulateWorld:
    def __init__(self, people, world):
        
        self.people = people
        self.world = world
    
    def move_person(self, person):

        x_increase = random.randint(-1, 1)
        y_increase = random.randint(-1, 1)

        new_x = person.area.x_coordinate + x_increase
        new_y = person.area.y_coordinate + y_increase

        if new_x > self.world.max_x-1:
            new_x = 1
        
        if new_x < 0:
            new_x = self.world.max_x-1
        
        if new_y > self.world.max_y-1:
            new_y = 1
        
        if new_y < 0:
            new_y = self.world.max_y-1
        
        new_area = self.world.get_area_by_coordinates(new_x, new_y)

        if new_area is not None:
            person.area.population.remove(person)
            new_area.add_person(person)
            person.area = new_area
        
        else:
            raise ValueError("New area does not exist")
        
    
    def increment_one_day(self):
        
        for person in self.people:
            
            if not person.alive:
                continue
            
            person.age +=1/365

            self.move_person(person)

            if person.active_infection is not None:

                #transmit disease

                people_closeby = person.area.population
                person.transmit_disease(people_closeby)
                
                
                recovery_chance = 1-person.active_infection.mortality_rate*((person.resistance/100)+1)
                death_risk = person.active_infection.mortality_rate
                
                recovery_chance /= 3
                death_risk /=3
                
                no_change = 1 - (recovery_chance + death_risk)
                
                
                
                #also implement health here to calc the death risk
                outcomes = ["recover", "death", "no_change"]
                probabilities = [recovery_chance, death_risk, no_change]
                outcome = random.choices(outcomes, probabilities)[0]
                
                if outcome == "death":
                    person.alive = False
                    continue
                
                if outcome == "recover":
                    person.previous_infections.append(person.active_infection)
                    person.active_infection = None
                    person.days_infected = 0
                    continue
                
                if outcome == "no_change":
                    person.days_infected +=1
        
        
    
    