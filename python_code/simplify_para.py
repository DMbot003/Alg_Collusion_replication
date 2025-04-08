import csv

# Define the ranges and number of steps
alpha_min, alpha_max = 0.0025, 0.25
beta_min, beta_max = 0.005, 0.5

# We want 1,000 rows; closest grid is 32x31 = 992, so we'll add 8 more rows
alpha_steps = 32  # 32 unique alpha values
beta_steps = 31   # 31 unique beta values gives 992 rows, then we adjust
total_rows = 1000

# Calculate step sizes
alpha_step = (alpha_max - alpha_min) / (alpha_steps - 1)
beta_step = (beta_max - beta_min) / (beta_steps - 1)

# Fixed values for other columns
fixed_values = {
    'PrintQ': 0,
    'Delta': 0.95,
    'a0': 0,
    'a1': 2,
    'a2': 2,
    'c1': 1,
    'c2': 1,
    'mu': 0.25,
    'extend1': 0.1,
    'extend2': 0.1,
    'NashP1': 1.47293,
    'NashP2': 1.47293,
    'CoopP1': 1.92498,
    'CoopP2': 1.92498,
    'typeQ1': 'O',
    'par1Q1': 0,
    'par2Q1': 0,
    'typeQ2': 'O',
    'par1Q2': 0,
    'par2Q2': 0
}

# Header rows
header_rows = [
    ["Number of experiments:", 1000, 1000],
    ["Number of cores", 25],
    ["Number of sessions", 100],
    ["Iterations per episode", 25000],
    ["Maximum number of episodes", 50000],
    ["Performance measurement period length:", 4],
    ["Number of Agents:", 2],
    ["Memory:", 1],
    ["Number of Prices:", 15],
    ["Type of Exploration Mechanism (1 = exponentially decreasing epsilon (beta); 2 = Boltzmann)", 1],
    ["Type of Payoff Input (1 = Singh & Vives demand; 2 = Logit demand; 3 = Logit demand with zero sigma (perfect competition))", 2],
    ["Compute Impulse Response analysis with a one-period deviation to static Best Response (0 = No; 1 = Yes)", 1],
    ["Compute Impulse Response analysis with a temporary or permanent deviation to Nash (0 = No; 1000 = Permanent; 999 >= X >= 1 = Duration of temporary shock)", 1],
    ["Compute Impulse Response analysis with a one-period deviation to all prices (0 = No; 1 = Yes)", 1],
    ["Compute Equilibrium Check (0 = No, 1 = Yes)", 1],
    ["Compute Q Gap w.r.t. Maximum (0 = NO; 1 = YES)", 1],
    ["Compute Learning Trajectory (X1 = 0 : NO; X1 > 0 : number of checkpoints; X2 > 0 : number of iterations between checkpoints)", 0, 0],
    ["Compute Detailed Analysis (0 = No; 1 = Yes)", 0]
]

# Column headers for experiment rows
experiment_headers = [
    "Experiment", "PrintQ", "Alpha1", "Alpha2", "Beta_1", "Beta_2", "Delta",
    "a0", "a1", "a2", "c1", "c2", "mu", "extend1", "extend2",
    "NashP1", "NashP2", "CoopP1", "CoopP2", "typeQ1", "par1Q1", "par2Q1",
    "typeQ2", "par1Q2", "par2Q2"
]

# Generate the data
data = []
experiment_num = 1

# Create the 32x31 grid (992 rows)
for i in range(alpha_steps):
    alpha = round(alpha_min + i * alpha_step, 4)
    for j in range(beta_steps):
        beta = round(beta_min + j * beta_step, 4)
        row = [
            experiment_num, fixed_values['PrintQ'], alpha, alpha, beta, beta,
            fixed_values['Delta'], fixed_values['a0'], fixed_values['a1'],
            fixed_values['a2'], fixed_values['c1'], fixed_values['c2'],
            fixed_values['mu'], fixed_values['extend1'], fixed_values['extend2'],
            fixed_values['NashP1'], fixed_values['NashP2'], fixed_values['CoopP1'],
            fixed_values['CoopP2'], fixed_values['typeQ1'], fixed_values['par1Q1'],
            fixed_values['par2Q1'], fixed_values['typeQ2'], fixed_values['par1Q2'],
            fixed_values['par2Q2']
        ]
        data.append(row)
        experiment_num += 1

# Add 8 more rows to reach 1,000 (e.g., repeat the last row or interpolate)
# Here, we'll repeat the last row for simplicity
last_row = data[-1]
for _ in range(total_rows - len(data)):
    new_row = last_row.copy()
    new_row[0] = experiment_num  # Update experiment number
    data.append(new_row)
    experiment_num += 1

# Write to CSV
with open('modified_experiments.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write header rows
    for row in header_rows:
        writer.writerow(row)
    
    # Write experiment headers
    writer.writerow(experiment_headers)
    
    # Write experiment data
    for row in data:
        writer.writerow(row)

print(f"Generated CSV with {len(data)} rows in 'modified_experiments.csv'")