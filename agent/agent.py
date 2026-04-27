from google import genai 
from .client import LLMClient, GemeniClient, QwenClient

def buildClient(config:dict)->LLMClient:
    provider = config["provider"]
    model = config["model"]
    if provider == "Google": 
        return GemeniClient(model)
    elif provider == "Qwen":
        return QwenClient(model)
    raise ValueError(f"Unsupported valueError")

def callModel():
    pass


