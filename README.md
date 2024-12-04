# Mandelbrot Set Generator
Mandelbrot Set Generator is a tool implemented in Python and Cython for generating the Mandelbrot set. It supports two main algorithms: Escape Time and Coloring Algorithms. The project is designed to quickly generate the Mandelbrot set and provide colorful visualizations.

## Quickstart
### Installation
```
python -m venv .venv # Create a virtual environment
source .\.venv\Scripts\activate # activate environment (windows)
# ./.venv/bin/activate # activate environment (linux/mac/WSL)
pip install pytest # Install pytest in virtual environment
pip install -e . # Install locally
```

### Test
```
pytest -s .\test\test.py #(windows)
pytest -s ./test/test.py #(linux/mac/WSL)
```