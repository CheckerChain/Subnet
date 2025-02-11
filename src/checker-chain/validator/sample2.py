"""
Sample without any communex code
"""
import asyncio
import concurrent.futures
import random
import re
import time
from functools import partial

from ..utils import log
from ..sqlite_utils import create_db, get_a_product, get_predictions_for_product, add_prediction,update_product_status


IP_REGEX = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+")

class TextValidator():
    
    def _get_miner_prediction(
        self,
        question: str,
    ) -> str | None:
        trust_score = min(max(int(random.uniform(0, 100)), 0), 100)
        if(trust_score < 20):
            trust_score = None
        return trust_score

    def _score_miner(self, product_trust_score:float, miner_answer: float | None) -> float:
        if not miner_answer:
            return 0

        return 0
    
    def score_miners(self):
        product = get_a_product(check_chain_review_done=True, mining_done=True)
        miners = get_predictions_for_product(product["_id"])
        score_dict: dict[int, float] = {}
        for miner in miners:
            score = self._score_miner(product['trust_score'], miner['miner_id'])
            score_dict[miner['miner_id']] = score
        if not score_dict:
            log("No miner managed to give a valid answer")
            return None

        # the blockchain call to set the weights
        # _ = set_weights(settings, score_dict, self.netuid, self.client, self.key)
        

    def get_miner_prompt(self) -> str:
        """
        Get one unmined product from our sqlite db
        Returns:
            The generated prompt for the miner modules.
        """
        product = get_a_product(mining_done=False)
        update_product_status(product["_id"], None, True, None);
        # Implement your custom prompt generation logic here
        return product["_id"];

    async def validate_step(
        self
    ) -> None:
        """
        Perform a validation step.

        Generates questions based on the provided settings, prompts modules to generate answers,
        and scores the generated answers against the validator's own answers.

        Args:
            syntia_netuid: The network UID of the subnet.
        """
        score_dict: dict[int, float] = {}

        product = get_a_product(mining_done=False)
        # miner_prompt = self.get_miner_prompt()
        miner_prompt = product["_id"]
        
        get_miner_prediction = partial(self._get_miner_prediction, miner_prompt)
        miners = ["MIN001","MIN002","MIN003","MIN004","MIN005","MIN006","MIN007","MIN008","MIN009"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            it = executor.map(get_miner_prediction, miners)
            miner_answers = [*it]

        for uid, miner_response in zip(miners, miner_answers):
            miner_answer = miner_response
            if not miner_answer:
                log(f"Skipping miner {uid} that didn't answer")
                continue

            add_prediction(product_id=product["_id"], miner_id=uid, prediction=miner_answer);
            # score = self._score_miner(miner_answer)
            # time.sleep(0.5)
            # # score has to be lower or eq to 1, as one is the best score, you can implement your custom logic
            # assert score <= 1
            # score_dict[uid] = score

        # if not score_dict:
        #     log("No miner managed to give a valid answer")
        #     return None

        update_product_status(product["_id"], None, True, None);
        # the blockchain call to set the weights
        # _ = set_weights(settings, score_dict, self.netuid, self.client, self.key)

    def validation_loop(self) -> None:
        """
        Run the validation loop continuously based on the provided settings.

        Args:
            settings: The validator settings to use for the validation loop.
        """

        while True:
            start_time = time.time()
            unmined = get_a_product(mining_done=False);
            mined_and_ready_to_score = get_a_product(mining_done=True, check_chain_review_done=True)
            if unmined is not None:
                _ = asyncio.run(self.validate_step())
            elif mined_and_ready_to_score is not None:
                _ = self.score_miners()
            else:
                elapsed = time.time() - start_time
                if elapsed < 300:
                    sleep_time = 300 - elapsed
                    log(f"Sleeping for {sleep_time}")
                    time.sleep(sleep_time)


if __name__ == "__main__":
    validator = TextValidator(
        )
    create_db();
    validator.validation_loop()
