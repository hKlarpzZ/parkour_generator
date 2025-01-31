import random

class Cell:
    def __init__(self, symbol):
        if symbol == "_":
            self.ref = Empty()
        elif symbol == "X":
            self.ref = Road()
        else:
            self.ref = None
    
    def __repr__(self):
        if self.ref is not None:
            return repr(self.ref)
        return "ER"


class House:
    def __init__(self, width, height, floors):
        self.width = width
        self.height = height
        self.floors = floors
        
    def __repr__(self):
        return f" {self.floors}"


class Road:
    def __init__(self):
        pass
    
    def __repr__(self):
        return " X"
    
    
class Empty:
    def __init__(self):
        pass
    
    def __repr__(self):
        return " _"


class WorldMap:
    def __init__(self):
        
        self.road = House(0, 0, "X")
        
        with open("input_map.txt", "rt+") as world_map:
            self.lines = []
            lines = world_map.readlines()
            for line in lines:
                world_map_line = []
                while line != "" and line != "\n":
                    if line[0] == "X":
                        house_cell = Cell(symbol=line[0])
                        house_cell.ref = self.road
                        world_map_line.append(house_cell)
                    else:
                        world_map_line.append(Cell(symbol=line[0]))
                    line = line[1:]
                self.lines.append(world_map_line)


    def generate(self, house: House):
        x = random.randint(0, len(self.lines[0]) - house.width - 1)
        y = random.randint(0, len(self.lines) - house.height - 1)
        
        for i in range(y, house.height + y):
            for j in range(x, house.width + x):
                if type(self.lines[i][j].ref) != Empty:
                    return False
                
        for i in range(y, house.height + y):
            for j in range(x, house.width + x):
                self.lines[i][j].ref = house
                
        return True

    def __repr__(self):
        output = ""
        
        for i in range(len(self.lines)):
            line_before = ""
            line = ""
            for j in range(len(self.lines[i])):
                line_before_repr = "  "
                line_repr = f"{repr(self.lines[i][j])}"
                
                
                if type(self.lines[i][j].ref) == House:
                    if i - 1 >= 0:
                        if type(self.lines[i - 1][j].ref) != House or self.lines[i - 1][j].ref != self.lines[i][j].ref:
                            line_before_repr = line_before_repr[:1] + "-"
                            
                        if j - 1 >= 0:
                            if type(self.lines[i - 1][j - 1].ref) != House or self.lines[i - 1][j - 1].ref != self.lines[i][j].ref:
                                line_before_repr = "+" + line_before_repr[1:]
                                
                            if type(self.lines[i - 1][j - 1].ref) == House and (type(self.lines[i - 1][j].ref) != House or self.lines[i - 1][j - 1].ref != self.lines[i - 1][j].ref):
                                line_before_repr = "+" + line_before_repr[1:]
                    if j - 1 >= 0:
                        if type(self.lines[i][j - 1].ref) != House or self.lines[i][j - 1].ref != self.lines[i][j].ref:
                            line_repr = "|" + line_repr[1:]
                            
                if type(self.lines[i][j].ref) != House:
                    if i - 1 >= 0:
                        if type(self.lines[i - 1][j].ref) == House:
                            line_before_repr = line_before_repr[:1] + "-"
                            
                        if j - 1 >= 0:
                            if type(self.lines[i - 1][j - 1].ref) == House:
                                line_before_repr = "+" + line_before_repr[1:]
                    if j - 1 >= 0:
                        if type(self.lines[i][j - 1].ref) == House:
                            line_repr = "|" + line_repr[1:]
                            
                line_before += line_before_repr
                line += line_repr
            
            line_before += "\n"
            line += "\n"
            output += line_before
            output += line
                        
            
            
        return output


def main():
    world_map = WorldMap()
    
    gen_settings = dict()
    gen_settings["1*1"] = 5
    gen_settings["2*2"] = 6
    gen_settings["2*3"] = 9
    gen_settings["3*2"] = 9
    gen_settings["3*3"] = 3
    gen_settings["gen_tries"] = 128
    
    for i in range(gen_settings["3*3"]):
        house = House(3, 3, random.randint(1,3))
        for i in range(gen_settings["gen_tries"]):
            if world_map.generate(house):
                break
            
    for i in range(gen_settings["3*2"]):
        house = House(3, 2, random.randint(1,3))
        for i in range(gen_settings["gen_tries"]):
            if world_map.generate(house):
                break
            
    for i in range(gen_settings["2*3"]):
        house = House(2, 3, random.randint(1,3))
        for i in range(gen_settings["gen_tries"]):
            if world_map.generate(house):
                break
            
    for i in range(gen_settings["2*2"]):
        house = House(2, 2, random.randint(1,3))
        for i in range(gen_settings["gen_tries"]):
            if world_map.generate(house):
                break
    
    for i in range(gen_settings["1*1"]):
        house = House(1, 1, random.randint(1,3))
        for i in range(gen_settings["gen_tries"]):
            if world_map.generate(house):
                break
    
    with open("output_map.txt", "wt+") as output_map:
        output_map.write(repr(world_map))
    
    

if __name__ == "__main__":
    main()