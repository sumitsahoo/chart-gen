from openai import OpenAI


class ChartUtil:
    def __init__(self):
        self.client = OpenAI()
        self.assistant = self.client.beta.assistants.create(
            instructions="You are a personal assistant called 'ChartGen'. When asked to create a chart, write and run code to generate the chart.",
            model="gpt-4-1106-preview",
            tools=[{"type": "code_interpreter"}],
        )
    
    def generate_chart(self, message, history):
        # TODO: Implement this method
