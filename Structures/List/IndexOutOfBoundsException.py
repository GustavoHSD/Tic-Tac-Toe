class IndexOutOfBoundsException(Exception):
    def __init__(self, index):
        raise Exception('Index ', index, ' out of bounds')
