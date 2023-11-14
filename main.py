from dotenv import load_dotenv
from src.ui.chart_ui import ChartUI

# Launch the Gradio UI

if __name__ == "__main__":
    # Take environment variables from .env.
    load_dotenv()
    chart_ui = ChartUI()
    chart_ui.launch_ui()
