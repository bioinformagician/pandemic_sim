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
    
    def __init__(self, areas = None):
        self.areas = areas if areas is not None else []
    
    def add_area(self, area):
        self.areas.append(area)
    
    def get_area_by_coordinates(self, x, y):
        for area in self.areas:
            if area.x_coordinate == x and area.y_coordinate == y:
                return area
        return None  # If not found

    
    def __repr__(self):
        return f"The world has {len(self.areas)} areas"
        
    
        
        
        
    
    