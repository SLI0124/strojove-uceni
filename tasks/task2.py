import os
import math
import time
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
    with open(file_path, 'r') as f:
        lines = f.readlines()
        _data = [list(map(float, line.strip().split(delimiter))) for line in lines if line.strip()]
    return _data


def euclidean_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def manhattan_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def cosine_distance(x, y):
    dot_product = sum(a * b for a, b in zip(x, y))
    norm_x = math.sqrt(sum(a ** 2 for a in x))
    norm_y = math.sqrt(sum(b ** 2 for b in y))
    return 1 - (dot_product / (norm_x * norm_y))


def single_linkage(cluster1, cluster2, metric):
    min_distance = float("inf")
    for point1 in cluster1:
        for point2 in cluster2:
            distance = metric(point1, point2)
            if distance < min_distance:  # the minimum distance between two clusters
                min_distance = distance
    return min_distance


def complete_linkage(cluster1, cluster2, metric):
    max_distance = 0
    for point1 in cluster1:
        for point2 in cluster2:
            distance = metric(point1, point2)
            if distance > max_distance:  # the maximum distance between two clusters
                max_distance = distance
    return max_distance


def agglomerate_clustering(data, metric, linkage, n_clusters):
    clusters = [[point] for point in data]  # Each point is a cluster at the beginning
    while len(clusters) > n_clusters:  # Merge clusters until the desired number of clusters is reached
        print(f"Clusters: {len(clusters)}/{n_clusters}")
        min_distance = float("inf")
        closest_clusters = None
        for i, cluster1 in enumerate(clusters):
            for j, cluster2 in enumerate(clusters):  # Compare all clusters
                if i == j:  # Skip the same cluster
                    continue
                distance = linkage(cluster1, cluster2, metric)  # Calculate the distance between two clusters
                if distance < min_distance:  # Find the closest clusters
                    min_distance = distance  # Update the minimum distance for the closest clusters
                    closest_clusters = (i, j)  # Update the closest clusters for merging
        i, j = closest_clusters  # Merge the closest clusters
        clusters[i].extend(clusters[j])  # Add the second cluster to the first cluster
        clusters.pop(j)  # Remove the second cluster since it is merged
    return clusters


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
                    time_start = time.time()
                    data = read_csv(csv_file, delimiter=';')

                    if metric == "euclidean":
                        metric_function = euclidean_distance
                    elif metric == "manhattan":
                        metric_function = manhattan_distance
                    else:
                        raise ValueError("Unknown metric")

                    if linkage == "single":
                        linkage_function = single_linkage
                    elif linkage == "complete":
                        linkage_function = complete_linkage
                    else:
                        raise ValueError("Unknown linkage")

                    # print all the parameters
                    print(f"Processing CSV file: {csv_file} - "
                          f"Metric: {metric} - Linkage: {linkage} - Clusters: {cluster}")

                    formatted_csv_file_name = csv_file.split("/")[-1].split(".")[0]

                    save_path = f"../results/task2/normal_graphs/"

                    if os.path.exists(f"../results/task2/normal_graphs/{formatted_csv_file_name}"
                                      f"_{cluster}_{metric}_{linkage}.png"):
                        print("Plot already exists, skipping...")
                        continue

                    aggregated_clusters = agglomerate_clustering(data, metric_function, linkage_function, cluster)
                    save_plot(data, aggregated_clusters,
                              f"{formatted_csv_file_name}_{cluster}_{metric}_{linkage}", save_path)
                    print(f"Time elapsed: {time.time() - time_start}")


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
                time_start = time.time()

                metric_function = cosine_distance
                linkage_function = single_linkage if linkage == "single" else complete_linkage

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
                    print(f"Time elapsed: {time.time() - time_start}")


if __name__ == '__main__':
    task_one()

    chosen_csv_file = "../datasets/data_clustering/clusters5n.csv"
    task_two(chosen_csv_file)
