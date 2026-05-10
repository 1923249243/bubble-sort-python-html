# Bubble Sort Python + HTML

A tiny bubble sort demo with a Python Flask API and an interactive HTML page.

## Features

- Sort numbers with bubble sort
- Show every pass of the algorithm
- Use a browser UI or call the API directly
- Includes basic Python tests

## Project Structure

```text
.
├── app.py
├── bubble_sort.py
├── requirements.txt
├── test_bubble_sort.py
└── templates
    └── index.html
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Run Tests

```bash
pytest
```

## API Example

```bash
curl -X POST http://127.0.0.1:5000/api/sort \
  -H "Content-Type: application/json" \
  -d "{\"numbers\":[5,3,8,1,2]}"
```
