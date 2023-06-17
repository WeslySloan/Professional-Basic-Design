class Cube:
    def __init__(self, side):
        self.side = side
    def get_side(self):
        return self.side
    def get_outside_area(self):
        return 6 * self.side * self.side
    def get_volume(self):
        return self.side * self.side * self.side

inputs = []
while True:
    try:
        side = int(input())
        inputs.append(side)
    except EOFError:
        break

for side in inputs:
    cube = Cube(side)
    area = cube.get_outside_area()
    volume = cube.get_volume()
    print(f"Side length = {side}, Area = {area}, Volume = {volume}")
