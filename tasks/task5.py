import csv


def load_csv(file_path, delimiter=";"):
    with open(file_path, "r") as file:
        reader = csv.reader(file, delimiter=delimiter)
        data = list(reader)
    return data


def main():
    file_path = "../datasets/data_classification/iris.csv"
    data = load_csv(file_path)
    print('\n'.join([str(row) for row in data]))


if __name__ == "__main__":
    main()
