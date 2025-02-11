from typing import Literal, Any
import datetime
import requests
from .sqlite_utils import add_product, get_products, update_product_status

def get_checker_chain_unmined_product_ids():
    url = "https://backend.checkerchain.com/api/v1/products?page=1&limit=30"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = response.json()
    
    if "data" not in data or "products" not in data["data"]:
        return "Invalid data structure."

    products = data["data"]["products"]
    if not products:
        return "No products found."

    # Fetch existing product IDs from the database
    all_products = get_products()
    existing_product_ids = {p["_id"] for p in all_products}
    unmined_products = [product for product in all_products if not product["mining_done"]]

    for product in products:
        if product["_id"] not in existing_product_ids:
            add_product(product["_id"], product["name"])
            unmined_products.append(product["_id"]);
        
        # Update all products status:
        # if product.isReviewed:
        #     update_product_status(product["_id"], check_chain_review_done=True, trust_score=product["trustScore"]);
    
    return unmined_products;

def get_product(product_id:str):
    url = "https://backend.checkerchain.com/api/v1/products/"+product_id
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if "data" not in data:
        return None
    return data

    data = response.json()

def iso_timestamp_now() -> str:
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    iso_now = now.isoformat()
    return iso_now


def log(
    msg: str,
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: Any | None = None,
    flush: Literal[False] = False,
):
    print(
        f"[{iso_timestamp_now()}] " + msg,
        *values,
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )

