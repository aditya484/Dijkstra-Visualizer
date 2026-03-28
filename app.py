import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from dijkstra import dijkstra
from utils import parse_input

st.set_page_config(page_title="Dijkstra Visualizer", layout="centered")

st.title("🚀 Dijkstra Algorithm Visualizer")

nodes = st.text_input("Enter nodes (comma separated)", "A,B,C,D,E")
edges = st.text_area(
    "Enter edges (format: node1,node2,weight)",
    "A,B,1\nA,C,4\nB,C,2\nB,D,5\nC,D,1\nD,E,3"
)

start_node = st.text_input("Enter start node", "A")

if st.button("Visualize"):
    graph, G = parse_input(nodes, edges)

    distances = dijkstra(graph, start_node)

    st.subheader("📊 Shortest Distances")
    st.write(distances)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    st.pyplot(plt)