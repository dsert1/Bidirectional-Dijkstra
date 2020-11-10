import unittest
from bidi import bidi

tests = [
    ({0:{1: 3, 5: 5}, 1: {3: 3}, 3:{4: 3}, 4: {}, 5:{4: 5}}, 0, 4, 9),
    ({0: {1: 2, 3: 2, 4: 1}, 1: {0: 9, 3: 3, 4: 10, 1: 5, 2: 8}, 2: {1: 9, 3: 5, 2: 1}, 3: {0: 1}, 4: {1: 8}}, 4, 0, 12),
    ({0: {1: 18}, 1: {1: 7, 7: 30}, 2: {5: 19}, 3: {1: 28, 3: 1}, 4: {2: 24}, 5: {}, 6: {3: 7, 0: 1}, 7: {2: 22}, 8: {5: 0, 4: 9}}, 5, 7, None),
    ({0: {4: 3, 1: 0}, 1: {3: 1, 6: 4, 0: 6, 4: 2, 1: 2}, 2: {2: 2}, 3: {2: 4}, 4: {4: 8, 3: 5}, 5: {2: 1, 0: 2, 5: 3}, 6: {}}, 3, 5, None),
    ({0: {6: 5, 0: 4, 3: 9}, 1: {2: 5, 9: 9, 1: 7, 5: 0, 7: 6}, 2: {6: 2, 4: 10, 8: 2, 0: 4, 2: 8, 7: 10}, 3: {7: 7, 8: 8, 6: 10, 2: 5}, 4: {8: 8, 0: 9, 2: 1, 4: 3}, 5: {4: 3, 9: 9, 2: 0}, 6: {5: 7, 7: 5, 9: 8, 8: 8, 0: 4, 1: 1}, 7: {0: 2, 2: 8, 5: 7, 6: 3, 9: 3, 8: 7, 3: 4, 7: 2}, 8: {8: 5, 9: 0, 1: 4, 5: 3, 0: 6, 3: 10}, 9: {3: 10, 1: 4, 0: 7, 7: 9, 8: 4}}, 0, 9, 8)
]

def check(student, staff):
    return student == staff

class TestCases(unittest.TestCase):
    # def test_01(self):
    #     G, s, t, staff_sol = tests[0]
    #     student_sol = bidi(G, s, t)
    #     print('my sol: ', student_sol)
    #     print('staff sol: ', staff_sol)
    #     self.assertTrue(check(staff_sol, student_sol))


    def test_02(self):
        G, s, t, staff_sol = tests[1]
        student_sol = bidi(G, s, t)
        print('my sol: ', student_sol)
        print('staff sol: ', staff_sol)
        self.assertTrue(check(staff_sol, student_sol))


    def test_03(self):
        G, s, t, staff_sol = tests[2]
        student_sol = bidi(G, s, t)
        self.assertTrue(check(staff_sol, student_sol))


    def test_04(self):
        G, s, t, staff_sol = tests[3]
        student_sol = bidi(G, s, t)
        self.assertTrue(check(staff_sol, student_sol))


    def test_05(self):
        G, s, t, staff_sol = tests[4]
        student_sol = bidi(G, s, t)
        self.assertTrue(check(staff_sol, student_sol))


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)