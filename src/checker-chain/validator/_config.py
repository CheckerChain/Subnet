from pydantic_settings import BaseSettings


class ValidatorSettings(BaseSettings):
    # == Scoring ==
    iteration_interval: int = 800  # Set, accordingly to your tempo.
    max_allowed_weights: int = 400  # Query dynamically based on your subnet settings.
    foo: int | None = None  # Anything else that you wish to implement.
    use_testnet: bool = True  # Set to True if you are using the testnet.
    netuid: int = 52  # The network UID.
