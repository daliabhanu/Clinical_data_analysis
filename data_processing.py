import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split

def prepare_data(data):
    df = pd.DataFrame(data)

    # Tokenize and label each word in the abstract as "ENTITY" or "OTHER"
    all_abstracts = " ".join(df['Abstract'])
    tokenized_abstracts = all_abstracts.split()
    word_counts = Counter(tokenized_abstracts)

    # Define a simple labeling strategy (assign "ENTITY" label to rare words)
    threshold = 1  # Adjust this threshold as needed
    word_labels = {word: "ENTITY" if count <= threshold else "OTHER" for word, count in word_counts.items()}

    # Create labeled sequences
    labeled_sequences = [[(word, word_labels[word]) for word in abstract.split()] for abstract in df['Abstract']]

    # Split data into training and testing sets
    train_data, test_data = train_test_split(labeled_sequences, test_size=0.2, random_state=42)

    return train_data, test_data, word_labels
