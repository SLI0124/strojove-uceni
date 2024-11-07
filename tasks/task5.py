import pandas as pd
import sklearn.metrics


class DecisionTree:
    def __init__(self, root_rule):
        self.root_rule = root_rule
        self.left_branch = None
        self.right_branch = None


class Branch:
    def __init__(self, rule):
        self.rule = rule
        self.left_branch = None
        self.right_branch = None


def evaluate_feature(df, label, feature):
    focus_df = df.loc[:, [feature, label]]  # Focus on feature and label columns
    min_val = focus_df[feature].min()
    max_val = focus_df[feature].max()
    best_gini = 1
    best_split_val = 0
    step = (max_val - min_val) / 15  # Evaluate 15 different split values

    for i in range(1, 15):  # Skip min and max split values
        current_split = min_val + step * i
        left_split = focus_df.loc[focus_df[feature] <= current_split]
        right_split = focus_df.loc[focus_df[feature] > current_split]

        gini_index_left = 1
        gini_index_right = 1

        # Gini index calculation for left split
        for value in left_split[label].unique():
            class_count = left_split.loc[left_split[label] == value][label].count()
            total_count = len(left_split)
            gini_index_left -= pow(class_count / total_count, 2)

        # Gini index calculation for right split
        for value in right_split[label].unique():
            class_count = right_split.loc[right_split[label] == value][label].count()
            total_count = len(right_split)
            gini_index_right -= pow(class_count / total_count, 2)

        gini_index = (gini_index_left + gini_index_right) / 2  # Average Gini index

        if gini_index < best_gini:
            best_split_val = current_split
            best_gini = gini_index

    return feature, best_split_val, best_gini


def branch(df, YLabel, k, n):
    if k == n:
        # Reached bottom level, no further branching
        label = df[YLabel].value_counts().index[0]  # Most common label in the split
        this_branch = Branch((k, ('END', label)))
        return this_branch

    gini_index_main = 1
    for value in df[YLabel].unique():
        class_count = df.loc[df[YLabel] == value][YLabel].count()
        total_count = len(df)
        gini_index_main -= pow(class_count / total_count, 2)

    if gini_index_main == 0:
        # Branch is pure, no further branching
        label = df[YLabel].value_counts().index[0]  # Most common label in the split
        this_branch = Branch((k, ('END', label)))
        return this_branch

    best_feature = evaluate_feature(df, YLabel, df.columns[0])
    for col in df.columns[1:-1]:  # Exclude first feature and last label column
        result = evaluate_feature(df, YLabel, col)
        if result[2] < best_feature[2]:
            best_feature = result

    new_df1 = df.loc[df[best_feature[0]] <= best_feature[1]]
    new_df2 = df.loc[df[best_feature[0]] > best_feature[1]]

    this_branch = Branch((k, best_feature))

    if len(new_df1) == 0 or len(new_df2) == 0:
        # If any branch is empty, stop branching
        label = df[YLabel].value_counts().index[0]
        this_branch = Branch((k, ('END', label)))
        return this_branch

    this_branch.left_branch = branch(new_df1, YLabel, k + 1, n)
    this_branch.right_branch = branch(new_df2, YLabel, k + 1, n)
    return this_branch


def decision_tree_train(df, y_label, n_levels=3, verbose=True):
    k = 0
    best_feature = evaluate_feature(df, y_label, df.columns[0])
    for col in df.columns[1:-1]:  # Exclude first feature and last label column
        result = evaluate_feature(df, y_label, col)
        if result[2] < best_feature[2]:
            best_feature = result

    new_df1 = df.loc[df[best_feature[0]] <= best_feature[1]]
    new_df2 = df.loc[df[best_feature[0]] > best_feature[1]]

    tree = DecisionTree((k, best_feature))
    tree.left_branch = branch(new_df1, y_label, k + 1, n_levels)
    tree.right_branch = branch(new_df2, y_label, k + 1, n_levels)
    return tree


