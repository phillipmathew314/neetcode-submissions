from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    s = 0
    maxName = ""
    for name, score in scores:
        if score > s:
            maxName = name
            s = score
    
    return maxName

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
