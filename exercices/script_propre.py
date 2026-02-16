import unittest
from typing import List

"""
Count names with more than a given number of letters.
"""


MIN_NAME_LENGTH: int = 7  # évite le "magic number"


def count_names_longer_than(prenoms: List[str], min_length: int = MIN_NAME_LENGTH) -> int:
    """
    Retourne le nombre de prénoms dont la longueur est strictement supérieure à min_length.
    """
    return sum(1 for prenom in prenoms if len(prenom) > min_length)


class TestNamesMethod(unittest.TestCase):
    def test_count_names_longer_than(self) -> None:
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_longer_than(prenoms=prenoms)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
