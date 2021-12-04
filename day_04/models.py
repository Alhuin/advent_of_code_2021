from dataclasses import dataclass


@dataclass
class GridPoint:
    value: int
    checked: bool = False

    def __repr__(self) -> str:
        return f"\033[92m{self.value:>2}\033[00m" if self.checked else f"{self.value:>2}"


class Grid:
    def __init__(self, data: list[list[GridPoint]]):
        self.data = data
        self.won = False

    def mark(self, drawn: int) -> None:
        for line in self.data:
            for point in line:
                if drawn == point.value:
                    point.checked = True
                    return

    @staticmethod
    def check_grid(grid: list[list[GridPoint] | tuple[GridPoint]]) -> bool:
        for line in grid:
            if not all(point.checked for point in line):
                continue
            return True
        return False

    def self_check(self) -> bool:
        if self.check_grid(self.data) or self.check_grid(list(zip(*self.data))):
            self.won = True
            return True
        return False

    def compute_score(self, last_called: int) -> int:
        return sum(sum(point.value for point in line if not point.checked) for line in self.data) * last_called

    def __repr__(self) -> str:
        return '\n'.join([f"[{', '.join([str(point) for point in line])}]" for line in self.data])
