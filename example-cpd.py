import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Load dataset
df = pd.read_csv("path_to_your_data.csv")

# Define network structure (example with financial variables)
model = BayesianNetwork([
    ('Market_Trend', 'Stock_Performance'),
    ('Economic_Outlook', 'Stock_Performance'),
    ('Stock_Performance', 'Investor_Sentiment')
])

# Initialize Maximum Likelihood Estimator
mle = MaximumLikelihoodEstimator(model, df)

# Estimate CPDs for each node
cpds = {}
for node in model.nodes():
    cpd = mle.estimate_cpd(node)
    cpds[node] = cpd
    print(f"\nCPD for {node}:")
    print(cpd)

# Add CPDs to model
for cpd in cpds.values():
    model.add_cpds(cpd)

# Validate model
print(f"\nModel is valid: {model.check_model()}")

# Perform inference
inference = VariableElimination(model)
result = inference.query(
    variables=['Stock_Performance'], 
    evidence={'Market_Trend': 'Bull'}
)
print(f"\nInference result:")
print(result)
