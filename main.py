import yaml
from agent.agent import buildClient
from agent.prompt import base_prompt 

def main():
    with open("config.yaml") as f: 
        config = yaml.safe_load(f)
    client = buildClient(config)
    response = client.chat(base_prompt)
    print(response)
    




if __name__ == "__main__":
    main()
