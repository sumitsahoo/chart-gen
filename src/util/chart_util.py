from openai import OpenAI
from src.util.log_util import LogUtil

import os
import time


class ChartUtil:
    def __init__(self):
        self.log = LogUtil()
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        # self.assistant = self.client.beta.assistants.create(
        #     name="ChartGen",
        #     instructions="You are great at creating beautiful data visualizations. You analyze data and come up with data visualizations relevant to the data. You also share a brief text summary of the data visualization.",
        #     model="gpt-4-1106-preview",
        #     tools=[{"type": "code_interpreter"}],
        # )

    def generate_chart(self, message, history):
        # Prepare the prompt
        ci_prompt = "Please generate a chart using following data: " + message

        try:
            # Create a thread and run the assistant
            thread = self.client.beta.threads.create(
                messages=[
                    {
                        "role": "user",
                        "content": ci_prompt,
                    }
                ]
            )

            # Run the assistant
            run = self.client.beta.threads.runs.create(
                assistant_id=os.environ["OPENAI_ASSISTANT_ID"], thread_id=thread.id
            )

            # Poll the run status until it is completed
            while True:
                # Refresh the run to get the latest status
                run = self.client.beta.threads.runs.retrieve(
                    run_id=run.id, thread_id=thread.id
                )

                if run.status == "completed":
                    self.log.info("Generated chart, Run finished")

                    # Get list of messages in the thread
                    messages = self.client.beta.threads.messages.list(
                        thread_id=thread.id
                    )

                    # Get the latest message in the thread and retrieve file id
                    image_file_id = messages.data[0].content[0].image_file.file_id

                    # Get the raw response from the file id
                    raw_response = self.client.files.with_raw_response.content(
                        file_id=image_file_id
                    )

                    # Delete generated file
                    self.client.files.delete(image_file_id)

                    # Save the generated chart to a file
                    with open(self.chart_out_path, "wb") as f:
                        f.write(raw_response.content)
                        return (self.chart_out_path,)

                elif run.status == "failed":
                    self.log.error("Unable to generate chart")
                    break

                # Wait for a short period before polling again to avoid hitting rate limits
                time.sleep(1)
        except Exception as e:
            self.log.error(e)

        return "🤔 Could you please rephrase your query and try again?"
