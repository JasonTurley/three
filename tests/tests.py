import unittest
import three
from datetime import timedelta, date, datetime

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
        self.assertEqual(len(seventeen_threes), 17)

        thousand_threes = three.n_threes(1000)
        self.assertEqual(len(thousand_threes), 1000)

    def test_three_class(self):
        instance = three.Three()
        self.assertEqual(instance.any_instance_attribute, 3)
        self.assertEqual(instance.the_best_number, 3)

        self.assertEqual(three.Three.attributes_of_the_class_too, 3)
        self.assertEqual(three.Three.any_attribute, 3)

    # Language section tests

    def test_letters(self):
        self.assertEqual(three.letters(), ['t', 'h', 'r', 'e', 'e'])

    def test_spanish(self):
        self.assertEqual(three.spanish(), 'tres')

    def test_german(self):
        self.assertEqual(three.german(), 'drei')

    def test_french(self):
        self.assertEqual(three.french(), 'drois')

    def test_italian(self):
        self.assertEqual(three.italian(), 'tre')

    # Currency Section Tests

    def test_dollars(self):
        self.assertEqual(three.dollars(), '$3.00')

    def test_cents(self):
        self.assertEqual(three.cents(), '$0.03')

    def test_euros(self):
        self.assertEqual(three.euros(), '€3.00')

    # Rule of Threes section test

    def test_rule_of(self):
        self.assertEqual(three.rule_of(), 'Things that come in 3s are inherently more appealing.')

    def test_is_appealing(self):
        appealing_array = [1, "two", 3.00]
        self.assertEqual(three.is_appealing(appealing_array), True)

        unappealing_array = [1, "two", 3.00, "four?"]
        self.assertEqual(three.is_appealing(unappealing_array), False)


    def test_hours_from_now(self):
        expected_hour_min = (datetime.now() + timedelta(hours=3)).strftime('%H:%M')
        self.assertTrue(three.hours_from_now().startswith(expected_hour_min))

    def test_days_from_now(self):
        expected = (date.today() + timedelta(days=3)).strftime('%d %B %Y')
        self.assertEqual(three.days_from_now(), expected)

if __name__ == "__main__":
    unittest.main()
