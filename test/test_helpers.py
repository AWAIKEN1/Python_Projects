from src.helpers import draw_board, check_turn, check_for_win


def test_draw_board():
    spots = {1: 'X', 2: '2', 3: 'O', 4: '4',
             5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    draw_board(spots)


def test_check_turn_even_turn():
    assert check_turn(2) == 'O'


def test_check_turn_odd_turn():
    assert check_turn(3) == 'X'


def test_check_for_win_horizontal_win():
    spots = {1: 'X', 2: 'O', 3: 'X', 4: 'O',
             5: 'O', 6: 'O', 7: 'X', 8: 'X', 9: 'O'}
    assert check_for_win(spots) == True


def test_check_for_win_diagonal_win():
    spots = {1: 'X', 2: 'O', 3: 'O', 4: 'O',
             5: 'X', 6: 'X', 7: 'O', 8: 'X', 9: 'X'}
    assert check_for_win(spots) == True
