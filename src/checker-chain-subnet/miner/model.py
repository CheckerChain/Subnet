import asyncio
from http.client import HTTPResponse
from typing import List
from communex.module import Module, endpoint
from communex.key import generate_keypair
from keylimiter import TokenBucketLimiter

from .llm import generate_review_score
from .util import get_overall_score
from utils import fetch_product_data

class Miner(Module):
    """
    A module class for mining and generating responses to prompts.

    Attributes:
        None

    Methods:
        generate: Generates a response to a given prompt using a specified model.
    """

    @endpoint
    async def generate(self, prompt: List[str], model: str = "foo"):
        """
        Generates a response to a given prompt using a specified model.

        Args:
            prompt: The prompt to generate a response for.
            model: The model to use for generating the response (default: "gpt-3.5-turbo").

        Returns:
            None
        """
        tasks = []
        for product_id in prompt:
            product = fetch_product_data(product_id)
            if product:
                tasks.append(generate_review_score(product))

        # Execute all API calls concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)
        # Extract overall scores safely, handling exceptions
        predictions = []
        for res in results:
            try:
                if isinstance(res, Exception):
                    raise res  # Re-raise exception to handle it below
                score = get_overall_score(res)
                predictions.append(score)
            except Exception as e:
                print(f"Error processing result: {e}")
                predictions.append(None)
        print(f"Answering: `{prompt}` with model `{model}`")
        return HTTPResponse(content={"answer":predictions})


if __name__ == "__main__":
    """
    Example
    """
    from communex.module.server import ModuleServer
    import uvicorn

    key = generate_keypair()
    miner = Miner()
    refill_rate = 1 / 400
    # Implementing custom limit
    bucket = TokenBucketLimiter(2, refill_rate)
    server = ModuleServer(miner, key, ip_limiter=bucket, subnets_whitelist=[3])
    app = server.get_fastapi_app()

    # Only allow local connections
    uvicorn.run(app, host="127.0.0.1", port=8000)
