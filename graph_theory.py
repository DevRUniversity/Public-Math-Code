import matplotlib.pyplot as plt
import networkx as nx
import random
import math
import time
import numpy as np
import copy

ANIMATION_DELAY = 2
COUNTER_LIMIT = 3

G = nx.Graph()  # create graph object

# define list of nodes (node IDs)
nodes = [1, 2, 3]
global Max_Node
Max_Node = 4

# define list of edges
# list of tuples, each tuple represents an edge
# tuple (id_1, id_2) means that id_1 and id_2 nodes are connected with an edge
edges = [(1, 2), (2,3), (3,1)]

# add information to the graph object
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# draw a graph and show the plot


def graph_draw(G, Counter):
    #https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_kamada_kawai.html
    #this one looks the best so I went with it
    #various layouts can be utilized here
    RatioOfProgression = float(Counter / COUNTER_LIMIT)
    nx.draw(G,  pos=nx.kamada_kawai_layout(G), node_size=5)
    

def update_graph(Counter):
    
    CopyOfEdges =  copy.deepcopy(G.edges)
    for edge in CopyOfEdges: #not doing this copying trick causes dictionary to change size during the iteration
        global Max_Node
        Max_Node = Max_Node + 1
        
        p1 = edge[0]
        p2 = edge[1]

        new_nodes   = [Max_Node, Max_Node+1, Max_Node+2]
        new_edges   = [(p1, Max_Node), (p2, Max_Node), (Max_Node+1, Max_Node), (Max_Node+2, Max_Node)]
        purge_edges = [edge]
        G.add_nodes_from(new_nodes)
        G.add_edges_from(new_edges)
        G.remove_edges_from(purge_edges)
        Max_Node = Max_Node + 2

    #Calls function to initiate the drawing of the graph
    graph_draw(G, Counter)

def Print_Custom_Graph_Data(GraphG):
    print("Current Iteration: " + str(Counter) + " Nodes: " + str(Max_Node) + " Edges: " +str(len(G.edges)) )


def animate_and_update(Counter):
    # Mention x and y limits to define their range
    plt.clf() #clears previous graph
    update_graph(Counter) #where we will put all of the code to update a graph as it changes
    plt.plot() #not entirely sure how plt knows to plot the nx graph, but it does I guess so whatever
    plt.pause(ANIMATION_DELAY)

print("Type \'Y\' to initiate the program:")
firstPass = True
Counter = 0


graph_draw(G, Counter)
while(Counter <= COUNTER_LIMIT):
    if(firstPass):
        while (input() != "Y"):
            pass #Waiting for User to Indicate to initiate program
        firstPass = False # No longer the first tick

        Print_Custom_Graph_Data(G)
        Counter = Counter + 1
        #just to capture initial state
        plt.plot()
        plt.pause(ANIMATION_DELAY)
    animate_and_update(Counter)
    Print_Custom_Graph_Data(G)
    Counter = Counter + 1
print("Finished Computations")
plt.show() #Must be at the end of the program
