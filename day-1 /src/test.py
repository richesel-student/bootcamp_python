import unittest
import ex00,  ex01, ex02

# from ex02 import decorator


class EX00TEST(unittest.TestCase):
    def test_ex00(self):
        test = {"gold_ingots": 3}
        test1 = {"gold_ingots": 4}
        result = ex00.add_ingot(test)
        self.assertEqual(result, test1)

class EX00TEST1(unittest.TestCase):
    def test1_ex00(self):
        zero = {}
        zero1 = {}
        test11 = {"gold_ingots": 4}
        result = ex00.add_ingot(zero)
        self.assertEqual(result, zero1)


class EX00TEST2(unittest.TestCase):
    def test2_ex00(self):
        zero = {}
        result = ex00.empty(zero)
        self.assertEqual(zero, result)

class EX00TEST3(unittest.TestCase):
    def test3_ex00(self):
        test11 = {"gold_ingots": 4}
        zero = {}
        result = ex00.empty(test11)
        self.assertEqual(zero, result)


class EX00TEST3(unittest.TestCase):
    def test3_ex00(self):
        test11 = {"gold_ingots": 4}
        zero = {}
        zero1 = {}
        result = ex00.empty(zero1)
        self.assertEqual(zero, result)
class EX00TEST4(unittest.TestCase):
    def test4_ex00(self):
        test11 = {"gold_ingots": 4}
        zero = {}
        zero1 = {}
        result = ex00.get_ingot(zero)
        self.assertEqual(zero, result)


class EX00TEST5(unittest.TestCase):
    def test5_ex00(self):
        test11 = {"gold_ingots": 4}
        zero = {}
        zero1 = {}
        result = ex00.get_ingot(zero)
        self.assertEqual(zero, result)
class EX00TEST6(unittest.TestCase):
    def test6_ex00(self):
        test = {"gold_ingots": 2}
        test1 = {"gold_ingots": 3}

        result = ex00.get_ingot(test1)
        self.assertEqual(test, result)

class EX00TEST7(unittest.TestCase):
    def test7_ex01(self):
        test = {"gold_ingots": 2}
        result = ex01.split_booty(test)
        self.assertEqual(test, result[0])

class EX00TEST8(unittest.TestCase):
    def test8_ex01(self):
        test1 = {"gold_ingots": 2}
        test2 = {"gold_ingots": 3}
        test3 = {"gold": 4}
        res = [{'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1}]


        combined_dict = [test1, test2, test3]

        result = ex01.split_booty(test1, test2, test3)
        for i in range(len(combined_dict)):
            self.assertEqual(res[i],  result[i])
class EX00TEST9(unittest.TestCase):
    def test9_ex01(self):
        res = [{'gold_ingots': 5}, {'gold_ingots': 5}, {'gold_ingots': 4}, {'gold_ingots': 4}]
        test1 = {"gold_ingots": 10}
        test2 = {"gold_ingots": 3}
        test3 = {"_ingots": 4}
        test4 = {"gold_ingots": 5}
        combined_dict = [test1, test2, test3, test4]
        result = ex01.split_booty(test1, test2, test3, test4)
        for i in range(len(combined_dict)):
            self.assertEqual(res[i],  result[i])


class EX00TEST11(unittest.TestCase):
    def test10_ex02(self):
        zero = {}
        result = ex02.empty(zero)
        self.assertTrue(result.startswith("SQUEAK"))
        self.assertIn("empty", result)

class EX00TEST12(unittest.TestCase):
    def test12_ex02(self):

        test = {"gold_ingots": 3}
        result = ex02.add_ingot(test)
        self.assertTrue(result.startswith("SQUEAK"))
        self.assertIn("add_ingot", result)

class EX00TEST13(unittest.TestCase):
    def test_ex13(self):

        test1 = {"gold_ingots": 3}
        result = ex02.get_ingot(test1)
        self.assertTrue(result.startswith("SQUEAK"))
        self.assertIn("get_ingot", result)

class EX00TEST14(unittest.TestCase):
    def test_ex14(self):

        test1 = {"gold_ingots": 3}
        result = ex02.get_ingot(test1)
        self.assertTrue(result.startswith("SQUEAK"))
        self.assertIn("get_ingot", result)
class EX00TEST15(unittest.TestCase):
    def test_ex15(self):

        test1 = {"gold_ingots": 3}
        result = ex02.split_booty(test1)
        self.assertTrue(result.startswith("SQUEAK"))
        self.assertIn("split_booty", result)





if __name__ == "__main__":
    unittest.main()
