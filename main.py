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
        with open("input_map.txt", "rt+") as world_map:
            self.lines = []
            lines = world_map.readlines()
            for line in lines:
                world_map_line = []
                while line != "" and line != "\n":
                    world_map_line.append(Cell(symbol=line[0]))
                    line = line[1:]
                self.lines.append(world_map_line)

    def __repr__(self):
        output = ""
        
        for i in range(len(self.lines)):
            line_before = ""
            line = ""
            for j in range(len(self.lines[i])):
                line_before_repr = "  "
                line_repr = f"{repr(self.lines[i][j])}"
                
                
                if type(self.lines[i][j].ref) == Road:
                    if i - 1 >= 0:
                        if type(self.lines[i - 1][j].ref) != Road:
                            line_before_repr = line_before_repr[:1] + "-"
                            
                        if j - 1 >= 0:
                            if type(self.lines[i - 1][j - 1].ref) != Road:
                                line_before_repr = "+" + line_before_repr[1:]
                                
                            if type(self.lines[i - 1][j - 1].ref) == Road and type(self.lines[i - 1][j].ref) != Road:
                                line_before_repr = "+" + line_before_repr[1:]
                    if j - 1 >= 0:
                        if type(self.lines[i][j - 1].ref) != Road:
                            line_repr = "|" + line_repr[1:]
                            
                if type(self.lines[i][j].ref) != Road:
                    if i - 1 >= 0:
                        if type(self.lines[i - 1][j].ref) == Road:
                            line_before_repr = line_before_repr[:1] + "-"
                            
                        if j - 1 >= 0:
                            if type(self.lines[i - 1][j - 1].ref) == Road:
                                line_before_repr = "+" + line_before_repr[1:]
                    if j - 1 >= 0:
                        if type(self.lines[i][j - 1].ref) == Road:
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
    with open("output_map.txt", "wt+") as output_map:
        output_map.write(repr(world_map))
    
    

if __name__ == "__main__":
    main()