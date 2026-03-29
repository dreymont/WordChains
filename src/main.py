

def is_one_letter_different(word1, word2):
    one_letter = sum(a != b for a, b in zip(word1, word2))
    return one_letter == 1

def find_neighbors(word, wordlist):
    neighbors = [w for w in wordlist if is_one_letter_different(word, w) is True]
    return neighbors


def find_chain(start, end, dictionary):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        current_word = path[-1]
        if current_word == end:
            return path

        neighbors = find_neighbors(current_word, dictionary)
        visited.add(current_word)
        for neighbor in neighbors:

            if neighbor not in visited:
                queue.append(path + [neighbor])

def load_dictionary(filepath, word_length):
    with open(filepath) as f:
        lines = f.readlines()
    words = [line.strip().lower() for line in lines[1:] if line.strip()]
    return [w for w in words if len(w) == word_length]


