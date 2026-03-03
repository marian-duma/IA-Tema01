import random
import data_io.file_handler as file_handler

# TODO
# check parameters for proper values greater than 0
# check scale to be a multiple of 10
def generate_data(seed : int = 3333, size : int = 1000, scale : int = 1) -> list[float]:
    random.seed(seed)
    output : list[float] = []
    for i in range(size):
        output.append(random.random() * scale)
    return output

def generate_input_file(path : str):
    file_handler.write_data(path,
                            generate_data(seed=8),
                            generate_data(seed=30)
                            )