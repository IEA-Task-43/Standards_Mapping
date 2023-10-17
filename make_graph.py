import pandas as pd
import networkx as nx
import hvplot.networkx as hvnx
import holoviews as hv
from holoviews import opts

# Initialize the Bokeh rendering extension
hv.extension('bokeh')

# Load the data
norm_category_df = pd.read_csv('Norm_Category.csv', delimiter=';')
norm_keyword_df = pd.read_csv('Norm_Keyword.csv', delimiter=';')
keywords_cat_df = pd.read_csv('Keywords_Cat.csv', delimiter=';')

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges for Norm_Category
for _, row in norm_category_df.iterrows():
    G.add_node(row['Category'], type='Category')
    G.add_node(row['Norm'], type='Norm')
    G.add_edge(row['Category'], row['Norm'], relationship=row['R_Category_Norm'])

# Add nodes and edges for Norm_Keyword
for _, row in norm_keyword_df.iterrows():
    G.add_node(row['Norm'], type='Norm')
    G.add_node(row['Key Words'], type='Keyword')
    G.add_edge(row['Norm'], row['Key Words'], relationship=row['R_Norm_KW'])

# Add keyword nodes from Keywords_Cat (if they aren't already added via edges)
for _, row in keywords_cat_df.iterrows():
    G.add_node(row['Keywords'], group=row['Group'], type='Keyword')

# Create the plot using hvplot
plot = hvnx.draw(G, 
                 node_color='lightblue', 
                 edge_color='gray', 
                 node_size=200, 
                 with_labels=True)

# Customize the plot
plot.opts(opts.Graph(width=800, height=500, padding=0.1))

# Save the plot as an HTML file
hv.save(plot, 'network_graph.html')

