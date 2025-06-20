import math

def main():
  
  # Here there are declared 4 lists for the cans info.
  can_names = [
    "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
  ]
  can_radiouses = [
    6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
  ]
  can_heights = [
    10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
  ]
  can_costs = [
    0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
  ]
  best_store = None
  best_cost = None
  max_store_eff = -1
  max_cost_eff = -1

  #for each can in the parallel list, values are unpacked
  for i in range(len(can_names)):
    name = can_names[i]
    radious = can_radiouses[i]
    height = can_heights[i]
    cost = can_costs[i]

    # Call the compute_storage_efficiency and
    # compute_cost_efficiency functions.
    store_eff = compute_storage_efficiency(radius, height)
    cost_eff  = compute_cost_efficiency(radius, height, cost)

    # Print the can size name, storage
    # efficiency, and cost efficiency.
    print(f"{name} {store_eff:.2f} {cost_eff:.0f}")

    # If the storage efficiency of the current can size is
    # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
    if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

    # If the cost efficiency of the current can size is
    # greater than the maximum cost efficiency, then save
    # the current can size name and its cost efficiency.
    if cost_eff > max_cost_eff:
        best_cost = name
        max_cost_eff = cost_eff

# Print the best storage and cost efficiencies.
print()
print("Best can size in storage efficiency:", best_store)
print("Best can size in cost efficiency:", best_cost)


main()