def decision_tree_predict(df, model: DecisionTree):
    first_rule = model.root_rule[1]
    predictions = []

    for row in df.iterrows():  # Iterate over rows
        prediction = -1
        if row[1][first_rule[0]] <= first_rule[1]:
            prediction = branch_predict(row, model.left_branch)
        else:
            prediction = branch_predict(row, model.right_branch)
        predictions.append(prediction)

    return predictions


def branch_predict(row, model: Branch):
    rule = model.rule[1]
    if rule[0] == 'END':
        return rule[1]

    if row[1][rule[0]] <= rule[1]:
        prediction = branch_predict(row, model.left_branch)
    else:
        prediction = branch_predict(row, model.right_branch)

    return prediction


def main():
    df = pd.read_csv('../datasets/data_classification/iris.csv', header=None, delimiter=';',
                     names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

    # Split data into train and test sets
    train_X = df.sample(frac=0.8)
    test_X = df.drop(train_X.index)
    print(f"Train: {train_X.shape}, Test: {test_X.shape}")

    # Train model on training data
    model = decision_tree_train(train_X, "species")

    # Predict on train set
    train_predictions = decision_tree_predict(train_X, model)
    train_accuracy = sklearn.metrics.accuracy_score(train_X.species, train_predictions)
    print(f"Train Accuracy: {train_accuracy}")

    # Predict on test set
    test_predictions = decision_tree_predict(test_X, model)
    test_accuracy = sklearn.metrics.accuracy_score(test_X.species, test_predictions)
    print(f"Test Accuracy: {test_accuracy}\n")

    # Repeat for Titanic dataset
    df_titanic = pd.read_csv("../datasets/data_classification/titanic_preprocessed.csv", sep=",",
                             index_col='PassengerId')
    df_titanic = df_titanic[[c for c in df_titanic if c not in ['Survived']] + ['Survived']]

    train_X = df_titanic.sample(frac=0.8)
    test_X = df_titanic.drop(train_X.index)

    model = decision_tree_train(train_X, "Survived")

    # Predict on train set
    train_predictions = decision_tree_predict(train_X, model)
    train_accuracy = sklearn.metrics.accuracy_score(train_X["Survived"], train_predictions)
    print(f"Train Accuracy (Titanic): {train_accuracy}")

    # Predict on test set
    test_predictions = decision_tree_predict(test_X, model)
    test_accuracy = sklearn.metrics.accuracy_score(test_X["Survived"], test_predictions)
    print(f"Test Accuracy (Titanic): {test_accuracy}\n")

    for i in range(1, 16):
        train_X = df_titanic.sample(frac=0.8)
        test_X = df_titanic.drop(train_X.index)

        model = decision_tree_train(train_X, "Survived", n_levels=i)

        # Predict on train set
        train_predictions = decision_tree_predict(train_X, model)
        train_accuracy = sklearn.metrics.accuracy_score(train_X["Survived"], train_predictions)
        print(f"Train Accuracy (Titanic) with depth {i}: {train_accuracy}")

        # Predict on test set
        test_predictions = decision_tree_predict(test_X, model)
        test_accuracy = sklearn.metrics.accuracy_score(test_X["Survived"], test_predictions)
        print(f"Test Accuracy (Titanic) with depth {i}: {test_accuracy}\n")

    # do the same for depth 30 and 50
    for i in [30, 50]:
        train_X = df_titanic.sample(frac=0.8)
        test_X = df_titanic.drop(train_X.index)

        model = decision_tree_train(train_X, "Survived", n_levels=i)

        # Predict on train set
        train_predictions = decision_tree_predict(train_X, model)
        train_accuracy = sklearn.metrics.accuracy_score(train_X["Survived"], train_predictions)
        print(f"Train Accuracy (Titanic) with depth {i}: {train_accuracy}")

        # Predict on test set
        test_predictions = decision_tree_predict(test_X, model)
        test_accuracy = sklearn.metrics.accuracy_score(test_X["Survived"], test_predictions)
        print(f"Test Accuracy (Titanic) with depth {i}: {test_accuracy}\n")


if __name__ == "__main__":
    main()
