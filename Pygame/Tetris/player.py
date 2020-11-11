from board import Direction, Rotation
from random import Random
import time

class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)


    def choose_action(self, board):
        print("cells:",board.cells)
        print("falling:",board.falling.cells)
        print("next:",board.next.cells)
        time.sleep(1)
        return self.random.choice([
            Direction.Left,
            Direction.Right,
            Direction.Down,
            Rotation.Anticlockwise,
            Rotation.Clockwise,
        ])

class CPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    def collide(self, block, board):
        for cell in block.cells:
            if cell[0] >= board.width or cell[0] < 0\
                or cell[1] >= board.height or cell[1] < 0:
                return True

            sandbox = board.clone()

            if block.collides(sandbox.cells):
                return True
        return False


    def row_transition(self, board):
        transition = 0
        for j in range(24):
            for i in range(9):
                if ((i,j) not in board.cells) and ((i+1,j) in board.cells):
                    transition += 1
                if ((i,j) in board.cells) and ((i+1,j) not in board.cells):
                    transition += 1
        return transition

    def col_transition(self, board):
        transition = 0
        for i in range(10):
            for j in range(23):
                if ((i,j) not in board.cells) and ((i,j+1) in board.cells):
                    transition += 1
                if ((i,j) in board.cells) and ((i,j+1) not in board.cells):
                    transition += 1
        return transition
    
    def get_holes(self, board):
        holes = 0
        for i in range(10):
            col_holes = -1
            for j in range(24):
                if col_holes == -1 and ((i,j) in board.cells):
                    col_holes = 0
                if col_holes != -1 and ((i,j) not in board.cells):
                    col_holes += 1
            if col_holes != -1:
                holes += col_holes
        return holes

    def get_wells(self, board):
        sum_n = [0,1,3,6,10,15,21,28,36,45,55,66,78,91,\
            105,120,136,153,171,190,210,231,253,276,300,]
        wells = 0
        col_wells = 0
        for i in range(10):
            for j in range(24):
                if (i,j) not in board.cells:
                    if ((i-1<0) or (i-1,j) in board.cells) and\
                        ((i+1>9) or (i+1,9) in board.cells):
                        col_wells += 1
                else:
                    wells += sum_n[col_wells]
                    col_wells = 0
        return wells

    def get_possible_position(self, board):
        positions = []
        sandbox_1 = board.clone()
        line = sandbox_1.height-1

        for j in range(6):
            sandbox_1.falling.move(Direction.Left,sandbox_1)
        for i in range(4):
            sandbox_2 = sandbox_1.clone()
            for k in range(10):
                sandbox_3 = sandbox_2.clone()
                sandbox_3.falling.move(Direction.Drop,sandbox_3)
                sandbox_4 = sandbox_3.clone()
                sandbox_4.land_block()
                
                cnt = 0
                useful_blocks = 0
                while line > 0:

                    if sandbox_4.line_full(line):
                        cnt += 1
                        for cell in sandbox_3.falling.cells:
                            if cell[1] == line:
                                useful_blocks += 1

                    line -= 1

                height = board.height-1-sandbox_3.falling.center[1]
                eliminated = useful_blocks * cnt
                row = self.row_transition(sandbox_4)
                col = self.col_transition(sandbox_4)
                hole = self.get_holes(sandbox_4)
                well = self.get_wells(sandbox_4)

                positions.append({
                    "Height": height,
                    "Eliminated": eliminated,
                    "Row_transitions": row,
                    "Col_transitions": col,
                    "Holes": hole,
                    "Wells": well,
                    "Move": int(sandbox_3.falling.center[0]-board.falling.center[0]),
                    "Rotation": i,
                    })

                sandbox_2.falling.move(Direction.Right,sandbox_2)
            sandbox_1.falling.rotate(Rotation.Clockwise,sandbox_1)
            sandbox_1.falling.move(Direction.Left,sandbox_1)
        return positions



    def choose_action(self, board):
        sandbox = board.clone()

        positions = self.get_possible_position(sandbox)
        actions = []
        best_score = -999999
        for i in range(len(positions)):
            score = -4.500158825082766*positions[i]["Height"]+\
                3.4181268101392694*positions[i]["Eliminated"]\
                -3.2178882868487753*positions[i]["Row_transitions"]\
                -9.348695305445199*positions[i]["Col_transitions"]\
                -7.899265427351652*positions[i]["Holes"]  \
                -3.3855972247263626*positions[i]["Wells"]
            if score > best_score:
                best_score = score
                idx = i

        move = Direction.Left if positions[idx]["Move"]<0 else Direction.Right

        for i in range(positions[idx]["Rotation"]):
            actions.append(Rotation.Clockwise) 

        for i in range(abs(positions[idx]["Move"])):
            actions.append(move) 
        
        actions.append(Direction.Drop)

        #time.sleep(1)
        return (actions)

#SelectedPlayer = RandomPlayer
SelectedPlayer = CPlayer