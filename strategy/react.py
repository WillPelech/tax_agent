import json
from agent.client import LLMClient
from registry import ToolRegistry


REACT_PROMPT = """You are in a ReAct loop.

Each turn, output exactly one block in one of these two shapes.

To use a tool:

Thought: I need last year's 1040 form for information.
Action: lookup_form
Action Input: {"form": "1040", "year": 2025}

To finish:

Thought: I have everything needed.
Final Answer: You owe $50,000 in taxes.
"""


class ReActStep:
    def __init__(self, thought=None, action=None, action_input=None, final=None):
        self.thought = thought
        self.action = action
        self.action_input = action_input
        self.final = final

    @classmethod
    def parse(cls, text: str) -> "ReActStep":
        step = cls()
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("Thought:"):
                step.thought = line[len("Thought:") :].strip()
            elif line.startswith("Action:"):
                step.action = line[len("Action:") :].strip()
            elif line.startswith("Action Input:"):
                step.action_input = line[len("Action Input:") :].strip()
            elif line.startswith("Final Answer:"):
                step.final = line[len("Final Answer:") :].strip()
        return step

    def is_done(self) -> bool:
        return self.final is not None

async def run(client: LLMClient, task: str, tool_registry: ToolRegistry, max_steps: int = 10):
    transcript = [REACT_PROMPT, f"Task: {task}"]

    for _ in range(max_steps):
        response = await client.chat("\n".join(transcript))
        transcript.append(response)

        step = ReActStep.parse(response)

        if step.is_done():
            return step.final

        if step.action and step.action_input:
            try:
                observation = await tool_registry.call_tool(step.action, json.loads(step.action_input))
            except Exception as e:
                observation = f"error: {e}"
        else:
            observation = f"unknown action: {step.action}"

        transcript.append(f"Observation: {observation}")

    return None
