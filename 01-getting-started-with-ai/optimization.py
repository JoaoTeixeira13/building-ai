# In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.
#
# The template code below contains an incomplete generate_routes function which takes as input a specified route and a list of port names absent from that route.
# Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).
#
# The mathematical term for such orderings is a permutation.
# Note that your program should work for an input portnames list of any length. The order in which the permutations are printed doesn't matter.
#
# As the output the function should print each permutation on its own row, as one string, with the port names separated by spaces.
#
# Output Example
# PAN AMS CAS NYC HEL
#
# ...
#
# PAN CAS AMS NYC HEL
# Tip: Your values might be different, but the formatting should be identical.

port_names = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def generate_routes(current_route, remaining_ports):
    if not remaining_ports:
        route_names = [port_names[index] for index in current_route]
        print(' '.join(route_names))
        return

    for index, next_port in enumerate(remaining_ports):
        updated_route = current_route + [next_port]
        ports_left = remaining_ports[:index] + remaining_ports[index + 1:]
        generate_routes(updated_route, ports_left)

start_port = [0]
other_ports = list(range(1, len(port_names)))

generate_routes(start_port, other_ports)