from pydantic_settings import BaseSettings

# Get all newly created products periodically (1h interval)
class ValidatorSettings(BaseSettings):
    # == Scoring ==
    iteration_interval: int = 60*60  # Every Hour
    max_allowed_weights: int = 400  # Query dynamically based on your subnet settings.
    foo: int | None = None  # Anything else that you wish to implement.
