''' Utils '''
def convert_to_binary_data(file_name):
    ''' Convert the image to binary '''
    with open(file_name, 'rb') as file:
        return file.read()

tags = ['gratitude', ' mental health', ' meditation']
for tag in tags:
    print(tag)