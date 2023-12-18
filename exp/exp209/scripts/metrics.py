import numpy as np
from typing import List

def ap_at_k(user_relevances: List[int], k: int) -> float:
    if sum(user_relevances[:k]) == 0:
        return 0.0
    nonzero_indices = np.asarray(user_relevances[:k]).nonzero()[0]
    return sum([sum(user_relevances[: idx + 1]) / (idx + 1) for idx in nonzero_indices]) / sum(user_relevances[:k])

def map_at_k(users_relevances: List[List[int]], k: int) -> float:
    return float(np.mean([ap_at_k(user_relevances, k) for user_relevances in users_relevances]))
