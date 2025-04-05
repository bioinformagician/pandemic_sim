from world_module import *
import random

class Population:
    def __init__(self, region):
        self.region = region

    def random_age(self):
        return round(random.gauss(40, 15))

    def random_bmi(self):
        return random.gauss(21, 5)

    def random_resistance(self):
        return random.gauss(0, 15)

    def generate_person_dict(self):
        return {
            "age": self.random_age(),
            "alive": True,
            "area": {"x": None, "y": None},
            "bmi": self.random_bmi(),
            "smoker": random.choice([True, False]),
            "days_infected": 0,
            "resistance": self.random_resistance(),
            "previous_infections": [],
            "active_infection": None
        }



class EuropeanPopulation(Population):
    def __init__(self):
        super().__init__("Europe")

    def random_age(self):
        return round(random.gauss(45, 10))
    
    def random_bmi(self):
        return round(random.gauss(24, 3), 2)

class AfricanPopulation(Population):
    def __init__(self):
        super().__init__("Africa")

    def random_age(self):
        return round(random.gauss(35, 12))
    
    def random_bmi(self):
        return round(random.gauss(22, 4), 2)

class EastAsianPopulation(Population):
    def __init__(self):
        super().__init__("East Asia")

    def random_age(self):
        return round(random.gauss(40, 10))
    
    def random_bmi(self):
        return round(random.gauss(23, 3), 2)

class SouthAmericanPopulation(Population):
    def __init__(self):
        super().__init__("South America")

    def random_age(self):
        return round(random.gauss(38, 11))
    
    def random_bmi(self):
        return round(random.gauss(25, 3), 2)





class Person:
    def __init__(self, alive, area, age, bmi, 
                 smoker, days_infected, resistance, previous_infections, 
                 active_infection):
        
        self.alive = alive
        self.area = area
        self.age = age
        self.bmi = bmi
        self.smoker = smoker
        self.resistance = resistance
        self.previous_infections = previous_infections
        self.active_infection = active_infection
        self.days_infected = days_infected
        self.update_health()
        
    def update_health(self):
        self.health = 100 - self.age 
            
        if self.smoker:
            self.health -= 20  
            
        if self.bmi > 40:
            self.health -= 10
                
        self.health = self.health
    
    def transmit_disease(self, people_closeby):
        #infect n people, n = infection_rate
        #the number of people subject to infection should be picked as gaussian with mean = infection_rate and std = 1
        if people_closeby is None:
            return
        
        if self.active_infection is not None:
            n_people = max(0, round(random.gauss(self.active_infection.infection_rate, 1)))

            if n_people == 0:
                return
            
            if n_people > len(people_closeby):
                n_people = len(people_closeby)

            people_subject_to_infection = random.sample(people_closeby, n_people)
            
            for person in people_subject_to_infection:
                self.active_infection.infect(person)

            
    
    
    def __repr__(self):
        return (f"Person(age={self.age}, bmi={self.bmi:.2f}, smoker={self.smoker}, "
                f"health={self.health})")
        
        




class Virus:
    
    def __init__(self, name, infection_rate, mortality_rate, mutation_rate):
        
        self.name = name
        self.infection_rate = infection_rate
        self.mortality_rate = mortality_rate
        self.mutation_rate = mutation_rate
        
    def infect(self, person):
        if not person.alive:
            return
                
        if person.resistance > 80:
            return

        previous_infection_names = [infection.name for infection in person.previous_infections]
        if self.name in previous_infection_names:
            return

        if person.active_infection is not None:
            return

        person.active_infection = self
    
    def __repr__(self):
        return f"Virus Name: {self.name}, Infection Rate: {self.infection_rate}, Mortality Rate: {self.mortality_rate}, Mutation Rate: {self.mutation_rate}"
                 



influenza_virus_blueprint = {
    "name": "Influenza",
    "infection_rate": 1.5,
    "mortality_rate": 0.01,
    "mutation_rate": 0.2
}

corona_virus_blueprint = {
    "name": "COVID-19",
    "infection_rate": 2,
    "mortality_rate": 0.02,
    "mutation_rate": 0.1
}