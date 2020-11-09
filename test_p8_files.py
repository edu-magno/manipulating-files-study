from processors.p8_file_functions import *


def test_post_transaction():
    post_transaction('test_transactions.txt', 'mercado', 'outcome', 500)
    result = 0
    with open('test_transactions.txt', 'r') as file:
        result = len(file.readlines())

    assert result > 0


def test_all_transactions():
    result = all_transactions('test_all_transactions.txt')
    expected = [{'title': 'mercado',
                 'transaction_type': 'outcome', 'value': '500'}]

    assert expected == result


def test_make_appointment():
    make_appointment('test_psychologist_appointments.txt', 'Roberto',
                     '2020-09-10 10:00:00', 'estou estressado com o trabalho')
    result = 0
    with open('test_psychologist_appointments.txt', 'r') as file:
        result = len(file.readlines())

    assert result > 0


def test_time_is_free():
    result1 = time_is_free(
        'test_psychologist_appointments.txt', '2020-09-10 10:00:00')
    expected1 = False

    assert result1 == expected1

    result2 = time_is_free(
        'test_psychologist_appointments.txt', '2020-09-10 14:00:00')
    expected2 = True

    assert result2 == expected2
