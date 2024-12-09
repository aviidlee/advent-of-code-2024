from abc import ABC, abstractmethod
from typing import Type

"""

"""


class Searcher(ABC):
    """
    matrix with standard indexation, that is, an n x m matrix otf:
    pos[0][0] pos[0][1] ... pos[0][m-1]
    .                           .
    .                           .
    .                           .
    pos[n-1][0]       ...   pos[n-1][m-1]

    """

    def __init__(self, matrix: list[list[str]], pos: tuple[int, int]):
        self.matrix = matrix
        self.pos = pos

    @abstractmethod
    def get_next_pos(self):
        pass

    def get_next_char(self):
        next_pos = self.get_next_pos()
        if (
            next_pos[0] >= 0
            and next_pos[0] < len(self.matrix)
            and next_pos[1] >= 0
            and next_pos[1] < len(self.matrix[0])
        ):
            return self.matrix[next_pos[0]][next_pos[1]]
        else:
            return ""


class NorthSearcher(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0] - 1, self.pos[1])
        return self.pos


class EastSearcher(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0], self.pos[1] + 1)
        return self.pos


class WestSearcher(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0], self.pos[1] - 1)
        return self.pos


class SouthSearcher(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0] + 1, self.pos[1])
        return self.pos


class NorthEast(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0] - 1, self.pos[1] + 1)
        return self.pos


class SouthEast(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0] + 1, self.pos[1] + 1)
        return self.pos


class NorthWest(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0] - 1, self.pos[1] - 1)
        return self.pos


class SouthWest(Searcher):
    def get_next_pos(self):
        self.pos = (self.pos[0] + 1, self.pos[1] - 1)
        return self.pos


class PatternFinder:
    def __init__(self, pattern: str, searchers: list[Type[Searcher]]):
        self.pattern = pattern
        self.searchers = searchers

    def search(self, matrix: list[list[str]]) -> int:
        total_found = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                total_found = total_found + self.search_from((row, col), matrix)

        return total_found

    """
  Search given that starting_pos has 'X'
  """

    def search_from(
        self, starting_pos: tuple[int, int], matrix: list[list[str]]
    ) -> int:
        total_found = 0

        if matrix[starting_pos[0]][starting_pos[1]] != self.pattern[0]:
            return 0

        for searcher_type in self.searchers:
            searcher = searcher_type(matrix, starting_pos)
            pattern_ind = 0

            while pattern_ind < len(self.pattern) - 1:
                next_char = searcher.get_next_char()
                if next_char == self.pattern[pattern_ind + 1]:
                    pattern_ind = pattern_ind + 1
                # Run off the edge of the matrix    
                elif next_char == "":
                    break
                # No match 
                else:
                    break 

            if pattern_ind == len(self.pattern) - 1:
                print(
                    f"Searcher {searcher.__class__} found match starting from {starting_pos}"
                )
                total_found = total_found + 1

        return total_found


def read_input(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        lines = f.readlines()
        cleaned_lines = []
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line != '':
                cleaned_lines.append(cleaned_line)

        return cleaned_lines


if __name__ == "__main__":
    mat = read_input("input.txt")
    print(f"matrix dimensions: {len(mat)} by {len(mat[0])}")
    print(mat[-1][:])
    finder = PatternFinder(
        "XMAS",
        [
            NorthSearcher,
            EastSearcher,
            WestSearcher,
            SouthSearcher,
            NorthEast,
            NorthWest,
            SouthEast,
            SouthWest,
        ],
    )
    print(f"Found {finder.search(mat)} occurrences")
