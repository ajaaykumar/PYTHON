import unittest
from A_Unique_String import Solution 

class Test_A_Unique_String(unittest.TestCase):
    try:
        def first_Test_Case(self):
            obj = Solution()
            result = obj.solve("abcd")
            self.assertEqual(result,True)

        def second_Test_Case(self):
            obj = Solution()
            result = obj.solve("")
            self.assertEqual(result,True)

        def third_Test_Case(self):
            obj = Solution()
            result = obj.solve("aab")
            self.assertEqual(result,False)

    except Exception as err:
        print("Error: "+str(err))

if __name__ == '__main__':
    unittest.main()

