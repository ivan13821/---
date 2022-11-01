import unittest
from func import get_number_from_index, get_empty_list, blocks, get_index_from_number, is_zero_in_mas, move_left,move_up, move_down, can_move, score

class test_2048(unittest.TestCase):
    def test_1 (self):
        self.assertEqual(get_number_from_index(1, 2), 7)
    def test_2 (self):
        self.assertEqual(get_number_from_index(3, 3), 16)
    def test_3 (self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4 (self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5 (self):
        self.assertEqual(get_index_from_number(1), (0, 0))
    def test_6 (self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_7 (self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), False)
    def test_8 (self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)
    def test_9 (self):
        a = []
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_10 (self):
        a = []
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        res = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(f'{move_left(mas)}', res)

    def test_11 (self):
        a = []
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        res = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), res)

    def test_12 (self):
        a = []
        mas = [
            [2, 2, 0, 4],
            [2, 4, 4, 4],
            [0, 4, 0, 0],
            [0, 0, 0, 0]
        ]
        res = [
            [4, 2, 4, 8],
            [0, 8, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), res)
    def test_13 (self):
        a = []
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 8],
            [0, 0, 0, 8],
            [4, 0, 0, 0]
        ]
        res = [
            [2, 2, 4, 16],
            [4, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), res)

    def test_14 (self):
        a = []
        mas = [
            [4, 2, 4, 0],
            [0, 4, 4, 8],
            [0, 0, 0, 8],
            [4, 0, 0, 0]
        ]
        res = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2, 0, 0],
            [8, 4, 8, 16]
        ]
        self.assertEqual(move_down(mas), res)

    def test_15 (self):
        a = []
        mas = [
            [2, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(can_move(mas), True)

    def test_16 (self):
        a = []
        mas = [
            [2, 2, 0, 0],
            [0, 4, 0, 0],
            [0, 0, 16, 0],
            [0, 0, 0, 32]
        ]
        self.assertEqual(score(mas), 56)