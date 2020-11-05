def post_transaction(filename, title, transaction_type, value):
    with open(filename, 'a') as file:
        file.writelines(
            ['title: {}\n'.format(title), 
            'transaction_type: {}\n'.format(transaction_type),
            'value: {}\n'.format(value)
            ])
        

def all_transaction(filename):
    list_of_lines = []
    
    with open(filename, 'r') as file:
        for line in file:
            splited_line = line.split()
            list_of_lines.append(tuple(splited_line))
            
    
