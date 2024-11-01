import numpy as np
import math
import os
from matplotlib import pyplot as plt

# virdis color palette
cluster_colors = {
    0: "#440154",
    1: "#FDE725",
    2: "#21918C",
    3: "#FF5733",
    4: "#5EC962"
}


def get_all_csv_path():
    all_paths = []
    for root, dirs, files in os.walk("../datasets/data_clustering"):
        for file in files:
            if file.endswith(".csv"):
                all_paths.append(os.path.join(root, file))
    # windows fix  - replace backslashes with forward slashes
    all_paths = [path.replace("\\", "/") for path in all_paths]
    return all_paths


def read_csv(file_path, delimiter=';'):
    return np.loadtxt(file_path, delimiter=delimiter)


def euclidean_distance_matrix(data):
    return np.sqrt(((data[:, np.newaxis] - data) ** 2).sum(axis=2))


def manhattan_distance_matrix(data):
    return np.abs(data[:, np.newaxis] - data).sum(axis=2)


def cosine_distance_matrix(data):
    dot_product = np.dot(data, data.T)  # dot product of data with itself
    norm = np.linalg.norm(data, axis=1)  # norm of each row
    return 1 - (dot_product / np.outer(norm, norm))  # cosine distance matrix


def agglomerate_clustering(data, metric, linkage, n_clusters):
    if metric == "euclidean":
        distance_matrix = euclidean_distance_matrix(data)
    elif metric == "manhattan":
        distance_matrix = manhattan_distance_matrix(data)
    elif metric == "cosine":
        distance_matrix = cosine_distance_matrix(data)
    else:
        raise ValueError("Unknown metric")

    np.fill_diagonal(distance_matrix, np.inf)  # Set diagonal to infinity to avoid self-comparison
    clusters = [[i] for i in range(len(data))]  # Initialize clusters

    while len(clusters) > n_clusters:  # Merge clusters until the desired number of clusters is reached
        print(f"Clusters: {len(clusters)}/{n_clusters}")
        # Find the closest clusters by finding the minimum distance in the distance matrix
        closest_clusters = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)
        i, j = sorted(closest_clusters)

        clusters[i].extend(clusters[j])  # Merge the clusters
        clusters.pop(j)  # Remove the merged cluster since it is no longer needed

        if linkage == "single":  # Update the distance matrix based on the linkage
            new_distances = np.minimum(distance_matrix[i], distance_matrix[j])
        elif linkage == "complete":
            new_distances = np.maximum(distance_matrix[i], distance_matrix[j])
        else:
            raise ValueError("Unknown linkage")

        distance_matrix[i] = new_distances  # Update the distance matrix
        distance_matrix[:, i] = new_distances  # Update the distance matrix (symmetric)
        distance_matrix = np.delete(distance_matrix, j, axis=0)  # Remove the merged cluster from the distance matrix
        distance_matrix = np.delete(distance_matrix, j, axis=1)  # Remove the merged cluster from the distance matrix
        np.fill_diagonal(distance_matrix, np.inf)  # Set diagonal to infinity to avoid self-comparison

    return [[data[idx] for idx in cluster] for cluster in clusters]  # Return the clusters


def save_plot(data, clusters, title, save_path):
    for x in data:
        plt.scatter(float(x[0]), float(x[1]))  # Plot the data points

    for i, cluster in enumerate(clusters):
        for point in cluster:
            plt.scatter(point[0], point[1], color=cluster_colors[i])  # Plot the clusters with different colors

    plt.title(title)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    plt.savefig(f"{save_path}/{title}.png")
    plt.clf()  # Clear the figure to avoid overlaps


def normalize(data):
    min_values = []
    max_values = []

    for i in range(len(data[0])):  # Iterate through columns
        column = [row[i] for row in data]
        min_values.append(min(column))
        max_values.append(max(column))
    normalized_data = []  # List to hold normalized rows

    for row in data:
        normalized_row = []  # List to hold normalized values for the current row
        for i in range(len(row)):
            if max_values[i] - min_values[i] > 0:  # Avoid division by zero
                normalized_value = (row[i] - min_values[i]) / (max_values[i] - min_values[i])
            else:
                normalized_value = 0
            normalized_row.append(normalized_value)  # Add normalized value to the row
        normalized_data.append(normalized_row)  # Add the normalized row to the data
    return normalized_data


