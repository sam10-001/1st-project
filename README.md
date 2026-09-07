# 1st-project
# Projectile Motion Simulator

A physics simulation project exploring projectile motion using both exact kinematics and numerical methods.

## What this project covers
- Exact trajectory calculation using standard kinematics equations 
- Comparison of different launch angles (including verifying that complementary angles, e.g. 30°/60°, give equal range)
- Euler's method: simulating motion step-by-step instead of using a  closed-form formula, and comparing its accuracy against the exact  solution at different step sizes (dt), also noted that increasing dt leads to increase in error
- Adding air resistance (quadratic drag) — a case where no exact formula exists, so numerical simulation becomes necessary rather than optional, which happens in real world

## What I learned
- How numerical integration (Euler's method) approximates continuous motion, and how step size affects accuracy
- How drag forces are modeled and why they require numerical methods
- Practical Python: NumPy arrays, Matplotlib plotting, functions, loops