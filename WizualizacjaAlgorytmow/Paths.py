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
    def algorithm(algorythm_name: str):
        return os.path.join(Paths.algorithms, algorythm_name)

    @staticmethod
    def codes(algorythm_name: str):
        algorythm_path = Paths.algorithm(algorythm_name)
        return os.path.join(algorythm_path, "codes")

    @staticmethod
    def test(algorythm_name: str):
        algorythm_path = Paths.algorithm(algorythm_name)
        return os.path.join(algorythm_path, "test.json")