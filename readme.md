# Homework 5 - Command Pattern and Plugin architecture

# Calculator Project

This project is a simple calculator implemented in Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator is designed using object-oriented principles and showcases various design patterns, including class methods, static methods, and a calculation history feature.

Additionally implements command pattern and plugin architecture

## Features

- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero)
- Store a history of calculations
- Retrieve the last calculation
- Clear the calculation history
- Uses `Decimal` for high-precision arithmetic

## Addtional Features

- Implemented Command Pattern along with Menu command
- Implemented Plugin architecture to dynamically load the commands
- Implemented multiprocessing

## Install Instructions

1. Clone
2. Install the requirements
```bash
pip3 install -r requirements.txt
```

# Running the application

```bash
python main.py
```
![alt text](image.png)

## Testing 
This project includes extensive unit tests for each feature and operation. Testing is done using the pytest framework, and code linting is handled by pylint to ensure code quality.

The project has been fully tested using pytest and pylint

```bash
pytest --num_records=100
pytest --pylint --cov
pytest --pylint --cov --cov-report=xml --cov-report=term-missing
```
## Testing results:
1. pytest --num_records=10

![alt text](image-3.png)

2. pytest --pylint --cov

![alt text](image-2.png)

3. pytest --pylint --cov --cov-report=xml --cov-report=term-missing

![alt text](image-1.png)


