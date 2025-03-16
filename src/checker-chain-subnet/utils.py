from typing import Literal, Any
import datetime
import requests
from .models.unreviewed_product import UnreviewedProductApiResponse

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

def fetch_product_data(product_id):
    """Fetch product data from the API using the product ID."""
    url = f"https://backend.checkerchain.com/api/v1/products/{product_id}"
    response = requests.get(url)
    if response.status_code == 200:
        productData = UnreviewedProductApiResponse.from_dict(
            response.json())
        if not (isinstance(productData, UnreviewedProductApiResponse)):
            return None
        return productData.data
    else:
        print("Error fetching product data:",
              response.status_code, response.text)
        return None