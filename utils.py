def read_input_as_int(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: int(x.strip()), f.readlines()))

