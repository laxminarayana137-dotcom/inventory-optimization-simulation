import numpy as np
import pandas as pd

# Simulation
num_simulations = 100

# Inventory
initial_inventory = 500
order_qty = 400
lead_time = 3

# Cost parameters
holding_cost_per_unit = 1
ordering_cost = 50
stockout_cost = 20

# Different ROP values
ROP_values = [250, 300, 350, 400, 450]

# Store final results
results = []

# DIFFERENT ROP LOOP
for ROP in ROP_values:

    all_stockouts = []
    all_service_levels = []
    all_costs = []

    for sim in range(num_simulations):

        inventory = initial_inventory
        stockouts = 0
        successful_days = 0
        orders = []
        total_cost = 0

        for day in range(1, 31):

            demand = np.random.randint(90, 150)

            # Stockout check
            if demand > inventory:
                stockouts += 1
                total_cost += stockout_cost
                inventory = 0
            else:
                inventory -= demand
                successful_days += 1

            # Order arrival
            while day in orders:
                inventory += order_qty
                orders.remove(day)

            # Place order
            if inventory < ROP and len(orders) == 0:
                arrival_day = day + lead_time
                orders.append(arrival_day)
                total_cost += ordering_cost

            # Holding cost
            total_cost += inventory * holding_cost_per_unit

        # Store simulation results
        service_level = successful_days / 30
        all_service_levels.append(service_level)
        all_stockouts.append(stockouts)
        all_costs.append(total_cost)

    # Average results for this ROP
    avg_service_level = sum(all_service_levels) / num_simulations
    avg_stockouts = sum(all_stockouts) / num_simulations
    avg_cost = sum(all_costs) / num_simulations

    # Store final results
    results.append({
        "ROP": ROP,
        "Avg_Service_Level": avg_service_level,
        "Avg_Stockouts": avg_stockouts,
        "Avg_Cost": avg_cost
    })

# Convert to DataFrame
df = pd.DataFrame(results)

# Export to CSV
df.to_csv("inventory_simulation_results.csv", index=False)

print("CSV file created successfully!")
print(df)

import os
print(os.getcwd())