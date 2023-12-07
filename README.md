# ChartGen
Generate charts using OpenAI 3.5 Turbo and Code Interpreter with Assistants API.<br>
More on Assistants API: https://platform.openai.com/docs/assistants/overview

## Medium Article
View my Medium article on ChartGen here: https://medium.com/@sumitsahoo/generate-charts-using-openai-code-interpreter-88cb93a06da0

## Dependency Installation

You need `Python 3.12.0` installed in your system. If you are using `pyenv` then check the version using command: `pyenv version`

1. Install poetry
    ```bash
    # Using pip
    pip install poetry
    
    # Using brew (macOS), if you are using pyenv you should use `pip install poetry`
    brew install poetry
    ```
2. Install the dependencies and create virtual environment
    Make poetry create virtual environment within project folder
    ```bash
    poetry config virtualenvs.in-project true
    ```
    Now, install dependency and create the environment
    ```bash
    poetry install
    ```
3. Activate the virtual environment and enter into the shell
    ```bash
    poetry shell
    ```    
4. Run the app
    ```python
    python3 main.py
    ```
To update dependencies use: `poetry update`<br>
To view virtual environment location, use: `poetry env info --path`<br>
To generate `requirements.txt` using poetry, use below command:
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

## Attributions
<a href="https://www.gradio.app/" title="gradio ui">UI is built using Gradio</a><br>
<a href="https://www.flaticon.com/free-icons/pie-chart" title="pie chart icons">Pie chart icons created by Pixel perfect - Flaticon</a>

## License

MIT License

Copyright (c) 2023 Sumit Sahoo

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
