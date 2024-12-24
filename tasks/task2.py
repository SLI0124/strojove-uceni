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

DATASET_PATH = "../datasets/data_clustering"
RESULTS_PATH = "../results/task2"


def get_all_csv_paths():
    all_paths = []
    for root, dirs, files in os.walk(DATASET_PATH):
        for file in files:
            if file.endswith(".csv") and file != "winequality-red.csv":
                all_paths.append(os.path.join(root, file))
    # Fix for Windows paths
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
        closest_clusters = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)
        i, j = sorted(closest_clusters)

        clusters[i].extend(clusters[j])  # Merge the clusters
        clusters.pop(j)

        if linkage == "single":
            new_distances = np.minimum(distance_matrix[i], distance_matrix[j])
        elif linkage == "complete":
            new_distances = np.maximum(distance_matrix[i], distance_matrix[j])
        else:
            raise ValueError("Unknown linkage")

        distance_matrix[i] = new_distances
        distance_matrix[:, i] = new_distances
        distance_matrix = np.delete(distance_matrix, j, axis=0)
        distance_matrix = np.delete(distance_matrix, j, axis=1)
        np.fill_diagonal(distance_matrix, np.inf)

    return [[data[idx] for idx in cluster] for cluster in clusters]


def save_plot(data, save_path, n_rows, n_cols, dataset_name, number_of_clusters, metrics, linkages):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(24, 18))
    axes = axes.flatten()

    plot_idx = 0
    for cluster in number_of_clusters:
        for metric in metrics:
            for linkage in linkages:
                ax = axes[plot_idx]
                for x in data:
                    ax.scatter(float(x[0]), float(x[1]))

                aggregated_clusters = agglomerate_clustering(data, metric, linkage, cluster)
                for i, cluster_group in enumerate(aggregated_clusters):
                    for point in cluster_group:
                        ax.scatter(point[0], point[1], color=cluster_colors[i])

                ax.set_title(f"Clusters: {cluster}, Metric: {metric}, Linkage: {linkage}")
                plot_idx += 1

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    plt.tight_layout()
    plt.savefig(f"{save_path}/{dataset_name}.png")
    plt.clf()


def normalize(data):
    min_values = [min([row[i] for row in data]) for i in range(len(data[0]))]
    max_values = [max([row[i] for row in data]) for i in range(len(data[0]))]

    normalized_data = []
    for row in data:
        normalized_row = [
            (row[i] - min_values[i]) / (max_values[i] - min_values[i]) if max_values[i] - min_values[i] > 0 else 0
            for i in range(len(row))
        ]
        normalized_data.append(normalized_row)

    return normalized_data


def standardize(data):
    means = [sum([row[i] for row in data]) / len(data) for i in range(len(data[0]))]
    std_devs = [math.sqrt(sum([(row[i] - means[i]) ** 2 for row in data]) / len(data)) for i in range(len(data[0]))]

    standardized_data = []
    for row in data:
        standardized_row = [
            (row[i] - means[i]) / std_devs[i] if std_devs[i] > 0 else 0
            for i in range(len(row))
        ]
        standardized_data.append(standardized_row)

    return standardized_data


def task_one():
    all_csv = get_all_csv_paths()
    metrics = ["euclidean", "manhattan"]
    number_of_clusters = [2, 3, 5]
    linkages = ["single", "complete"]

    for csv_file in all_csv:
        data = read_csv(csv_file, delimiter=';')
        formatted_csv_file_name = os.path.basename(csv_file).split(".")[0]

        save_path = os.path.join(RESULTS_PATH, "non_normalized")

        if os.path.exists(f"{save_path}/{formatted_csv_file_name}_non_normalized.png"):
            print(f"Plot for {formatted_csv_file_name} already exists, skipping...")
            continue

        print(f"Processing CSV file: {csv_file}")

        save_plot(data, save_path, len(number_of_clusters), len(metrics) * len(linkages),
                  formatted_csv_file_name, number_of_clusters, metrics, linkages)


def task_two(chosen_csv):
    metrics = ["cosine", "euclidean", "manhattan"]
    number_of_clusters = [2, 3, 5]
    linkages = ["single", "complete"]

    data = np.array(read_csv(chosen_csv, delimiter=';'))
    normalized_data = np.array(normalize(data))
    standardized_data = np.array(standardize(data))

    formatted_csv_file_name = os.path.basename(chosen_csv).split(".")[0]

    save_path = os.path.join(RESULTS_PATH, "normalized")

    if os.path.exists(f"{save_path}/{formatted_csv_file_name}_non_normalized.png"):
        print(f"Plot for {formatted_csv_file_name} already exists, skipping...")
    else:
        print(f"Processing CSV file: {chosen_csv}")
        save_plot(data, save_path, len(number_of_clusters), len(metrics) * len(linkages),
                  formatted_csv_file_name, number_of_clusters, metrics, linkages)

    save_plot(normalized_data, save_path, len(number_of_clusters), len(metrics) * len(linkages),
              f"{formatted_csv_file_name}_normalized", number_of_clusters, metrics, linkages)

    save_plot(standardized_data, save_path, len(number_of_clusters), len(metrics) * len(linkages),
              f"{formatted_csv_file_name}_standardized", number_of_clusters, metrics, linkages)


if __name__ == '__main__':
    task_one()

    chosen_csv_file = "../datasets/data_clustering/clusters5n.csv"
    task_two(chosen_csv_file)
