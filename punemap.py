import osmnx as ox
import networkx as nx

def build_graph(place_name):
    """
    Build a graph for the given place name using OSM data.
    """
    print(f"Downloading graph for: {place_name}")
    G = ox.graph_from_place(place_name, network_type="drive")
    G = ox.add_edge_lengths(G)
    return G


def get_nearest_node(G, location):
    """
    Get nearest graph node for a given (lat, lon) tuple.
    """
    return ox.distance.nearest_nodes(G, location[1], location[0])  # (lon, lat) order


def bfs_path(G, source, target):
    return nx.shortest_path(G, source=source, target=target, method='bfs')


def dijkstra_path(G, source, target):
    return nx.shortest_path(G, source=source, target=target, weight="length", method="dijkstra")


def astar_path(G, source, target):
    return nx.astar_path(G, source=source, target=target, weight="length")
