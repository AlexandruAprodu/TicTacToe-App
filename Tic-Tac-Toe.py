valori_grila = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

def update_grid():
    print(' _______________')
    print(' | ' + valori_grila[0] + ' | ', valori_grila[1] + ' | ', valori_grila[2] + ' | ')
    print(' _______________')
    print(' | ' + valori_grila[3] + ' | ', valori_grila[4] + ' | ', valori_grila[5] + ' | ')
    print(' _______________')
    print(' | ' + valori_grila[6] + ' | ', valori_grila[7] + ' | ', valori_grila[8] + ' | ')
    print(' _______________')

def tie():
    if get_winner():
        return False

    if valori_grila[0] != '-' and \
     valori_grila[1] != '-' and \
     valori_grila[2] != '-' and \
     valori_grila[3] != '-' and \
     valori_grila[4] != '-' and \
     valori_grila[5] != '-' and \
     valori_grila[6] != '-' and \
     valori_grila[7] != '-' and \
     valori_grila[8] != '-':
        return True


def check_winner_on_rows(ics_sau_zero):
    if valori_grila[0] == valori_grila[1] == valori_grila[2] == ics_sau_zero:
        return True
    if valori_grila[3] == valori_grila[4] == valori_grila[5] == ics_sau_zero:
        return True
    if valori_grila[6] == valori_grila[7] == valori_grila[8] == ics_sau_zero:
        return True


def check_winner_on_columns(ics_sau_zero):
    if valori_grila[0] == valori_grila[3] == valori_grila[6] == ics_sau_zero:
        return True
    if valori_grila[1] == valori_grila[4] == valori_grila[7] == ics_sau_zero:
        return True
    if valori_grila[2] == valori_grila[5] == valori_grila[8] == ics_sau_zero:
        return True


def check_winner_on_diagonal(ics_sau_zero):
    if valori_grila[0] == valori_grila[4] == valori_grila[8] == ics_sau_zero:
        return True

    if valori_grila[2] == valori_grila[4] == valori_grila[6] == ics_sau_zero:
        return True


def assign_value_to_grid(position, value):
    list_index = position - 1
    valori_grila[list_index] = value


def ask_player_for_position(ics_sau_zero):
    return int(input(f'{ics_sau_zero}, alege o pozitie libera de la 1 la 9: '))


def get_winner():
    winner_name = None
    if check_winner_on_diagonal('X'):
        winner_name = 'X'

    if check_winner_on_diagonal('0'):
        winner_name = '0'

    if check_winner_on_columns('X'):
        winner_name = 'X'

    if check_winner_on_columns('0'):
        winner_name = '0'

    if check_winner_on_rows('X'):
        winner_name = 'X'

    if check_winner_on_rows('0'):
        winner_name = '0'

    return winner_name


def main():
    nume_jucatorX = input('Nume jucator X: ')
    nume_jucator0 = input('Nume jucator 0: ')

    current_player = 'X'

    update_grid()

    while True:
        current_player_position = ask_player_for_position(current_player)
        value_to_write = current_player

        assign_value_to_grid(current_player_position, value_to_write)
        update_grid()

        if current_player == 'X':
            current_player = '0'
        else:
            current_player = 'X'

        winner_name = get_winner()

        if winner_name:
            break
        if tie():
            break

    if tie():
        print('Egalitate!')

    if winner_name == 'X':
        print(f'Castigatorul este {nume_jucatorX}!')

    if winner_name == '0':
        print(f'Castigatorul este {nume_jucator0}!')

    key = input('Apasa "5" pentru joc nou: ')
    if key == '5':
        global valori_grila
        valori_grila = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        main()

main()
