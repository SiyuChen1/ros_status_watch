from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import pygraphviz as pgv
from .pydotfactory import PydotFactory
import pydot

def from_graph_generate_dot():
    '''
    first from .json data generate graph
    we define topic and node are Nodes of Graph and the difference is shape
    @for shape: box stands for topics,ellipse for nodes
    @for color: red stands for error,black stands for normal
    @for line style: dashed and solid,black solid stands for normal connection between topic and node,red dashed line means error
    TODO:
    1. define function to read .json data 
    2. create a graph
    '''

    # we use PydotFactory to create graph,subgraph,node and edge
    f = PydotFactory()

    # we create a graph
    graph = f.get_graph()
    
    # we create a subgraph
    module_1 = f.add_subgraph_to_graph(graph,'module 1')
    module_2 = f.add_subgraph_to_graph(graph,'module 2')
    module_3 = f.add_subgraph_to_graph(graph,'module 3')
    
    # we add node to graph
    f.add_node_to_graph(module_1,'node_1',nodelabel='node_1',shape='ellipse')
    f.add_node_to_graph(module_1,'node 2',nodelabel='node 2',shape='ellipse')
    f.add_node_to_graph(module_2,'node 3',nodelabel='node 3',shape='ellipse',color='red')
    f.add_node_to_graph(module_2,'node 4',nodelabel='node 4',shape='ellipse',color='red')
    f.add_node_to_graph(module_3,'node 5',nodelabel='node 5',shape='ellipse',color='red')
    f.add_node_to_graph(graph,'topic 1',nodelabel='topic 1',shape='box')
    f.add_node_to_graph(graph,'topic 2',nodelabel='topic 2',shape='box')
    f.add_node_to_graph(graph,'topic 3',nodelabel='topic 3',shape='box')
    f.add_node_to_graph(graph,'topic 4',nodelabel='topic 4',shape='box')
    f.add_node_to_graph(graph,'topic 5',nodelabel='topic 5',shape='box')
    
    # we add edge to graph
    f.add_edge_to_graph(graph,'node_1','topic 1',label='10 Hz',style='dashed')
    f.add_edge_to_graph(graph,'node 2','topic 2')
    f.add_edge_to_graph(graph,'node 3','topic 3')
    f.add_edge_to_graph(graph,'node 4','topic 3')
    f.add_edge_to_graph(graph,'node 4','topic 4')
    f.add_edge_to_graph(graph,'node 5','topic 5')
    f.add_edge_to_graph(graph,'topic 1','node 3')
    f.add_edge_to_graph(graph,'topic 1','node 4')
    f.add_edge_to_graph(graph,'topic 2','node 3')
    f.add_edge_to_graph(graph,'topic 2','node 4')
    f.add_edge_to_graph(graph,'topic 3','node 5')
    f.add_edge_to_graph(graph,'topic 4','node 5')

    # we generate .dot 
    s = str(f.create_dot(graph))
    
    # we convert graph to format pygraphviz graph
    A = pgv.AGraph(s)

    '''
    @ test function of pgv.AGraph()
    print(A.number_of_edges())
    print(A.number_of_nodes())
    print(A.get_node('node_1'))
    if A.has_node('node_1'):
        print("enter")
    else:
        print("false")
    '''
    return s
   