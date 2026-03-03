from scipy.spatial.distance import cityblock
from pathlib import Path

import utils.manhattan as manhattan
import data_io.file_handler as file_handler
import utils.data_generator as data_generator


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

input_file_path = str(DATA_DIR / "input.csv")
output_file_path = str(DATA_DIR / "output.csv")


def main() -> None:
    # Generate random data
    print(input_file_path)
    data_generator.generate_input_file(input_file_path)

    # Read the data and work
    v1, v2 = file_handler.read_data(input_file_path)
    try:
        file_handler.write_result(
            output_file_path,
            manhattan.distance(v1, v2),
            "(Handwritten function)"
            )
        file_handler.write_result(
            output_file_path,
            cityblock(v1, v2),
            "(Cityblock function)"
            )
    except ValueError as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()