
# Genetic Algorithm for Different Types of Variables

This repository contains the implementation of a **genetic algorithm** designed to work with various types of variables, including binary variables, permutations, and real numbers. It is a metaheuristic-based solution for optimization problems that require a flexible and generalizable approach.

## Prerequisites

To effectively use and understand this project, it is recommended to have prior knowledge of **metaheuristics** and **genetic algorithms**, as the code is based on advanced concepts such as population evolution, crossover operators, mutation, and selection.

### Technologies Used

- Python 3.8+
- Standard Python libraries for data structure manipulation

## Main Files

- `Binario.py`: Implementation of the genetic algorithm for binary variables.
- `Permutacion.py`: Implementation of the genetic algorithm for permutation problems.
- `Real.py`: Implementation of the genetic algorithm for real-valued variables.
- `Individuo.py`: Defines the base class for individuals in the population, compatible with different types of variables.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. Install the necessary dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each file contains a modular implementation of the genetic algorithm logic for its respective variable type. You can adapt it to your specific optimization needs by creating new instances and configuring genetic operators based on your problem.

To run one of the modules, simply execute the script in Python:

```bash
python Binario.py
```

or

```bash
python Permutacion.py
```

## Contributions

Contributions are welcome. If you find any issues or think you can improve the code, feel free to open an issue or submit a pull request.
