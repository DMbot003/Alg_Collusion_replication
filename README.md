# Alg_Collusion_replication
# Artificial Intelligence, Algorithmic Pricing, and Collusion - Code Description


## Overview
This README explains how to use the code for the paper written Calvano et al. (2019). The code simulates experiments from the paper using FORTRAN, with outputs processed in R/RStudio to generate figures and tables. We modified the original codes for input parameters varies and run the implement with less number of parameter pairs and less repeated experiments due to computational efficiency. To verify the codes from the original paper, for a specified pair of parameters, we also implemented the Q-learning pricing algorithms in python and made it interacting with each others in the economic environment. Moreover, we also write the codes to preceed the outputs to generate figures and tables in python for the convience. Finally, to verify whether the advanced algorithm with efficiency can be applied in this context, we also implement DQN in python.

### Key Components
- **Executables:**
  - `baseline.exe`: Main experiments.
  - `stochasticdemand.exe`: Stochastic demand case (Section 6.3).
  - `entryexit.exe`: Variable market structure case (Section 6.4).
- **Inputs:** Parameters read from `A_InputParameters.txt`.
- **Outputs:** Text files with simulation results, processed by R scripts.

## Folder Structure
- 'fcode_Fortran': FORTRAN source code and executables.
- 'Rscripts': R scripts and input files for paper figures/tables.
- 'pythoncode': Python code for implementing Q-learning algorithm and DQN algorithm

## Requirements
- **FORTRAN Compiler:** Intel Visual FORTRAN Compiler XE 13.1.2 (Windows, 64-bit).
- **R and RStudio:** Version 4.0.2 (R) and 1.3.959 (RStudio).
- **Python and Tensorflow**
- **Redistributables:** Intel FORTRAN Compiler 2017 libraries ([download](https://software.intel.com/en-us/articles/redistributables-for-intel-parallel-studio-xe-2017-composer-edition-for-windows)).

## Building and Running
1. **Compile (Optional):** Use provided source code with Intel Visual FORTRAN and OpenMP directives.
2. **Run Executables:** Place `A_InputParameters.txt` in the same folder as the executable and double-click to run. Note: Some tasks may take days and generate large files (several GB).

## Input Parameters (`A_InputParameters.txt`)
- **Common Parameters:** Define experiment settings (e.g., number of agents, iterations).
- **Experiment Parameters:** Specific settings per experiment (e.g., learning rates, demand parameters).

## Output Files
- **Simulation Results:** Text files (e.g., `A_res.txt`, `InfoExperiment_XXXX.txt`).
- **R Processing:** Use R scripts to generate figures (PDF) or tables (TXT).

## Example: Replicating Table I
1. Copy `baseline.exe` to `\AER_code\AER_paper_Rscripts\table_I`.
2. Run `baseline.exe` in that folder.
3. Run `\table_I\table_I.R` in RStudio to generate `Table_I.txt`.

## References
- Calvano, E., et al. (2019). *Artificial Intelligence, Algorithmic Pricing and Collusion*. University of Bologna.
- Press, W.H., et al. (1992). *Numerical Recipes in Fortran 77* (2nd ed.). Cambridge University Press.
