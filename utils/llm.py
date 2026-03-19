import os
from dotenv import load_dotenv

load_dotenv()

# Prefer explicit provider selection; otherwise choose based on available keys.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "").strip().lower()
if not LLM_PROVIDER:
    if OPENAI_API_KEY:
        LLM_PROVIDER = "openai"
    elif GOOGLE_API_KEY:
        LLM_PROVIDER = "gemini"
    else:
        LLM_PROVIDER = "openai"

LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0"))

if LLM_PROVIDER in ("gemini", "google", "gen"):
    try:
        import google.genai as genai
        from google.genai.types import GenerateContentConfig
    except ImportError as e:
        raise ImportError(
            "To use Gemini as the LLM provider, install google-genai (pip install google-genai)"
        ) from e

    if not GOOGLE_API_KEY:
        raise RuntimeError(
            "GOOGLE_API_KEY must be set to use Gemini. "
            "Set GOOGLE_API_KEY in your environment or in .env, or set LLM_PROVIDER=openai and provide OPENAI_API_KEY."
        )

    # Ensure the environment key is available to the SDK.
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

    # Instantiate the client once for reuse.
    client = genai.Client()

    from langchain_core.prompt_values import PromptValue
    from langchain_core.runnables.base import Runnable

    class GeminiLLM(Runnable[PromptValue, str]):
        """Wrapper to use Google Gemini (Generative AI) as an LLM in LangChain."""

        def __init__(
            self,
            model: str | None = None,
            temperature: float | None = None,
        ) -> None:
            # Use a recent supported Gemini model. Change via GEMINI_MODEL env var.
            self.model = model or os.getenv("GEMINI_MODEL", "models/gemini-2.5-flash")
            self.temperature = (
                temperature if temperature is not None else LLM_TEMPERATURE
            )

        def invoke(self, prompt: PromptValue, config=None, **kwargs):
            prompt_text = prompt.to_string() if hasattr(prompt, "to_string") else str(prompt)

            response = client.models.generate_content(
                model=self.model,
                contents=prompt_text,
                config=GenerateContentConfig(temperature=self.temperature),
            )

            # Response object exposes `.text` for the generated content.
            text = getattr(response, "text", None)
            if text is None:
                parts = getattr(response, "parts", None) or []
                if parts:
                    first = parts[0]
                    text = getattr(first, "text", None) or getattr(first, "content", None)

            if text is None:
                text = str(response)

            return text

    llm = GeminiLLM()

else:
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. "
            "Set OPENAI_API_KEY in your environment or in .env, or set LLM_PROVIDER=gemini and provide GOOGLE_API_KEY."
        )

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=LLM_TEMPERATURE,
        api_key=OPENAI_API_KEY,
    )
