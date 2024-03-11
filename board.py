"""Board of the game."""
import os
from pathlib import Path

import numpy as np
import typhon as ty
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from block import Block, Height, Color
from board_layout import BOARD_LAYOUT

SIZE = 6
FIGURE_PADDING = 0.2
RECTANGE_PADDING = 0.05
RECTANGE_WIDTH = 0.9
SAVE_PATH = Path("plots")


class GameBoard:
    def __init__(self, size: int = SIZE):
        if size != SIZE:
            raise NotImplementedError(f"This is only implimented for a siye of {SIZE}.")
        self.size = size
        self.board_height = np.empty((size, size))
        self.board = np.empty((size, size))
        self.block_layout = {color: np.zeros((size, size)) for color in Color.members}
        self.iterations = 0

        self._init_board()

    def _init_board(self):
        self.board_height = BOARD_LAYOUT

    def possible_place(self, block: Block, row, col):
        color_board = self.block_layout[block.color]

        if self.board_height[row, col] != block.height.numerical:
            return False
        if color_board[row, :].sum() > 0:
            return False
        if color_board[:, col].sum() > 0:
            return False
        return True

    def set_block(self, block: Block, row: int, col: int):
        self.iterations += 1
        self.block_layout[block.color][row, col] = 1

    def unset_block(self, block: Block, row: int, col: int):
        self.block_layout[block.color][row, col] = 0

    def no_block(self, row, col):
        return all(self.block_layout[color][row, col] == 0 for color in Color.members)

    def block_height(self, row, col) -> Height:
        height = self.board_height[row, col]
        return Height.from_numerical(self.board_height[row, col])

    @property
    def board_state(self):
        board_state = np.zeros(self.board.shape)
        board_state = board_state.fill(np.nan)
        for color in Color.members:
            board_state = np.where(
                self.block_layout[color] != 1,
                board_state,
                color,
            )
        return board_state

    def print_board(self):
        board_state = np.zeros(self.board.shape)
        board_state = board_state.fill(np.nan)
        for color in Color.members:
            board_state = np.where(
                self.block_layout[color] != 1,
                board_state,
                color.name.lower(),
            )
        for row in range(self.size):
            print(board_state[row, :])

    def plot_board(self):
        ty.plots.styles.use(["typhon", "typhon-dark"])
        step = 1
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim([-FIGURE_PADDING, self.size + FIGURE_PADDING])
        ax.set_ylim([-FIGURE_PADDING, self.size + FIGURE_PADDING])

        for i in range(self.size + 1):
            ax.plot([0, self.size], [i, i], color="ty:chalmers-blue", linewidth=3)
            ax.plot([i, i], [0, self.size], color="ty:chalmers-blue", linewidth=3)

        ax.axis("image")
        ax.axis("off")

        board_state = self.board_state
        for row in range(self.size):
            for col in range(self.size):
                height_text = str(self.board_height[row, col])
                ax.text(
                    col + 0.35,
                    (self.size - row - 1) + 0.3,
                    height_text,
                    fontsize=32,
                    color="ty:darkgrey",
                )
                if board_state[row, col]:
                    ax.add_patch(
                        Rectangle(
                            xy=(
                                col + RECTANGE_PADDING,
                                (self.size - row - 1) + RECTANGE_PADDING,
                            ),
                            width=RECTANGE_WIDTH,
                            height=RECTANGE_WIDTH,
                            color=board_state[row, col].plot_color,
                        )
                    )
        if not SAVE_PATH.is_dir():
            os.mkdir(SAVE_PATH)
        fig.savefig(SAVE_PATH / f"impossible_game_{str(self.iterations).zfill(5)}.png")
        plt.close()

    @property
    def solved(self):
        return all(self.block_layout[color].sum() == 6 for color in Color.members)
