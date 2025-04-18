from .config import StdConfig
from pydantic import Field

class AIConfig(StdConfig):
    """
    Configuration for AI-related settings.
    """
    openai_api_key: str = Field(
        default=None,
        description="OpenAI API key",
        env="OPENAI_API_KEY",
        arg_short="-k",
        arg_long="--openai-api-key",
    )
