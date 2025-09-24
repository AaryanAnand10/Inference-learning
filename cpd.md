# Detailed CPD Calculation for Bayesian Network Prediction

Let me walk you through a complete step-by-step calculation of Conditional Probability Distributions (CPDs) to perform prediction in a Bayesian network.

## 🏗️ Setting Up the Network Structure

Let's use a classic example with three variables:
- **Rain** (R): {Yes, No}
- **Sprinkler** (S): {On, Off} 
- **Grass Wet** (G): {Wet, Dry}

**Network Structure**: Rain → Grass Wet ← Sprinkler

## 📊 Step 1: Define the CPD Tables

#### **Prior CPD for Rain**
```
P(R) = {
    P(Rain = Yes) = 0.3
    P(Rain = No) = 0.7
}
```

#### **Prior CPD for Sprinkler**
```
P(S) = {
    P(Sprinkler = On) = 0.4
    P(Sprinkler = Off) = 0.6
}
```

#### **Conditional CPD for Grass Wet**
```
P(G|R,S) = {
    P(Grass = Wet | Rain = Yes, Sprinkler = On) = 0.95
    P(Grass = Wet | Rain = Yes, Sprinkler = Off) = 0.8
    P(Grass = Wet | Rain = No, Sprinkler = On) = 0.85
    P(Grass = Wet | Rain = No, Sprinkler = Off) = 0.1
    
    P(Grass = Dry | Rain = Yes, Sprinkler = On) = 0.05
    P(Grass = Dry | Rain = Yes, Sprinkler = Off) = 0.2
    P(Grass = Dry | Rain = No, Sprinkler = On) = 0.15
    P(Grass = Dry | Rain = No, Sprinkler = Off) = 0.9
}
```

## 🎯 Step 2: Prediction Query Example

**Query**: What's the probability that the grass is wet given that we observe rain?
**Mathematical notation**: P(Grass = Wet | Rain = Yes)

## 🔄 Step 3: Apply the Inference Formula

Since Sprinkler is not observed, we need to marginalize over it:

```
P(G = Wet | R = Yes) = Σ P(G = Wet | R = Yes, S = s) × P(S = s)
```

## 📝 Step 4: Detailed Calculation

#### **Calculate for Sprinkler = On**
```
P(G = Wet | R = Yes, S = On) × P(S = On)
= 0.95 × 0.4
= 0.38
```

#### **Calculate for Sprinkler = Off**
```
P(G = Wet | R = Yes, S = Off) × P(S = Off)
= 0.8 × 0.6
= 0.48
```

#### **Sum the Results**
```
P(G = Wet | R = Yes) = 0.38 + 0.48 = 0.86
```

## 🧮 Step 5: Complete Joint Probability Calculation

For a more complex prediction, let's calculate the joint probability of all variables.

#### **Calculate P(R = Yes, S = On, G = Wet)**

**Step 5a**: Use the chain rule of probability
```
P(R, S, G) = P(R) × P(S) × P(G|R, S)
```

**Step 5b**: Substitute values
```
P(R = Yes, S = On, G = Wet) = P(R = Yes) × P(S = On) × P(G = Wet | R = Yes, S = On)
= 0.3 × 0.4 × 0.95
= 0.114
```

## 📊 Step 6: Normalization for Conditional Queries

When we have evidence, we need to normalize. Let's calculate P(S | G = Wet).

#### **Step 6a**: Calculate unnormalized probabilities

**For S = On:**
```
P(S = On, G = Wet) = Σ P(R = r, S = On, G = Wet)
= P(R = Yes, S = On, G = Wet) + P(R = No, S = On, G = Wet)
= (0.3 × 0.4 × 0.95) + (0.7 × 0.4 × 0.85)
= 0.114 + 0.238
= 0.352
```

**For S = Off:**
```
P(S = Off, G = Wet) = Σ P(R = r, S = Off, G = Wet)
= P(R = Yes, S = Off, G = Wet) + P(R = No, S = Off, G = Wet)
= (0.3 × 0.6 × 0.8) + (0.7 × 0.6 × 0.1)
= 0.144 + 0.042
= 0.186
```

#### **Step 6b**: Calculate normalizing constant
```
Z = P(G = Wet) = P(S = On, G = Wet) + P(S = Off, G = Wet)
= 0.352 + 0.186
= 0.538
```

#### **Step 6c**: Normalize to get final probabilities
```
P(S = On | G = Wet) = P(S = On, G = Wet) / P(G = Wet)
= 0.352 / 0.538
= 0.654

P(S = Off | G = Wet) = P(S = Off, G = Wet) / P(G = Wet)
= 0.186 / 0.538
= 0.346
```

## ✅ Step 7: Verification

Check that probabilities sum to 1:
```
P(S = On | G = Wet) + P(S = Off | G = Wet) = 0.654 + 0.346 = 1.0 ✓
```

## 🎯 Key Takeaways for CPD Calculations

1. **Identify Dependencies**: Understand which variables depend on others
2. **Apply Chain Rule**: Break down joint probabilities using conditional independence
3. **Marginalize**: Sum over unobserved variables when needed
4. **Normalize**: Ensure probabilities sum to 1 when computing conditionals
5. **Verify Results**: Always check that your final probabilities are valid

This systematic approach allows you to perform any prediction query in a Bayesian network by leveraging the CPD structure and applying fundamental probability rules.
