import os


class Paths:
    program = os.path.dirname(os.path.abspath(__file__))
    resources = os.path.join(program, "Resources")
    icons = os.path.join(resources, "Icons")
    algorithms = os.path.join(program, "Algorithms")

    @staticmethod
    def icon(icon_file: str):
        return os.path.join(Paths.icons, icon_file)

    @staticmethod
    def algorithm(algorithm_name: str):
        return os.path.join(Paths.algorithms, algorithm_name)

    @staticmethod
    def codes(algorithm_name: str):
        algorithm_path = Paths.algorithm(algorithm_name)
        return os.path.join(algorithm_path, "codes")

    @staticmethod
    def test(algorithm_name: str):
        algorithm_path = Paths.algorithm(algorithm_name)
        return os.path.join(algorithm_path, "test.json")