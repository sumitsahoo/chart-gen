from openai import OpenAI


class ChartUtil:
    def __init__(self):
        self.client = OpenAI()
        self.assistant = self.client.beta.assistants.create(
            name="ChartGen",
            instructions="You are great at creating beautiful data visualizations. You analyze data and come up with data visualizations relevant to the data. You also share a brief text summary of the data visualization.",
            model="gpt-4-1106-preview",
            tools=[{"type": "code_interpreter"}],
        )
    
    def generate_chart(self, message, history):
        # TODO: Implement this method
