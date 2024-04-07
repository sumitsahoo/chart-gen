# 📊 ChartGen
Generate charts using OpenAI (gpt-3.5-turbo-0125 or gpt-4-0125-preview) and Code Interpreter with Assistants API.<br>
More on Assistants API: https://platform.openai.com/docs/assistants/overview

## 📖 Medium Article
View my Medium article on ChartGen here: https://medium.com/@sumitsahoo/generate-charts-using-openai-code-interpreter-88cb93a06da0

## 📦 Dependency Installation

You need `Python 3.12.2` installed in your system. If you are using `pyenv` then check the version using command: `pyenv version`

1. Install poetry
    ```bash
    # Linux, macOS, Windows (WSL): https://python-poetry.org/docs/#installing-with-the-official-installer
    curl -sSL https://install.python-poetry.org | python3 -
    ```
2. Set poetry to create virtual environment within project folder
    ```bash
    poetry config virtualenvs.in-project true
    ```
3. Install dependency and create the virtual environment
    ```bash
    poetry install
    ``` 
4. Run the app with poetry
    ```python
    poetry run python main.py
    ```
To update dependencies use: `poetry update`<br>
To view virtual environment location, use: `poetry env info --path`<br>
To generate `requirements.txt` using poetry, you need to have export plugin installed.<br>
Install the plugin:
```bash
poetry self add poetry-plugin-export
```
Once the plugin is installed, use `export` command to generate `requirements.txt`
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

## 🙏🏻 Attributions
<a href="https://www.gradio.app/" title="gradio ui">UI is built using Gradio</a><br>
<a href="https://www.flaticon.com/free-icons/pie-chart" title="pie chart icons">Pie chart icons created by Pixel perfect - Flaticon</a>

## 📜 License

MIT License

Copyright (c) 2024 Sumit Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
