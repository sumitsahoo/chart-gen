# ChartGen
Generate charts using OpenAI 3.5 Turbo and Code Interpreter [WIP]

## Dependency Installation

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
<a href="https://www.flaticon.com/free-icons/pie-chart" title="pie chart icons">Pie chart icons created by Pixel perfect - Flaticon</a>
