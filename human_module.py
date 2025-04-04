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
            "infected": False,
            "alive": True,
            "area": (random.uniform(-90, 90), random.uniform(-180, 180)),
            "bmi": self.random_bmi(),
            "smoker": random.choice([True, False]),
            "days_infected": 0,
            "resistance": self.random_resistance(),
            "previous_infections": []
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
    def __init__(self, infected, alive, area, age, bmi, smoker, days_infected, resistance, previous_infections):
        
        self.infected = infected
        self.alive = alive
        self.area = area
        self.age = age
        self.bmi = bmi
        self.smoker = smoker
        self.resistance = resistance
        self.previous_infections = previous_infections
        self.days_infected = days_infected
        self.update_health()
        
    def update_health(self):
        self.health = 100 - self.age 
            
        if self.smoker:
            self.health -= 20  
            
        if self.bmi > 40:
            self.health -= 10
                
        self.health = self.health
    
    
        
        
    def __repr__(self):
        return (f"Person(age={self.age}, bmi={self.bmi:.2f}, smoker={self.smoker}, "
                f"health={self.health}, infected={self.infected})")
        
        




class Virus:
    
    def __init__(self, name, infection_rate, mortality_rate, mutation_rate):
        
        self.name = name
        self.infection_rate = infection_rate
        self.mortality_rate = mortality_rate
        self.mutation_rate = mutation_rate
        
    def infect(self, person):
            
        if person.alive == False:
            return
            
        if person.infected:
            return
            
        if person.resistance > 80:
            person.infected = False
            return

        else:
            person.infected = True
            return
    
    def __repr__(self):
        return f"Virus Name: {self.name}, Infection Rate: {self.infection_rate}, Mortality Rate: {self.mortality_rate}, Mutation Rate: {self.mutation_rate}"
                 



class SimulateWorld:
    def __init__(self, virus, people):
        
        self.virus = virus
        self.people = people
        
        
    
    def increment_one_day(self):
        
        for person in self.people:
            
            if not person.alive:
                continue
            
            person.age +=1/365
                            
            #person.location +=1
            
            if person.infected:
                
                
                recovery_chance = 1-self.virus.mortality_rate*((person.resistance/100)+1)
                death_risk = self.virus.mortality_rate
                
                recovery_chance /= 7
                death_risk /=7
                
                no_change = 1 - (recovery_chance + death_risk)
                
                
                
                #also implement health here to calc the death risk
                outcomes = ["recover", "death", "no_change"]
                probabilities = [recovery_chance, death_risk, no_change]
                outcome = random.choices(outcomes, probabilities)[0]
                
                if outcome == "death":
                    person.alive = False
                    continue
                
                if outcome == "recover":
                    person.infected = False
                    person.previous_infections = person.previous_infections.append(self.virus.name)
                    person.days_infected = 0
                    continue
                
                if outcome == "no_change":
                    person.days_infected +=1

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