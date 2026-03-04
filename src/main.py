from scipy.spatial.distance import cityblock
from pathlib import Path
import utils.manhattan as manhattan
import data_io.file_handler as file_handler
import utils.data_generator as data_generator


def main() -> None:
    """ 
    Calculate Manhattan distance using a handwritten function and
    the cityblock function imported from scipy.
    Workflow:
    1. Create the data directory if it doesn't exist.
    2. Generate 2 random lists if an input file does not exist,
       and create that file.
    3. Read the data from the input file.
    4. Calculate the Manhattan distance using the two functions.
    5. Write the two results to a file.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)

    input_file_path = str(DATA_DIR / "input.csv")
    output_file_path = str(DATA_DIR / "output.csv")

    if not Path(input_file_path).exists():
        try:
            file_handler.write_data(
                input_file_path,
                data_generator.generate_data(seed=86, size=10**5, scale=1000),
                data_generator.generate_data(seed=41, size=10**5, scale=1000),
                )
        except ValueError as e:
            print(e)
            exit()

    # Read the data and calculate
    v1, v2 = file_handler.read_data(input_file_path)

    result_manhattan = manhattan.distance(v1, v2)
    result_cityblock = cityblock(v1, v2)

    try:
        file_handler.write_result(
            output_file_path,
            result_manhattan,
            f"(Handwritten function)"
            )
        file_handler.write_result(
            output_file_path,
            result_cityblock,
            f"(Cityblock function)"
            )
    except ValueError as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()