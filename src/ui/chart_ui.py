import gradio as gr
import os
from src.util.log_util import LogUtil
from src.util.chart_util import ChartUtil


class ChartUI:
    def __init__(self):
        self.chart_util = ChartUtil()
        self.log = LogUtil()
        self.theme = gr.themes.Base(
            primary_hue="red",
            secondary_hue="red",
        ).set(
            # button_primary_background_fill="*secondary_500",
            button_primary_background_fill="#2196F3",
            button_primary_background_fill_dark="*primary_500",
            button_primary_text_color="white",
            loader_color="#2196F3",
        )

    def launch_ui(self):
        # Check if index is built

        custom_css = """
            
            footer {visibility: hidden}
        """

        with gr.Blocks(
            title="ChartGen",
            theme=self.theme,
            # css=custom_css,
        ) as chart_gen:
            gr.Image(
                "./images/logo.svg",
                height=80,
                width=400,
                interactive=False,
                container=False,
                show_download_button=False,
            )

            gr.Interface(
                fn=self.chart_util.generate_chart,
                inputs=[gr.Textbox(label="Enter the data for chart generation")],
                outputs=[
                    gr.Image(label="Generated Chart"),
                    gr.Markdown(label="Chart Description"),
                ],
                allow_flagging=False,
            )

        chart_gen.queue().launch(
            favicon_path="./images/favicon.ico",
            # auth=("user", "user@1234"),
            auth_message="Welcome to ChartGen. Please enter the username and password to continue.",
            debug=False,
            show_api=False,
            server_name="0.0.0.0",
            server_port=8080,
            share=False,
            allowed_paths=["./images/", "./outputs/"],
        )
