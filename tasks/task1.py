from itertools import combinations
from collections import defaultdict


def apriori(filename, min_sup, min_conf):
    # Step 1: Read file and store transactions
    transactions = []
    with open(filename, 'r') as file:
        for line in file:
            transaction = line.strip().split()
            transactions.append(transaction)

    total_transactions = len(transactions)

    # Step 2: Calculate minimum support count from percentage
    min_support_count = (min_sup / 100) * total_transactions

    print(f"Processing  {filename} with Min Support: {min_sup}% and Min Confidence: {min_conf}%\n")

    # Step 3: Generate candidate 1-item-sets
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[(item,)] += 1

    # Step 4: Filter candidate item-sets to get frequent 1-item-sets
    initial_list = {item_set: count for item_set, count in item_counts.items() if count >= min_support_count}
    frequent_item_sets = initial_list.copy()

    print(f"Found {len(initial_list)} frequent 1-item-sets")

    # Step 5: Generate larger item-sets using frequent item-sets
    k = 2
    while initial_list:  # Continue until no more frequent item-sets can be generated at the end of the loop
        print(f"Generating candidate {k}-item-sets")
        # Generate candidate k-item-sets by combining frequent (k-1)-item-sets
        candidate_item_sets = defaultdict(int)
        items = list(initial_list.keys())
        for i in range(len(items)):
            for j in range(i + 1, len(items)):  # Generate new candidates by combining every pair of item-sets
                # Combine two item-sets to get new candidate
                new_candidate = tuple(sorted(set(items[i]).union(set(items[j]))))
                if len(new_candidate) == k:
                    # Count the frequency of the new candidate in the transactions to filter it later
                    candidate_item_sets[new_candidate] = sum(1 for transaction in transactions
                                                             if set(new_candidate).issubset(transaction))

        # Filter candidates to get frequent k-item-sets
        initial_list = {item_set: count for item_set, count in candidate_item_sets.items() if
                        count >= min_support_count}
        frequent_item_sets.update(initial_list)

        print(f"Found {len(initial_list)} frequent {k}-item-sets")

        k += 1  # Move to the next item-set size

    # Step 6: Generate and filter association rules based on confidence
    print("\nAssociation Rules:")
    for item_set, count in frequent_item_sets.items():
        if len(item_set) > 1:  # We need at least 2 items to generate a rule
            for i in range(1, len(item_set)):
                subsets = combinations(item_set, i)
                for subset in subsets:
                    # The rule is: subset -> (item_set - subset)
                    remaining_items = set(item_set) - set(subset)
                    if remaining_items:  # Ensure that the remaining items are not empty
                        subset_support = frequent_item_sets.get(tuple(sorted(subset)), 0)
                        if subset_support > 0:  # Ensure that the subset is a frequent item-set
                            confidence = count / subset_support
                            if confidence >= min_conf / 100:  # Filter rules based on confidence
                                print(f"Rule: {subset} -> {remaining_items}, Confidence: {confidence:.2f},"
                                      f" Support: {count / total_transactions:.2f}")

    # Step 7: Print frequent item-sets
    print("\nFrequent Item-Sets:")
    for item_set, count in frequent_item_sets.items():
        print(f"Item-Set: {item_set}, Support: {count / total_transactions:.2f}, Confidence: {count:.2f}")
    print()

    # step 8: Print the total count of k-item-sets
    print(f"Total count of k-item-sets with {min_sup}% support:")
    for i in range(1, k):
        count = sum(1 for item_set in frequent_item_sets.keys() if len(item_set) == i)
        print(f"Total count of {i}-item-sets: {count}" if count > 0 else "\n")


if __name__ == "__main__":
    # test #1
    myapriori_filename = "../datasets/itemsets_test.dat"
    min_support = 25
    min_confidence = 50
    apriori(myapriori_filename, min_support, min_confidence)

    # test #2
    myapriori_filename = "../datasets/itemsets_test.dat"
    min_support = 15
    min_confidence = 50
    apriori(myapriori_filename, min_support, min_confidence)

    # chess dataset
    myapriori_filename = "../datasets/chess.dat"
    min_support = 90
    min_confidence = 80
    apriori(myapriori_filename, min_support, min_confidence)

    # connect dataset
    myapriori_filename = "../datasets/connect.dat"
    min_support = 98
    min_confidence = 95
    apriori(myapriori_filename, min_support, min_confidence)
