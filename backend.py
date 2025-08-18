from punemap import build_graph, get_nearest_node, bfs_path, dijkstra_path, astar_path
import time

def compute_routes(place_name, source, destination):
    # Build graph
    G = build_graph(place_name)

    # Find nearest nodes
    source_node = get_nearest_node(G, source)
    dest_node = get_nearest_node(G, destination)

    results = {}

    # BFS
    start = time.time()
    path_bfs = bfs_path(G, source_node, dest_node)
    results['BFS'] = {
        "path": path_bfs,
        "time": time.time() - start,
        "length": sum(ox.utils_graph.get_route_edge_attributes(G, path_bfs, "length"))
    }

    # Dijkstra
    start = time.time()
    path_dijkstra = dijkstra_path(G, source_node, dest_node)
    results['Dijkstra'] = {
        "path": path_dijkstra,
        "time": time.time() - start,
        "length": sum(ox.utils_graph.get_route_edge_attributes(G, path_dijkstra, "length"))
    }

    # A*
    start = time.time()
    path_astar = astar_path(G, source_node, dest_node)
    results['A*'] = {
        "path": path_astar,
        "time": time.time() - start,
        "length": sum(ox.utils_graph.get_route_edge_attributes(G, path_astar, "length"))
    }

    return results, G
