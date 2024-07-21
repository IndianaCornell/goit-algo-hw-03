import os
import random
import string

def generate_random_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_files(directory, num_files):
    extensions = ['txt', 'csv', 'log', 'json', 'xml', 'html', 'md', 'py', 'jpg', 'png']
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for _ in range(num_files):
        file_name = generate_random_name()
        extension = random.choice(extensions)
        full_file_name = os.path.join(directory, f"{file_name}.{extension}")
       
        with open(full_file_name, 'w') as file:
            file.write("")  

directory = 'files'
num_files = 10

create_files(directory, num_files)
