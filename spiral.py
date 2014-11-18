LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3


def change_state(prev_state):
    if prev_state == LEFT:
        return DOWN
    elif prev_state == DOWN:
        return RIGHT
    elif prev_state == RIGHT:
        return UP
    elif prev_state == UP:
        return LEFT
    raise ValueError(prev_state)


def new_direction(x, y, state):
    if state == LEFT:   return (x+1, y)
    if state == RIGHT:  return (x-1, y)
    if state == UP:     return (x, y-1)
    if state == DOWN:   return (x, y+1)


def spiral(rows, cols):
    # initialize empty array
    result = [[0] * cols for row in xrange(rows)]

    # initial state
    x, y = (0, 0)
    state = LEFT
    counter = 1

    # adjust for first step taken
    moves = cols-1

    while cols > 0 and rows > 0:
        while moves > 0:
            result[y][x] = counter
            x, y = new_direction(x, y, state)
            moves -= 1
            counter += 1

        state = change_state(state)
        if state in (UP, DOWN):
            rows -= 1
            moves = rows
        elif state in (LEFT, RIGHT):
            cols -= 1
            moves = cols

    result[y][x] = counter
    return result


import unittest

class TestSpiral(unittest.TestCase):

    def test_54(self):
        expected = [
            [  1,  2,  3,  4],
            [ 14, 15, 16,  5],
            [ 13, 20, 17,  6],
            [ 12, 19, 18,  7],
            [ 11, 10,  9,  8]
        ]
        result = spiral(5, 4)
        self.assertEqual(expected, result)

    def test_22(self):
        expected = [
            [1, 2],
            [4, 3]
        ]
        result = spiral(2, 2)
        self.assertEqual(expected, result)

    def test_41(self):
        expected = [
            [1],
            [2],
            [3],
            [4]
        ]
        result = spiral(4, 1)
        self.assertEqual(expected, result)

    def test_33(self):
        expected = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
        result = spiral(3, 3)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()