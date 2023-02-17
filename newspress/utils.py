''' Utils '''
def convert_to_binary_data(file_name):
    ''' Convert the image to binary '''
    with open(file_name, 'rb') as file:
        return file.read()
