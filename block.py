"""Block class."""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Self


class BlockProperty(Enum):
    @classmethod
    @property
    def members(cls):
        return [mem for mem in cls.__members__.values()]


class Color(BlockProperty):
    """Color of the Blocks."""

    GREEN = auto()
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    PURPLE = auto()
    BLUE = auto()

    @property
    def plot_color(self) -> str:
        return COLOR2PLOTTING_COLOR[self]


class Height(BlockProperty):
    """Height of the Blocks."""

    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()

    @property
    def numerical(self) -> int:
        return HEIGHT2NUMERICAL[self]

    @classmethod
    def from_numerical(cls, height: int) -> Self:
        numerical2height = {v: k for k, v in HEIGHT2NUMERICAL.items()}
        return numerical2height[height]


@dataclass
class Block:
    def __init__(self, color: Color, height: Height):
        self.color = color
        self.height = height

    def __repr__(self):
        return f"{self.color} - {self.height}"

    def __eq__(self, other):
        if not isinstance(other, Block):
            return False
        return self.color == other.color and self.height == other.height


HEIGHT2NUMERICAL: dict[Height, int] = {
    Height.ONE: 1,
    Height.TWO: 2,
    Height.THREE: 3,
    Height.FOUR: 4,
    Height.FIVE: 5,
    Height.SIX: 6,
}

COLOR2PLOTTING_COLOR: dict[Color, str] = {
    Color.GREEN: "limegreen",
    Color.RED: "orangered",
    Color.ORANGE: "orange",
    Color.YELLOW: "gold",
    Color.PURPLE: "mediumslateblue",
    Color.BLUE: "lightskyblue",
}


def create_block_list() -> list[Block]:
    return [
        Block(color=color, height=height)
        for height in Height.members
        for color in Color.members
    ]


if __name__ == "__main__":
    blocks = create_block_list()
    pass
