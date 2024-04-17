from copy import deepcopy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

"""
def main():
    building = generate_building()
    grid = convert_text_to_pathfinding_grid(building)
    for floor in grid:
        print()
        for row in floor:
            print(row)
"""

#def generate_building():
    # w is wall
    # h is half-wall
    # o is obstacle
    # m is mini-object
    # n is normal-object
    # l is large-object
    # d is door
    # s is stair
    # g is glass
    # ' ' is empty space
    # e is for exit
    # p evacuation plan marker
    # 1 is room indicator
    # 2 is hall indicator

"""
    building = [
        [
            [' ','w','w','w','w'],
            [' ',' ',' ',' ','w'],
            ['w','w','w',' ',' '],
        ],
        [
            [' ', 'w', 'w', 'w', 'w'],
            [' ', ' ', ' ', ' ', 'w'],
            ['w', 'w', 'w', ' ', ' '],
        ]
    ]



    building1 = [
        [

            #21 by 31
            ['w','w','g','g','g','g','g','w','w','w','w','w','g','w','w','w','g','w','w','w','g','g','g','g','g','g','g','w','w','w','w'],
            ['w','l','l','l','l','l',' ',' ','h',' ','w','m','n','m','w',' ','m',' ','w','p',' ',' ',' ',' ',' ',' ',' ','p','d','1','e'],
            ['g','l',' ',' ',' ',' ',' ',' ','h',' ','w',' ',' ',' ','w',' ','n','n','w',' ',' ',' ',' ',' ',' ',' ',' ','2','w',' ','w'],
            ['g','l',' ','n','n','n',' ',' ','h',' ','w',' ',' ',' ','w',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ','w','s','w'],
            ['g','l',' ','n','n','n',' ',' ','h',' ','w',' ','1','p','w','p','1','m','w',' ',' ',' ','w','w','w','w','w','w','w','w','w'],
            ['g',' ',' ',' ',' ',' ',' ',' ','h',' ','w','w','w','d','w','d','w','w','w',' ',' ',' ','h','l','n','l','w',' ',' ',' ','w'],
            ['w',' ',' ',' ',' ',' ',' ',' ','w',' ',' ',' ',' ','1',' ','1',' ',' ','w',' ',' ',' ','h','l','n','l','w',' ',' ',' ','g'],
            ['w','w','w',' ',' ',' ',' ',' ','w',' ','p','1',' ',' ','p',' ',' ',' ','w',' ',' ',' ','h','l','n','l','w',' ',' ',' ','g'],
            ['w',' ','w',' ',' ',' ',' ',' ','w','w','d','w','w','w','d','w','w','w','w',' ',' ',' ',' ',' ',' ',' ','h',' ',' ',' ','g'],
            ['w',' ','w','2',' ',' ',' ',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ',' ','p',' ',' ',' ',' ',' ','m','h',' ',' ',' ','g'],
            ['e','1','d','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','m','h',' ','1','p','w'],
            ['w',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','m','h','h','h','d','w'],
            ['w',' ','w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','2','w'],
            ['w','w','w',' ',' ','2',' ','2',' ',' ',' ',' ',' ',' ',' ','p',' ',' ',' ',' ','p',' ','h','l','n','l','h','l','n','l','w'],
            ['w','w','w','w','w','d','w','d','w','w','w','w','w','w','w',' ','w','w','w','w',' ',' ','h','l','n','l','h','l','n','l','w'],
            ['w',' ',' ',' ','1','p','w','p','1',' ',' ',' ','w',' ','w',' ','w',' ',' ','w',' ',' ','h','l','n','l','h','l','n','l','w'],
            ['g',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ','w',' ','w',' ','w',' ',' ','w',' ',' ','w','w','w','w','w','w','w','w','w'],
            ['g',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ','w',' ','w',' ','w',' ',' ','w',' ',' ',' ',' ',' ',' ',' ',' ','w','s','w'],
            ['g',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ','w','1','w',' ','w','1',' ','w',' ',' ',' ',' ',' ',' ',' ','2','w',' ','w'],
            ['w',' ',' ',' ',' ',' ','w',' ',' ',' ',' ',' ','w','p','d','2','d','p',' ','w','p',' ',' ',' ',' ',' ',' ','p','d','1','e'],
            ['w','w','g','g','g','w','w','w','g','g','g','w','w','w','w','e','w','w','w','w','w','g','g','g','g','g','g','w','w','w','w'],
        ],
        [
            ['w','w','g','g','g','g','g','g','w','w','w','g','g','w','w','w','g','g','w','w','w','g','g','g','g','g','g','w','w','w','w'],
            ['w',' ',' ',' ',' ',' ','m','n','m','w','m','n','m',' ','w','l','l','l',' ','w','p',' ',' ',' ',' ',' ',' ','p','d','1','w'],
            ['g','m',' ',' ','w','1',' ',' ',' ','w',' ',' ',' ','1','w','l',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','2','w',' ','w'],
            ['g','l',' ',' ','w','p','m','n','m','w','m','n','m','p','w','l',' ',' ',' ','w',' ',' ',' ','2',' ',' ',' ',' ','w','s','w'],
            ['g','l',' ',' ','w','d','w','w','w','w','w','w','w','d','w',' ',' ',' ','l','w',' ',' ','w','d','w','w','w','w','w','w','w'],
            ['w','l',' ','1','w','2',' ',' ',' ',' ',' ',' ',' ','2','w','1',' ',' ','l','w',' ','2','d','p',' ',' ',' ',' ',' ',' ','w'],
            ['w','l','l','p','w',' ',' ',' ',' ','p',' ',' ',' ',' ','w','p','l','l','l','w',' ',' ','w','1','m',' ','m',' ','m',' ','g'],
            ['w','w','w','d','w',' ','w','w','w','w','w','w','w',' ','w','d','w','w','w','w',' ',' ','w',' ','l','l','l','l','l',' ','g'],
            ['w','m','w','2',' ',' ','w',' ',' ',' ',' ',' ','w',' ',' ','2',' ',' ',' ',' ',' ',' ','w',' ','l','l','l','l','l',' ','g'],
            ['g',' ','w',' ',' ',' ','w','2','m','n','m',' ','w','2',' ',' ',' ',' ',' ',' ',' ',' ','w',' ','m',' ','m',' ','m',' ','g'],
            ['g','p','d','2',' ','2','d','p',' ','n',' ','p','d','p',' ',' ',' ',' ',' ',' ','p',' ','w',' ',' ',' ',' ',' ',' ',' ','g'],
            ['w',' ','w',' ',' ',' ','w',' ','m','n','m','1','w',' ',' ',' ',' ',' ',' ',' ',' ',' ','w',' ','m',' ','m',' ','m',' ','g'],
            ['w','m','w','2',' ',' ','w',' ',' ',' ',' ',' ','w',' ',' ','2',' ',' ',' ',' ',' ',' ','w',' ','l','l','l','l','l',' ','g'],
            ['w','w','w','d','w',' ','w','w','w','w','w','w','w',' ','w','d','w','w','w','w',' ',' ','w',' ','l','l','l','l','l',' ','g'],
            ['w','m','1','p','w',' ',' ',' ',' ','p',' ',' ',' ',' ','w','p','l','l','l','w',' ',' ','w','1','m',' ','m',' ','m',' ','g'],
            ['w','n',' ',' ','w','2',' ',' ',' ',' ',' ',' ',' ','2','w','1',' ',' ','l','w',' ','2','d','p',' ',' ',' ',' ',' ',' ','w'],
            ['g','m',' ',' ','w','d','w','w','w','w','w','w','w','d','w',' ',' ',' ','l','w',' ',' ','w','d','w','w','w','w','w','w','w'],
            ['g',' ',' ',' ','w','p','m','n','m','w','m','n','m','p','w','l',' ',' ','l','w',' ',' ',' ','2',' ',' ',' ',' ','w','s','w'],
            ['g',' ',' ',' ','w','1',' ',' ',' ','w',' ',' ',' ','1','w','l',' ',' ',' ','w',' ',' ',' ',' ',' ',' ',' ','2','w',' ','w'],
            ['w','m','n','m','w',' ','m','n','m','w','m','n','m',' ','w','l','l','l',' ','w','p',' ',' ',' ',' ',' ',' ','p','d','1','w'],
            ['w','w','g','w','w','w','g','g','w','w','w','g','g','w','w','w','w','g','w','w','w','g','g','g','g','g','g','w','w','w','w'],
        ],
        [
            ['w','w','w','w','w','g','w','w','w','g','w','w','w','w','w','w','w','w','w','g','w','w','w','g','w','w','w','w','w','w','w'],
            ['w','l','l','w',' ','n',' ','w',' ','n',' ','w',' ','m','w','m',' ','w',' ','n',' ','w',' ','n',' ','w',' ','p','d','1','w'],
            ['g','l',' ','w',' ','n','m','w',' ','n','m','w',' ','n','w','n',' ','w','m','n',' ','w','m','n',' ','w',' ',' ','w',' ','w'],
            ['g','l',' ','w','p','1',' ','w','p','1',' ','w','p','1','w','1','p','w',' ','1','p','w',' ','1','p','w',' ',' ','w','s','w'],
            ['g','l','1','w','d','w','w','w','d','w','w','w','d','w','w','w','d','w','w','w','d','w','w','w','d','w',' ',' ','w','w','w'],
            ['w','l','p','d','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ',' ',' ','w'],
            ['w','w','w','w',' ','p',' ',' ',' ','2',' ','2',' ',' ','p',' ',' ','p',' ',' ','2',' ','2',' ',' ',' ','p',' ',' ','2','w'],
            ['w','m','p','d','2',' ','w','w','w','d','w','d','w','w','w',' ',' ','w','w','w','d','w','d','w','w','w',' ','w','w','d','w'],
            ['g','n','1','w',' ',' ','w',' ','1','p','w','p','1',' ','w',' ',' ','w',' ','1','p','w','p','1',' ','w',' ','w','1','p','w'],
            ['g','m',' ','w',' ',' ','w','1',' ',' ','w',' ',' ','1','w',' ',' ','w','1',' ',' ','w',' ',' ','1','w',' ','w','1','m','g'],
            ['g',' ',' ','w',' ','2','d','p',' ',' ','w',' ',' ','p','d','2','2','d','p',' ',' ','w',' ',' ','p','d','2','d','p','n','g'],
            ['g','m',' ','w',' ',' ','w',' ',' ',' ','w',' ',' ',' ','w',' ',' ','w',' ',' ',' ','w',' ',' ',' ','w',' ','w',' ','m','g'],
            ['g','n','1','w',' ',' ','w',' ','1','p','w','p','1',' ','w',' ',' ','w',' ','1','p','w','p','1',' ','w',' ','w','1','p','w'],
            ['w','m','p','d','2',' ','w','w','w','d','w','d','w','w','w',' ',' ','w','w','w','d','w','d','w','w','w',' ','w','w','d','w'],
            ['w','w','w','w',' ','p',' ',' ',' ','2',' ','2',' ',' ','p',' ',' ','p',' ',' ','2',' ','2',' ',' ',' ','p',' ',' ','2','w'],
            ['w','l','p','d','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ','2',' ',' ',' ',' ',' ','w'],
            ['g','l','1','w','d','w','w','w','d','w','w','w','d','w','w','w','d','w','w','w','d','w','w','w','d','w',' ',' ','w','w','w'],
            ['g','l',' ','w','p','1',' ','w','p','1',' ','w','p','1','w',' ','p','w',' ','1','p','w',' ','1','p','w',' ',' ','w','s','w'],
            ['g','l',' ','w',' ','n','m','w',' ','n','m','w',' ','n','w','n','1','w','m','n',' ','w','m','n',' ','w',' ','2','w',' ','w'],
            ['w','l','l','w',' ','n',' ','w',' ','n',' ','w',' ','m','w','m',' ','w',' ','n',' ','w',' ','n',' ','w',' ','p','d','1','w'],
            ['w','w','w','w','w','g','w','w','w','g','w','w','w','w','w','w','w','w','w','g','w','w','w','g','w','w','w','w','w','w','w'],
        ],
        # [
        #     ['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w','s','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w','w','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w','w','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w','s','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','w',' ','w'],
        #     ['w',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',',' ',' ',',' ',' ',',' 'd',' ','w'],
        #     ['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','e','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
        # ],
        ]
    return building
"""

