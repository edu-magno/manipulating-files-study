def post_transaction(filename, title, transaction_type, value):
    with open(filename, 'a') as file:
        file.writelines(
            ['title: {}\n'.format(title),
             'transaction_type: {}\n'.format(transaction_type),
             'value: {}\n'.format(value)
             ])


def all_transactions(filename):
    line_items = []
    list_of_lines = []
    dict_line = {}
    with open(filename, 'r') as file:
        for line in file:
            splited_line = line.split()
            line_items.append(tuple(splited_line))

    for index in range(int(len(line_items) / 3)):
        list_of_line = line_items[index * 3:3 * (index + 1)]
        list_of_lines.append(list_of_line)

    for items, index in zip(list_of_lines[0], range(len(list_of_lines[0]))):
        key_len = len(list_of_lines[0][index][0]) - 1
        key = items[0][:key_len]
        value = items[1]
        dict_line.update({key: value})

    return [dict_line]


def make_appointment(filename, name, hour, description):
    id_pacient = 1
    with open(filename, 'r') as file:
        id_pacient = int(len(file.readlines()) / 4 + 1)

    with open(filename, 'a+') as file:

        file.writelines(
            ['id: {}\n'.format(id_pacient),
             'name: {}\n'.format(name),
             'hour: {}\n'.format(hour),
             'description: {}\n'.format(description)
             ]
        )



def time_is_free(filename, hour):
    free_time = True
    with open(filename, 'r') as file:
        file_lines = file.readlines()

        for line in file_lines:
            has_time = line.find(hour)

            if has_time > 0:
                free_time = False
                break
            if has_time == -1:
                free_time = True

    return free_time
