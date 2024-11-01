from itertools import combinations
from collections import defaultdict


def read_transactions(filename):
    transactions = []
    with open(filename, 'r') as file:
        for line in file:
            transaction = line.strip().split()
            transactions.append(transaction)
    return transactions


def calculate_min_support_count(min_sup, total_transactions):
    return (min_sup / 100) * total_transactions


def generate_candidate_1_item_sets(transactions):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[(item,)] += 1
    return item_counts


def filter_frequent_item_sets(item_counts, min_support_count):
    return {item_set: count for item_set, count in item_counts.items() if count >= min_support_count}


def generate_candidate_k_item_sets(initial_list, transactions, k):
    candidate_item_sets = defaultdict(int)
    items = list(initial_list.keys())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            new_candidate = tuple(sorted(set(items[i]).union(set(items[j]))))
            if len(new_candidate) == k:
                candidate_item_sets[new_candidate] = sum(1 for transaction in transactions
                                                         if set(new_candidate).issubset(transaction))
    return candidate_item_sets


def generate_association_rules(frequent_item_sets, total_transactions, min_conf):
    rules = []
    for item_set, count in frequent_item_sets.items():
        if len(item_set) > 1:
            for i in range(1, len(item_set)):
                subsets = combinations(item_set, i)
                for subset in subsets:
                    remaining_items = set(item_set) - set(subset)
                    if remaining_items:
                        subset_support = frequent_item_sets.get(tuple(sorted(subset)), 0)
                        if subset_support > 0:
                            confidence = count / subset_support
                            if confidence >= min_conf / 100:
                                rules.append((subset, remaining_items, confidence, count / total_transactions))
    return rules


def print_results(all_frequent_item_sets, total_transactions, rules):
    print("\nFrequent Item-Sets:")
    for item_set, count in all_frequent_item_sets.items():
        print(f"Item-Set: {item_set}, Support: {count / total_transactions:.2f}, Confidence: {count:.2f}")

    print("\nAssociation Rules:")
    for rule in rules:
        subset, remaining_items, confidence, support = rule
        print(f"Rule: {subset} -> {remaining_items}, Confidence: {confidence:.2f}, Support: {support:.2f}")

    print(f"\nTotal count of k-item-sets with minimum support:")
    for i in range(1, max(len(item_set) for item_set in all_frequent_item_sets.keys()) + 1):
        count = sum(1 for item_set in all_frequent_item_sets.keys() if len(item_set) == i)
        print(f"Total count of {i}-item-sets: {count}" if count > 0 else "")


def apriori(filename, min_sup, min_conf):
    transactions = read_transactions(filename)
    total_transactions = len(transactions)

    min_support_count = calculate_min_support_count(min_sup, total_transactions)

    print(f"Processing {filename} with Min Support: {min_sup}% and Min Confidence: {min_conf}%\n")

    initial_item_counts = generate_candidate_1_item_sets(transactions)
    frequent_item_sets = filter_frequent_item_sets(initial_item_counts, min_support_count)

    all_frequent_item_sets = frequent_item_sets.copy()

    print(f"Found {len(frequent_item_sets)} frequent 1-item-sets")

    k = 2
    while frequent_item_sets:
        print(f"Generating candidate {k}-item-sets")
        candidate_item_sets = generate_candidate_k_item_sets(frequent_item_sets, transactions, k)
        frequent_item_sets = filter_frequent_item_sets(candidate_item_sets, min_support_count)

        if frequent_item_sets:
            all_frequent_item_sets.update(frequent_item_sets)
            print(f"Found {len(frequent_item_sets)} frequent {k}-item-sets")

        k += 1

    rules = generate_association_rules(all_frequent_item_sets, total_transactions, min_conf)
    print_results(all_frequent_item_sets, total_transactions, rules)


def run_apriori_tests():
    test_cases = [
        ("../datasets/itemsets_test.dat", 25, 50),
        ("../datasets/itemsets_test.dat", 15, 50),
        ("../datasets/chess.dat", 90, 80),
        ("../datasets/connect.dat", 98, 95)
    ]

    for filename, min_support, min_confidence in test_cases:
        apriori(filename, min_support, min_confidence)


if __name__ == "__main__":
    run_apriori_tests()
