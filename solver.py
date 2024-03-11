"""Solver for impossible game."""

from board import GameBoard
from block import Block, Height, create_block_list


def solve(board: GameBoard, avail_blocks: list[Block]):
    if board.solved:
        print("finished board:")
        board.print_board()
        quit()

    for row in range(board.size):
        for col in range(board.size):
            if board.no_block(row, col):
                needed_block_height = board.block_height(row, col)
                possible_blocks = filter_height(avail_blocks, needed_block_height)

                for block in possible_blocks[::-1]:
                    if board.possible_place(block, row=row, col=col):
                        board.set_block(block, row=row, col=col)
                        board.plot_board()
                        avail_blocks.remove(block)
                        solve(board=board, avail_blocks=avail_blocks)
                        board.unset_block(block, row=row, col=col)
                        avail_blocks.append(block)

                return


def filter_height(block_list: list[Block], height: Height):
    return [block for block in block_list if block.height == height]


if __name__ == "__main__":
    blocks = create_block_list()
    board = GameBoard()
    solve(board=board, avail_blocks=blocks)
    board.print_board()
