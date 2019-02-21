# Pre-Sliced Linear Algebra
This project is inspired by the FLAME notation (also referred to as "Slicing and Dicing") for linear algebra algorithms as presented in the ![Linear Algebra: Foundations to Frontiers](http://ulaff.net/index.html) series of MOOC's from the University of Texas. The goal is to implement the slicing and dicing method in a library which can be used to experiment with and implement linear algebra algorithms in a way which is boilerplate free and highly expressive.

## Table of Contents
- [FLAME Notation](#flame-notation)
- [Motivation](#flame-notation)
- [Implementation](#implementation)
- [Usage](#usage)
- [TODO](#todo)

## FLAME Notation
FLAME notation has a number of advantages over typical representations of linear algebra algorithms:
- It provides a clear visual intuition of how matrices are traversed.
- Indicies are abstracted away - algorithms are defined recursively.
- It lends itself to clean and expressive derivations and proofs.

I will present a simple example below. For more on FLAME notation, see this ![introduction by the wonderful Rob van de Geijn](https://www.youtube.com/watch?v=QCg0VQOUB8E), ![section 4.2 "A Farewell to Indicies" from LAFF: On Programming for Correctness](http://www.cs.utexas.edu/users/rvdg/pubs/LAFFPfC.pdf), and if you want to go further, ![the entire series of LAFF MOOC's.](http://ulaff.net/index.html)

Consider the typical summation notation for the dot-product:

![](https://latex.codecogs.com/svg.latex?x^T&space;y&space;=&space;\sum_{i&space;=&space;1}^{n}{x_i&space;\cdot&space;y_i})

In FLAME notation, this would be represented as follows:

1. Partition vectors *x* and *y* into top and bottom sub-vectors, where initially the top sub-vectors are empty. Set alpha to 0.

![](https://latex.codecogs.com/svg.latex?x%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_T%20%5C%5C%20%5Ccline%7B1-1%7D%20x_B%20%5Cend%7Barray%7D%5Cright%29%2C%20y%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_T%20%5C%5C%20%5Ccline%7B1-1%7D%20y_B%20%5Cend%7Barray%7D%5Cright%29%2C%20%5Calpha%20%3D%200)

2. Expose the top values of the bottom sub-vectors as *chi* and *psi*.

![](https://latex.codecogs.com/svg.latex?%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_T%20%5C%5C%20%5Ccline%7B1-1%7D%20x_B%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_0%20%5C%5C%20%5Ccline%7B1-1%7D%20%5Cchi_1%20%5C%5C%20x_2%20%5Cend%7Barray%7D%5Cright%29%2C%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_T%20%5C%5C%20%5Ccline%7B1-1%7D%20y_B%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_0%20%5C%5C%20%5Ccline%7B1-1%7D%20%5Cpsi_1%20%5C%5C%20y_2%20%5Cend%7Barray%7D%5Cright%29)

3. Use the exposed scalars to update alpha.

![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3A%3D%20%5Calpha%20&plus;%20%5Cchi_1%20%5Ccdot%20%5Cpsi_1)

4. Repartition the vectors by moving the exposed values into the top sub-vectors.

![](https://latex.codecogs.com/svg.latex?%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_T%20%5C%5C%20%5Ccline%7B1-1%7D%20x_B%20%5Cend%7Barray%7D%5Cright%29%20%5Cleftarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_0%20%5C%5C%20%5Cchi_1%20%5C%5C%20%5Ccline%7B1-1%7D%20x_2%20%5Cend%7Barray%7D%5Cright%29%2C%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_T%20%5C%5C%20%5Ccline%7B1-1%7D%20y_B%20%5Cend%7Barray%7D%5Cright%29%20%5Cleftarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_0%20%5C%5C%20%5Cpsi_1%20%5C%5C%20%5Ccline%7B1-1%7D%20y_2%20%5Cend%7Barray%7D%5Cright%29)

5. Repeat steps 2-4 as long as the bottom sub-vectors are non-empty.

6. Once this process is complete, *alpha* will equal the dot-product of *x* and *y*.

We can also traverse vectors and matrices from left to right:

![](https://latex.codecogs.com/svg.latex?x%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20x_L%20%26%20x_R%20%5C%5C%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20x_0%20%26%20%5Cchi_1%20%26%20x_2%20%5C%5C%20%5Cend%7Barray%7D%5Cright%29)

![](https://latex.codecogs.com/svg.latex?A%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20A_L%20%26%20A_R%20%5C%5C%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20A_0%20%26%20a_1%20%26%20A_2%20%5C%5C%20%5Cend%7Barray%7D%5Cright%29)

And matrices diagonally:

![](https://latex.codecogs.com/svg.latex?A%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20A_%7BTL%7D%20%26%20A_%7BTR%7D%20%5C%5C%20%5Chline%20A_%7BBL%7D%20%26%20A_%7BBR%7D%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20A_%7BTL%7D%20%26%20a_%7B01%7D%20%26%20A_%7B02%7D%20%5C%5C%20%5Chline%20a%5ET_%7B10%7D%20%26%20%5Calpha_%7B11%7D%20%26%20a%5ET_%7B12%7D%20%5C%5C%20A_%7B20%7D%20%26%20a_%7B21%7D%20%26%20A_%7B22%7D%20%5Cend%7Barray%7D%5Cright%29)

Blocked algorithms expose sub-matrices instead of vectors and scalars:

![](https://latex.codecogs.com/svg.latex?A%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20A_%7BTL%7D%20%26%20A_%7BTR%7D%20%5C%5C%20%5Chline%20A_%7BBL%7D%20%26%20A_%7BBR%7D%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20A_%7BTL%7D%20%26%20A_%7B01%7D%20%26%20A_%7B02%7D%20%5C%5C%20%5Chline%20A_%7B10%7D%20%26%20A_%7B11%7D%20%26%20A_%7B12%7D%20%5C%5C%20A_%7B20%7D%20%26%20A_%7B21%7D%20%26%20A_%7B22%7D%20%5Cend%7Barray%7D%5Cright%29)

## Motivation
FLAME notation is a wonderful tool for reasoning about linear algebra algorithms. However things start to break down once we go to apply it in code. There exists from the Flame team the ![Spark webpage](http://www.cs.utexas.edu/users/flame/Spark/) where one can generate boilerplate code in a number of languages based on the specified input/output operands and the directions in which they should be traversed. There are a few problems here:
- The need for such a webpage in the first place. It's a bit tedious and a step which can be eliminated.
- The code that is generated is verbose and unclear. It would be very difficult for anyone besides the person who generated the code to figure out what's going on; what operands are there and in what direction are they being traversed. 
- The only part of the code that we really care about is the update section, can we eliminate the clutter?

The goal of this project is to alleviate these pain points by creating an API with which one can immediately jump into experimenting with linear algebra algorithms with next to no boilerplate while being very expressive about the operands involved in an algorithm and the direction in which they are traversed.

## Implementation
Looking at the previous example of FLAME notation, there is a clear set of steps which will be consistent accross all algorithms:
- **Partition** the operands.
- **Expose** values.
- Use the exposed values to **calculate** the desired value.
- **Update** the output operand with the calculation.
- **Repartition** the operands and repeat until all values are in one side of the operand, then output the result.

With this specification in mind the following abstract classes have been created which all operands are based on:

```python
class Operand(ABC):

    @abstractmethod
    def partition(self):
        pass


class PartitionedOperand(ABC):

    @abstractmethod
    def expose(self):
        pass

    @abstractmethod
    def is_complete(self):
        pass

    @abstractmethod
    def combine(self):
        pass


class ExposedOperand(ABC):

    @abstractmethod
    def repartition(self):
        pass

    @abstractmethod
    def exposed_value(self):
        pass

    @abstractmethod
    def update(self, alpha: float):
        pass
```

Concrete types for the three types of operands; scalars, vectors, and matrices, have been/will be implemented based on the above abstract classes, with a different implementation for each direction in which the operands can be traversed:

- Scalar (Most methods for scalar are simply identity)
- TBVector/Matrix (Top-to-bottom)
- BTVector/Matrix (Bottom-to-top)
- LRVector/Matrix (Left-to-right)
- RLVector/Matrix (right-to-left)
- TLBRMatrix (Top-left to bottom-right)
- BRTLMatrix (Bottom-right to top-left)
- TRBLMatrix (Top-right to bottom-left)
- BLTRMatrix (Bottom-left to top-right)

Blocked versions of the diagonally-traversing matrices may also be implemented in the future.

With the above in place, the **apply** function is implemented. This is where the magic happens and the value of this project comes to fruition. The apply function takes an arbitary function and an arbitary number of any sub-types of the Operand class as parameters. It goes through the **partition** -> **expose** -> **calculate** -> **update** -> **repartition** -> **repeat** process for each of the operands, where the **calculate** step is defined by the function that is passed in.

```python
def apply(f, *expression: Operand):
    arity = len(inspect.signature(f).parameters)
    assert arity == len(expression), "The size of the expression did not match the arity of the function."

    partitionings = [x.partition() for x in expression]

    def _apply(f, *expression: PartitionedOperand):
        if all(x.is_complete() for x in expression):
            return expression[-1].combine().value
        else:
            exposes = [x.expose() for x in expression]
            alpha = f(*[x.exposed_value() for x in exposes])
            exposes[-1] = exposes[-1].update(alpha)
            repartitionings = (x.repartition() for x in exposes)
            return _apply(f, *repartitionings)

    return _apply(f, *partitionings)
```

## Usage
Using the apply method with our operand types, we can implement any linear algebra algorithm with a single function where the operands and the direction in which they are traversed are clearly expressed in the type signature, and only the **calculate** step need be defined. Pass all of this into the **apply** function, and you're done.

```python
def axpy(alpha: Scalar, x: TBVector, y: TBVector):

    def kernel(alpha: float, chi: float, psi: float):
        return alpha * chi + psi

    return apply(kernel, alpha, x, y)


def scal(alpha: Scalar, x: TBVector):
    return apply(lambda alpha, x: alpha * x, alpha, x)


def dot_product(x: LRVector, y: TBVector):

    alpha = Scalar(0)

    def kernel(chi: float, psi: float, alpha: float):
        return chi * psi + alpha

    return apply(kernel, x, y, alpha)


def euclidean_length(x: TBVector):
    sum_of_squares = dot_product(x, x)
    return sqrt(sum_of_squares)

```

For very simple operations like the above, a lambda expression might be appropriate as has been done for scal, however I believe it is preferrable to explicitly define a kernel function for readability/expressiveness.

A few notes on usage:
- The output operand should always be the last one passed in to the apply function, as this is the operand that the update step is applied to.
- This is not intended to be a performant linear algebra library for use in production. It is intended for the meta-exploration of linear algebra only.
- The recursion limit on python means that vectors of length greater than 992 will cause an error. Following on from the previous point, this isn't really a concern since there isn't much reason to use this library for vectors and matrices larger than can be easily read at a glance by the human eye.

## TODO
- Implement matrices
- Implement backwards-traversing vectors
- Implement blocked matrices
