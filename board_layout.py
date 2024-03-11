"""Board layout of the physical 6x6 game."""

import numpy as np

BOARD_LAYOUT = np.array(
    [
        [6, 3, 2, 4, 5, 1],
        [4, 5, 1, 6, 3, 2],
        [1, 2, 4, 3, 6, 5],
        [2, 5, 3, 6, 1, 4],  # [2, 6, 3, 5, 1, 4],
        [3, 1, 5, 2, 4, 6],
        [5, 4, 6, 1, 2, 3],
    ]
)
