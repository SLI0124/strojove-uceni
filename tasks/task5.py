import csv
import random


def load_data(filename, delimiter=';'):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=delimiter)
        _ = next(csv_reader) if 'titanic_preprocessed.csv' in filename else None  # Skip the header for Titanic dataset
        for row in csv_reader:
            dataset.append([float(value) for value in row[:-1]] + [int(row[-1])])

    return dataset


def split_train_test_data(dataset, train_ratio=0.8):
    train_size = int(len(dataset) * train_ratio)
    train_set = []
    test_set = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(test_set))
        train_set.append(test_set.pop(index))

    return train_set, test_set


def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            proportion = [row[-1] for row in group].count(class_val) / size
            score += proportion * proportion
        gini += (1.0 - score) * (size / n_instances)
    return gini


def test_split(index, value, dataset):
    left, right = [], []
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    best_index, best_value, best_score, best_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < best_score:
                best_index, best_value, best_score, best_groups = index, row[index], gini, groups
    return {'index': best_index, 'value': best_value, 'groups': best_groups}


def node_to_leaf(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)


def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del (node['groups'])

    # Print detailed information about the current split
    print("\t" * depth + f"Depth {depth}: Splitting on attribute index {node['index']} with value {node['value']}")

    # Check if either child is empty, if so create a leaf node
    if not left or not right:
        node['left'] = node['right'] = node_to_leaf(left + right)
        print("\t" * depth + f"Leaf created at depth {depth} with class {node['left']}")
        return

    # Check if max depth is reached
    if depth >= max_depth:
        node['left'], node['right'] = node_to_leaf(left), node_to_leaf(right)
        print("\t" * depth + "Max depth reached, creating leaf nodes.")
        return

    # Process left child
    if len(left) <= min_size:
        node['left'] = node_to_leaf(left)
        print("\t" * (depth + 1) + f"Left leaf node at depth {depth + 1} with class {node['left']}")
    else:
        node['left'] = get_split(left)
        print("\t" * (depth + 1) + f"Left child split at depth {depth + 1} on attribute index {node['left']['index']} "
                                   f"with value {node['left']['value']}")
        split(node['left'], max_depth, min_size, depth + 1)

    # Process right child
    if len(right) <= min_size:  # Check if right child is empty
        node['right'] = node_to_leaf(right)  # Create a leaf node if empty
        print("\t" * (depth + 1) + f"Right leaf node at depth {depth + 1} with class {node['right']}")
    else:
        node['right'] = get_split(right)
        print("\t" * (depth + 1) + f"Right child split at depth {depth + 1} on attribute index"
                                   f" {node['right']['index']} with value {node['right']['value']}")
        split(node['right'], max_depth, min_size, depth + 1)


def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root


def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


def decision_tree(train: list, test: list, max_depth: int, min_size: int):
    tree = build_tree(train, max_depth, min_size)
    predictions = []
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return predictions


def accuracy_metric(actual, predicted):
    correct = sum(1 for i in range(len(actual)) if actual[i] == predicted[i])
    return correct / float(len(actual)) * 100.0


def task_one():
    file_path = "../datasets/data_classification/iris.csv"
    dataset = load_data(file_path)
    train_set, test_set = split_train_test_data(dataset)

    max_depth = 5
    min_size = 10

    train_predictions = decision_tree(train_set, train_set, max_depth, min_size)
    test_predictions = decision_tree(train_set, test_set, max_depth, min_size)

    train_actual = [row[-1] for row in train_set]
    test_actual = [row[-1] for row in test_set]

    train_accuracy = accuracy_metric(train_actual, train_predictions)
    test_accuracy = accuracy_metric(test_actual, test_predictions)

    print(f"Training Accuracy: {train_accuracy:.2f}")
    print(f"Testing Accuracy: {test_accuracy:.2f}\n\n")


def task_two():
    file_path = "../datasets/data_classification/titanic_preprocessed.csv"
    dataset = load_data(file_path, delimiter=',')
    train_set, test_set = split_train_test_data(dataset)

    max_depth = range(1, 15)
    min_size = 10
    train_accuracy = []
    test_accuracy = []
    for i, depth in enumerate(max_depth):
        train_predictions = decision_tree(train_set, train_set, depth, min_size)
        test_predictions = decision_tree(train_set, test_set, depth, min_size)

        train_actual = [row[-1] for row in train_set]
        test_actual = [row[-1] for row in test_set]

        train_accuracy.append(accuracy_metric(train_actual, train_predictions))
        test_accuracy.append(accuracy_metric(test_actual, test_predictions))

        # print progress
        print(f"Total Progress: {(i + 1)}" + "/" + str(len(max_depth)) + " completed\n")

    for i in range(len(max_depth)):
        print(f"Max Depth: {max_depth[i]}, Training Accuracy: {train_accuracy[i]:.2f}, "
              f"Testing Accuracy: {test_accuracy[i]:.2f}")


def main():
    task_one()
    print("\n" * 10)
    task_two()


if __name__ == "__main__":
    main()
