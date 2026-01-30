# Test Low Coverage Repo

A sample Python project with partial test coverage (~20-30%) for testing AI test generation.

## Structure
- `app.py` - Main module with 20+ functions
- `test_app.py` - Tests only 3 functions (add, subtract, multiply)

## Run Tests
```bash
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing
```