def standardize(data):
    means = []

    for i in range(len(data[0])):  # Iterate through columns
        column = [row[i] for row in data]
        mean_value = sum(column) / len(column)
        means.append(mean_value)

    std_devs = []  # List to hold standard deviations for each column

    for i in range(len(data[0])):
        sum_squared_diff = 0
        for row in data:
            sum_squared_diff += (row[i] - means[i]) ** 2
        std_dev_value = math.sqrt(sum_squared_diff / len(data))
        std_devs.append(std_dev_value)

    standardized_data = []  # List to hold standardized rows

    # Standardize each row
    for row in data:
        standardized_row = []  # List to hold standardized values for the current row
        for i in range(len(row)):
            if std_devs[i] > 0:  # Avoid division by zero
                standardized_value = (row[i] - means[i]) / std_devs[i]
            else:
                standardized_value = 0
            standardized_row.append(standardized_value)  # Add standardized value to the row
        standardized_data.append(standardized_row)  # Add the standardized row to the data
    return standardized_data


def task_one():
    all_csv = get_all_csv_path()
    metrics = ["euclidean", "manhattan"]
    number_of_clusters = [2, 3, 5]
    linkages = ["single", "complete"]

    for csv_file in all_csv:
        for cluster in number_of_clusters:
            for metric in metrics:
                for linkage in linkages:
                    data = read_csv(csv_file, delimiter=';')

                    print(f"Processing CSV file: {csv_file} - "
                          f"Metric: {metric} - Linkage: {linkage} - Clusters: {cluster}")

                    formatted_csv_file_name = csv_file.split("/")[-1].split(".")[0]

                    save_path = f"../results/task2/normal_graphs/"

                    if os.path.exists(f"../results/task2/normal_graphs/{formatted_csv_file_name}"
                                      f"_{cluster}_{metric}_{linkage}.png"):
                        print("Plot already exists, skipping...")
                        continue

                    aggregated_clusters = agglomerate_clustering(data, metric, linkage, cluster)
                    save_plot(data, aggregated_clusters,
                              f"{formatted_csv_file_name}_{cluster}_{metric}_{linkage}", save_path)


def task_two(chosen_csv):
    metrics = ["cosine", "euclidean", "manhattan"]
    number_of_clusters = [2, 3, 5]
    linkages = ["single", "complete"]

    data = read_csv(chosen_csv, delimiter=';')
    normalized_data = normalize(data)
    standardized_data = standardize(data)

    formatted_csv_file_name = chosen_csv.split("/")[-1].split(".")[0]

    for cluster in number_of_clusters:
        for metric in metrics:
            for linkage in linkages:

                if metric == "euclidean":
                    metric_function = euclidean_distance_matrix
                elif metric == "manhattan":
                    metric_function = manhattan_distance_matrix
                elif metric == "cosine":
                    metric_function = cosine_distance_matrix
                else:
                    raise ValueError("Unknown metric")

                if linkage == "single":
                    linkage_function = np.minimum
                elif linkage == "complete":
                    linkage_function = np.maximum
                else:
                    raise ValueError("Unknown linkage")

                for processed_data, preprocess_name in zip([data, normalized_data, standardized_data],
                                                           ["original", "normalized", "standardized"]):
                    # check if plot already exists
                    if os.path.exists(f"../results/task2/normalized_graphs/{formatted_csv_file_name}_{cluster}_"
                                      f"{metric}_{linkage}_{preprocess_name}.png"):
                        print("Plot already exists, skipping...")
                        continue

                    print(f"Processing CSV file: {formatted_csv_file_name} - Metric: {metric} - "
                          f"Linkage: {linkage} - Clusters: {cluster} - Preprocess: {preprocess_name}")

                    save_path = f"../results/task2/normalized_graphs/"
                    aggregated_clusters = agglomerate_clustering(processed_data, metric_function, linkage_function,
                                                                 cluster)
                    save_plot(processed_data, aggregated_clusters,
                              f"{formatted_csv_file_name}_{cluster}_{metric}_{linkage}_{preprocess_name}", save_path)


if __name__ == '__main__':
    task_one()

    chosen_csv_file = "../datasets/data_clustering/clusters5n.csv"
    task_two(chosen_csv_file)
