import random


def simulate_mining(num):
    # Simulate a trust score between 0 and 100
    trust_score = min(max(int(random.uniform(0, 100)), 0), 100)
    return trust_score