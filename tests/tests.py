import unittest
import three

class TestThree(unittest.TestCase):
    def test_three(self):
        self.assertEqual(three.three(), 3, "Should equal three.")
        self.assertNotEqual(three.three(), 4, "Should not equal three.")


    def test_squared(self):
        self.assertEqual(three.squared(), 3 ** 2, "Should equal 9.")


    def test_cubed(self):
        self.assertEqual(three.cubed(), 3 ** 3, "Should equal 27.")


    def test_dozen(self):
        self.assertEqual(three.dozen(), 3 * 12, "Should equal 36.")


    def test_binary(self):
        self.assertEqual(three.binary(), bin(3))


    def test_factorial(self):
        self.assertEqual(three.factorial(), 3 * 2 * 1)


    def test_is_three(self):
        self.assertTrue(three.is_three(3), "Should be true.")


    def test_filter(self):
        test_items = [1, 3, None, True, "happy", 3]
        self.assertEqual(three.filter(test_items),
                            list(filter(three.is_three, test_items)),
                            "The two lists should be the same.")


    def test_map(self):
        test_items = [1, 3, None, True, "happy", 3]
        self.assertEqual(three.map(test_items),
                            list(map(lambda x: 3, test_items)),
                            "The two lists should be the same.")


    def test_reduce(self):
        test_items = [1, 3, None, True, "happy", 3]
        self.assertEqual(three.reduce(test_items), 3)

    def test_force_three(self):

        @three.force_three
        def function_about_four():
            return 4

        self.assertEqual(function_about_four(), 3)

    def test_n_threes(self):
        seventeen_threes = three.n_threes(17)
        self.assertEqual(len(some_threes), 17)

        thousand_threes = three.hand_me_some_threes(1000)
        self.assertEqual(len(some_threes), 1000)



if __name__ == "__main__":
    unittest.main()
