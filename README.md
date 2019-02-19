# Pre-Sliced Linear Algebra
This project is inspired by the FLAME notation (also referred to as "Slicing and Dicing") of linear algebra algorithms as presented in the ![Linear Algebra: Foundations to Frontiers](http://ulaff.net/index.html) series of MOOC's from the University of Texas. The goal is to implement the slicing and dicing method in a library which can be used to experiment with and implement linear algebra algorithms in a way which is boilerplate free and highly expressive.

## FLAME Notation
FLAME notation has a number of advantages over typical representations of linear algebra algorithms such as summation notation and set comprehensions:
- It provides a clear visual intuition of how matrices are traversed.
- Indicies are abstracted away, algorithms are defined recursively.
- They lend themselves to clean and expressive derivations and proofs.

I will present a simple example below. For more on FLAME notation, see this ![introduction by the wonderful Rob van de Geijn](https://www.youtube.com/watch?v=QCg0VQOUB8E), and ![section 4.2 "A Farewell to Indicies" of LAFF: On Programming for Correctness](http://www.cs.utexas.edu/users/rvdg/pubs/LAFFPfC.pdf).

Consider the typical summation notation for the dot-product:

![](https://latex.codecogs.com/svg.latex?x^T&space;y&space;=&space;\sum_{i&space;=&space;1}^{n}{x_i&space;\cdot&space;y_i})

In FLAME notation, this would be represented as follows:

1. Partition vectors *x* and *y* into top and bottom sub-vectors, where initially the top sub-vectors are empty. Set alpha to 0.

![](https://latex.codecogs.com/svg.latex?x%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_T%20%5C%5C%20%5Ccline%7B1-1%7D%20x_B%20%5Cend%7Barray%7D%5Cright%29%2C%20y%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_T%20%5C%5C%20%5Ccline%7B1-1%7D%20y_B%20%5Cend%7Barray%7D%5Cright%29%2C%20%5Calpha%20%3D%200)

2. Expose the top values of the bottom sub-vectors as *chi* and *psi1*

![](https://latex.codecogs.com/svg.latex?%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_T%20%5C%5C%20%5Ccline%7B1-1%7D%20x_B%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_0%20%5C%5C%20%5Ccline%7B1-1%7D%20%5Cchi_1%20%5C%5C%20x_2%20%5Cend%7Barray%7D%5Cright%29%2C%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_T%20%5C%5C%20%5Ccline%7B1-1%7D%20y_B%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_0%20%5C%5C%20%5Ccline%7B1-1%7D%20%5Cpsi_1%20%5C%5C%20y_2%20%5Cend%7Barray%7D%5Cright%29)

3. Use the exposed scalars to update alpha

![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3A%3D%20%5Calpha%20&plus;%20%5Cchi_1%20%5Ccdot%20%5Cpsi_1)

4. Repartition the vectors by moving the exposed values into the top sub-vectors.

![](https://latex.codecogs.com/svg.latex?%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_T%20%5C%5C%20%5Ccline%7B1-1%7D%20x_B%20%5Cend%7Barray%7D%5Cright%29%20%5Cleftarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20x_0%20%5C%5C%20%5Cchi_1%20%5C%5C%20%5Ccline%7B1-1%7D%20x_2%20%5Cend%7Barray%7D%5Cright%29%2C%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_T%20%5C%5C%20%5Ccline%7B1-1%7D%20y_B%20%5Cend%7Barray%7D%5Cright%29%20%5Cleftarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7D%20y_0%20%5C%5C%20%5Cpsi_1%20%5C%5C%20%5Ccline%7B1-1%7D%20y_2%20%5Cend%7Barray%7D%5Cright%29)

5. Repeat steps 2-4 as long as the bottom sub-vectors are non-empty.

6. Once this process is complete, *alpha* will equal the dot-product of *x* and *y*

We can also traverse vectors and matrices from left to right:

![](https://latex.codecogs.com/svg.latex?A%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20A_L%20%26%20A_R%20%5C%5C%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20A_0%20%26%20%5Calpha_1%20%26%20A_2%20%5C%5C%20%5Cend%7Barray%7D%5Cright%29)

And matrices diagonally:

![](https://latex.codecogs.com/svg.latex?A%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20A_%7BTL%7D%20%26%20A_%7BTR%7D%20%5C%5C%20%5Chline%20A_%7BBL%7D%20%26%20A_%7BBR%7D%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20A_%7BTL%7D%20%26%20a_%7B01%7D%20%26%20A_%7B02%7D%20%5C%5C%20%5Chline%20a%5ET_%7B10%7D%20%26%20%5Calpha_%7B11%7D%20%26%20a%5ET_%7B12%7D%20%5C%5C%20A_%7B20%7D%20%26%20a_%7B21%7D%20%26%20A_%7B22%7D%20%5Cend%7Barray%7D%5Cright%29)

Blocked algorithms expose sub-matrices instead of scalars:

![](https://latex.codecogs.com/svg.latex?A%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Cc%7D%20A_%7BTL%7D%20%26%20A_%7BTR%7D%20%5C%5C%20%5Chline%20A_%7BBL%7D%20%26%20A_%7BBR%7D%20%5Cend%7Barray%7D%5Cright%29%20%5Crightarrow%20%5Cleft%28%5Cbegin%7Barray%7D%7Bc%7Ccc%7D%20A_%7BTL%7D%20%26%20A_%7B01%7D%20%26%20A_%7B02%7D%20%5C%5C%20%5Chline%20A_%7B10%7D%20%26%20A_%7B11%7D%20%26%20A_%7B12%7D%20%5C%5C%20A_%7B20%7D%20%26%20A_%7B21%7D%20%26%20A_%7B22%7D%20%5Cend%7Barray%7D%5Cright%29)
