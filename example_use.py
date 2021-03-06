'''
Timothy Davison
5/6/2018
Instructions/Example use of the SC+SSTL package.
'''

import osmnx as ox
import sc_methods
import sstl_methods
import sc_plot
import random


G = ox.graph_from_point((40.758896, -73.985130), distance=500)
ox.plot.plot_graph(G)


graph = sc_methods.graph_from_OSMnx(G)
sc_plot.sc_plot_directed(graph)
for node in graph.nodes:
    satisf = random.randint(0,2)
    if satisf == 0:
        node.tf_satisfied = False
sc_plot.sc_plot_directed(graph)


file = "NYC_Traffic_Sample"
sc_methods.load_nyc_data(graph, file)


sample_node = graph.a_node()
print(sample_node.data)


sample_bfs = graph.bfs_set(sample_node, 1, 4)
sample_distance = sc_methods.nodes_from_point(graph, sample_node, 50)
polygon_set = {(40.758896, -73.985130), (40.658896, -73.885130), (40.858896, -73.985130)}
sample_polygon = graph.nodes_in_polygon(polygon_set)


tf = sstl_methods.tf_everywhere(graph.dataframe, '6:00-7:00AM', '<=', 300)
robust = sstl_methods.robust_everywhere(graph.dataframe, '6:00-7:00AM', '<=', 300)
percent = sstl_methods.percent_everywhere(graph.dataframe, '6:00-7:00AM', '<=', 300)
integral = sstl_methods.sstl_integral_timeset(graph, ['6:00-7:00AM', '7:00-8:00AM'], '<=', 600)




