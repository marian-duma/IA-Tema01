import csv

def read_data(path : str) -> tuple[list[float], list[float]]:
    """Read two lists from a .csv file

    Args:
        path (str): the path of the .csv file

    Returns:
        tuple[list[float], list[float]]:
            the lists that will store in memory the values read from the file.
    """
    v1 : list[float] = []
    v2 : list[float] = []
    
    with open(path, mode='rt', newline='') as f:
        line = ""
        reader = csv.reader(f)
        # If one float conversion fails, then the value is alphanumeric
        # thus it can be considered a header row.
        # If neither conversion fails, then the value is a number
        # that will be added to the list.
        try:
            line = next(reader)
            value1 = float(line[0])
            value2 = float(line[1])
            v1.append(value1)
            v2.append(value2)
        except ValueError:
            pass # Ignore the first row.
        except StopIteration:
            return [],[] # On empty file.
        # Continue from the second row.
        for row in reader:
            if not row:
                continue
            v1.append(float(row[0]))
            v2.append(float(row[1]))

    return (v1, v2)

def write_data(path : str, v1 : list[float], v2 : list[float]) -> None:
    """Write two lists in a .csv file."""
    with open(path, mode='wt', newline='') as f:
        writer = csv.writer(f)
        for i, j in zip(v1, v2, strict=True):
            writer.writerow([i, j])

def write_result(path : str, result : float, message : str = ""):
    """Write the result of the Manhattan distance.

    Args:
        message (str, optional): Custom message for each write. Defaults to "".
    """
    with open(path, "at") as f:
        f.write(f"Manhattan distance is: {result}. {message}\n")
        