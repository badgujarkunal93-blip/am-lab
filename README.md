# AM Lab Practicals

Python implementations of the AM (Applied Mathematics) practical programs, arranged lab-wise. Each program is in a separate file and accepts values from the user instead of relying on one fixed example dataset.

## Repository structure

### Lab 1 — Matrices
| Practical | Program |
|---|---|
| Gauss Elimination | [01_gauss_elimination.py](Lab-1-Matrices/01_gauss_elimination.py) |
| Matrix Multiplication | [02_matrix_multiplication.py](Lab-1-Matrices/02_matrix_multiplication.py) |
| Inverse of a 2 x 2 Matrix | [03_inverse_of_2x2_matrix.py](Lab-1-Matrices/03_inverse_of_2x2_matrix.py) |
| Eigenvalues, Eigenvectors and Diagonalization | [04_eigenvalues_eigenvectors_diagonalization.py](Lab-1-Matrices/04_eigenvalues_eigenvectors_diagonalization.py) |

### Lab 2 — Probability Distributions
| Practical | Program |
|---|---|
| Binomial Distribution | [01_binomial_distribution.py](Lab-2-Probability/01_binomial_distribution.py) |
| Normal Distribution | [02_normal_distribution.py](Lab-2-Probability/02_normal_distribution.py) |
| Joint PMF of Two Dice | [03_joint_pmf_two_dice.py](Lab-2-Probability/03_joint_pmf_two_dice.py) |
| Central Limit Theorem | [04_central_limit_theorem.py](Lab-2-Probability/04_central_limit_theorem.py) |
| t and F Distribution Samples | [05_t_and_f_distribution.py](Lab-2-Probability/05_t_and_f_distribution.py) |

### Lab 3 — Hypothesis Testing
| Practical | Program |
|---|---|
| Z-test for Single Mean | [01_z_test_single_mean.py](Lab-3-Hypothesis-Testing/01_z_test_single_mean.py) |
| t-test for Difference of Means | [02_t_test_difference_of_means.py](Lab-3-Hypothesis-Testing/02_t_test_difference_of_means.py) |
| Z-test for Single Proportion | [03_z_test_single_proportion.py](Lab-3-Hypothesis-Testing/03_z_test_single_proportion.py) |
| F-test for Comparison of Variances | [04_f_test_comparison_of_variances.py](Lab-3-Hypothesis-Testing/04_f_test_comparison_of_variances.py) |

### Lab 5 — Correlation and Regression
| Practical | Program |
|---|---|
| Karl Pearson Correlation | [01_pearson_correlation.py](Lab-5-Correlation-Regression/01_pearson_correlation.py) |
| Spearman Rank Correlation | [02_spearman_rank_correlation.py](Lab-5-Correlation-Regression/02_spearman_rank_correlation.py) |
| Simple Linear Regression | [03_simple_linear_regression.py](Lab-5-Correlation-Regression/03_simple_linear_regression.py) |
| Multiple Linear Regression | [04_multiple_linear_regression.py](Lab-5-Correlation-Regression/04_multiple_linear_regression.py) |

## Setup

Python 3.9 or newer is recommended.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run any program from the repository root, for example:

```bash
python Lab-1-Matrices/01_gauss_elimination.py
```

On Windows, use `py` instead of `python` if that is how Python is configured:

```bash
py Lab-2-Probability/01_binomial_distribution.py
```

## Notes

- Inputs are requested at runtime, so you can try different matrices, sample sizes, significance levels and datasets.
- Programs that draw graphs require Matplotlib.
- Hypothesis-testing programs report the p-value and use the selected significance level to decide whether to reject the null hypothesis.
- The 2 x 2 eigenvalue practical follows the manual characteristic-equation approach from the supplied practical code.
- The t-test for two means follows the pooled-variance method in the supplied lab sheet.
- The multiple-regression program uses a least-squares solver to avoid directly inverting the normal-equation matrix, while retaining the same regression model.
- The joint PMF practical follows the two-fair-dice sample space from the supplied code.

## Repository

[GitHub: badgujarkunal93-blip/am-lab](https://github.com/badgujarkunal93-blip/am-lab)
