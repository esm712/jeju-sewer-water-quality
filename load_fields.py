def load_fields_from_txt(file_path):
    with open(file_path, 'r') as file:
        fields = [line.strip() for line in file.readlines()]
    return fields