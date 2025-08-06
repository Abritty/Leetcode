# Leetcode 1768: Merge Strings Alternately
def merge_alternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged.append(word1[i])
        if j < len(word2):
            merged.append(word2[j])
        i += 1
        j += 1
    return ''.join(merged)

# Test cases
if __name__ == "__main__":
    # Test case 1
    word1 = "abc"
    word2 = "pqr"
    print(merge_alternately(word1, word2))  # Expected: "apbqcr"

    # Test case 2
    word1 = "ab"
    word2 = "pqrs"
    print(merge_alternately(word1, word2))  # Expected: "apbqrs"

    # Test case 3
    word1 = "abcd"
    word2 = "pq"
    print(merge_alternately(word1, word2))  # Expected: "apbqcd"
    # Test case 4
    word1 = ""
    word2 = "pq"
    print(merge_alternately(word1, word2))