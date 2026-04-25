from google import genai 
from .client import LLMClient, GemeniClient

def buildClient(config:dict)->LLMClient:
    provider = config["provider"]
    model = config["model"]
    if provider == "Google": 
        return GemeniClient(model)
    raise ValueError(f"Unsupported valueError")

def callModel():
    pass


