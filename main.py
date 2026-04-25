import yaml
from agent.agent import buildClient

def main():
    with open("config.yaml") as f: 
        config = yaml.safe_load(f)
    client = buildClient(config)
    response = client.chat("hello")
    print(response)
    




if __name__ == "__main__":
    main()