def convert_text_to_pathfinding_grid(text_building):
    # 0 is impassable
    # 1 is easily passable
    # 2 is passable
    # 3 is difficultly passable
    grid = deepcopy(text_building)
    floors = len(grid)
    for floor in range(floors):
        for row in grid[floor]:
            for col in range(len(row)):
                if row[col] == 'f':
                    row[col] = -2
                elif row[col] == 'w' or row[col] == 'g' or row[col] == 'l':
                    row[col] = 0
                elif row[col] == ' ' or row[col] == 'd' or row[col] == 'e' or row[col] == 's' or row[col] == 'p' or row[col] == '1' or row[col] == '2':
                    row[col] = 1
                elif row[col] == 'h' or row[col] == 'm':
                    row[col] = 2
                elif row[col] == 'n':
                    row[col] = 3
    return grid

def main():

    matrix = [#[
        #[1,0,0,0,0],
       # [1,1,3,1,1],
       #[0,0,2,0,0],
       # ],
        [
        [' ', 'w', 'w', 'w', 'w'],
        [' ', ' ', ' ', ' ', 'w'],
        ['w', 'w', 'w', ' ', ' '],
        ]
    ]
    grid = deepcopy(matrix)
    floors = len(grid)
    for floor in range(floors):
        for row in grid[floor]:
            for col in range(len(row)):
                if row[col] == 'f':
                    row[col] = -2
                elif row[col] == 'w' or row[col] == 'g' or row[col] == 'l':
                    row[col] = 0
                elif row[col] == ' ' or row[col] == 'd' or row[col] == 'e' or row[col] == 's' or row[col] == 'p' or row[col] == '1' or row[col] == '2':
                    row[col] = 1
                elif row[col] == 'h' or row[col] == 'm':
                    row[col] = 2
                elif row[col] == 'n':
                    row[col] = 3
    return grid
    print(" ")
    print(matrix)
    grid = Grid(matrix=matrix[0])
    start = grid.node(0, 0)
    end = grid.node(4, 1)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)
    for node in path:
        print(node.x, node.y)


if __name__ == '__main__':
    main()