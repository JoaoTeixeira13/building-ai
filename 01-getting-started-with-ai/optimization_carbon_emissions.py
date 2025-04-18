port_names = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# Distance matrix: D[i][j] = distance from port i to port j (in km)
distance_matrix = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

# CO₂ emissions: 0.020 kg per km per ton of goods
emission_per_km = 0.020


def calculate_total_emissions(route):
    emissions = 0
    for i in range(len(route) - 1):
        from_port = route[i]
        to_port = route[i + 1]
        emissions += distance_matrix[from_port][to_port] * emission_per_km
    return emissions


def find_best_route(current_route, remaining_ports, best_so_far):
    lowest_emissions, best_route = best_so_far

    if not remaining_ports:
        total_emissions = calculate_total_emissions(current_route)
        if total_emissions < lowest_emissions:
            return total_emissions, current_route[:]  # found a better route!
        return best_so_far

    for i, next_port in enumerate(remaining_ports):
        new_route = current_route + [next_port]
        next_remaining = remaining_ports[:i] + remaining_ports[i + 1:]
        best_so_far = find_best_route(new_route, next_remaining, best_so_far)

    return best_so_far


def main():
    start_route = [0]  # Start from "PAN"
    remaining_ports = list(range(1, len(port_names)))
    initial_best = (float('inf'), [])

    lowest_emissions, best_route = find_best_route(start_route, remaining_ports, initial_best)

    readable_route = ' → '.join([port_names[i] for i in best_route])
    print(f"Best Route: {readable_route}")
    print(f"Total CO₂ Emissions: {lowest_emissions:.1f} kg")


main()