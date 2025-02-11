import asyncio
import random
import requests
import concurrent

miners = range(20);
score_dict = {};

def get_first_product():
    url = "https://backend.checkerchain.com/api/v1/products?page=1&limit=30"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "products" in data["data"]:
            products = data["data"]["products"]
            if products:
                return products[0]  # Return the first product
            else:
                return "No products found."
        else:
            return "Invalid data structure."
    else:
        return f"Error: {response.status_code}"

def simulate_mining(num):
    # Simulate a trust score between 0 and 100
    trust_score = min(max(int(random.uniform(0, 100)), 0), 100)
    if(trust_score < 20):
        trust_score = None
    return trust_score

async def run_mining_threads(num_threads=30):
    with concurrent.futures.ThreadPoolExecutor(num_threads) as executor:
        tasks = executor.map(simulate_mining,[0 for num in miners])
    return [*tasks]

def score_miner (miner_trust, actual_trust): 
    if not miner_trust or miner_trust < 0 or miner_trust > 100: 
        return 0
    # Calculate the absolute difference
    deviation = abs(miner_trust - actual_trust)
    score = 100 - deviation  
    return score

if __name__ == "__main__":
    # Get the first product
    product = get_first_product()
    print("First Product:", product.get("name"))
    print("Trust Score:", product.get("trustScore"))
    # Run the mining simulation
    scores = asyncio.run(run_mining_threads())
    for miner, miner_response in zip(miners, scores):
        score_dict[miner] = score_miner(miner_response, product.get("trustScore"))
        
    sorted_scores = sorted(score_dict.items(), key= lambda item: item[1], reverse=True);
    sorted_scores_dict =  [{'miner': miner, 'score': score} for miner, score in sorted_scores]
    print("Generated Trust Scores:", scores)
    print("Generated Trust Scores:", sorted_scores_dict)
