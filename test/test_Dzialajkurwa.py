import unittest
from Raport import Problemy, Raport, Temperatura

from main import generate_raport


class EmptyTest(unittest.TestCase):
    def test_empty_file(self):
        file_path = "test/inputs/empty_file.txt"
        expected_output = Raport()

        raport = generate_raport(file_path)
        self.assertEqual(str(raport), str(expected_output))

    def test_from_spec_first_Example(self):
        file_path = "test/inputs/test_first_from_spec.txt"
        expected_output = Raport(
            czas_trwania_raportu=70,
            temperatura=Temperatura(max=100.0, min=90.0, srednia=95.0))

        result = generate_raport(file_path)
        self.assertEqual(str(result), str(expected_output))

    def test_from_spec_second_Example(self):
        file_path = "test/inputs/test_second_from_spec.txt"
        expected_output = Raport(
            wadliwe_logi=["2023-x1-01 23:5x 10xC", "2023-01-02 00:10"],
            procent_wadliwych_logow=40.0,
            czas_trwania_raportu=70,
            temperatura=Temperatura(max=100.0, min=90.0, srednia=95.0),
            problemy=Problemy(wysoki_poziom_zaklocen_EM=True))

        result = generate_raport(file_path)
        self.assertEqual(str(result), str(expected_output))


if __name__ == '__main__':
    unittest.main()
