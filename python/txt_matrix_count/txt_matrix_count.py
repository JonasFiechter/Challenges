with open('mock_matrix.txt', 'r') as file:
    text = file.read()

text_to_list = text.replace('\n', ';').split(';')

for key, value in {item: text_to_list.count(item) for item in text_to_list}.items():
    print(f'{key} => {value}')