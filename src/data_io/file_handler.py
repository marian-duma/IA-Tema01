import csv

def read_data(path : str) -> tuple[list[float], list[float]]:
    v1 : list[float] = []
    v2 : list[float] = []
    
    with open(path, mode='rt') as f:
        line = ""
        reader = csv.reader(f)
        #check if the csv contains a header row
        try:
            line = next(reader)
            float(line[0])
            v1.append(float(line[0]))
            v2.append(float(line[1]))
        except ValueError:
            pass
        except StopIteration:
            return [],[]
        for row in reader:
            if not row:
                continue
            v1.append(float(line[0]))
            v2.append(float(line[1]))

    return (v1, v2)

def write_data(path : str, v1 : list[float], v2 : list[float]) -> None:
    with open(path, mode='wt') as f:
        writer = csv.writer(f)
        for i, j in zip(v1, v2, strict=True):
            writer.writerow([i, j])

def write_result(path : str, result : float, message : str = ""):
    with open(path, "at") as f:
        f.write(f"Manhattan distance is: {result}. {message}\n")
        