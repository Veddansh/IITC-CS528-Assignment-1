import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#first graph
g1 = nx.Graph()
n1 = g1.add_node(10)
n2 = g1.add_node(26)
n3 = g1.add_node(15)
n4 = g1.add_node(33)
n5 = g1.add_node(18)
n6 = g1.add_node(22)


e1 = g1.add_edge(6,9)

g1_degrees = dict(g1.degree)

print("Degrees of G1 are : ",g1_degrees)

nx.draw( nx.gnm_random_graph(6,9,seed=None,directed=False) )

graph_name = "Graph 1"
plt.title(graph_name)
plt.show()



#second graph
g2 = nx.Graph()
n1 = g2.add_node(10)
n2 = g2.add_node(26)
n3 = g2.add_node(15)
n4 = g2.add_node(33)
n5 = g2.add_node(18)
n6 = g2.add_node(22)
n7 = g2.add_node(52)
n8 = g2.add_node(42)
n9 = g2.add_node(35)
n10 = g2.add_node(48)


e1 = g2.add_edge(10,15)

g2_degrees = dict(g2.degree)

print("Degrees of G2 are : ",g2_degrees)

nx.draw( nx.gnm_random_graph(10,15,seed=None,directed=False) )

graph_name = "Graph 2"
plt.title(graph_name)
plt.show()



#third graph
g3 = nx.Graph()
n1 = g3.add_node(10)
n2 = g3.add_node(26)
n3 = g3.add_node(15)
n4 = g3.add_node(33)
n5 = g3.add_node(18)
n6 = g3.add_node(22)
n7 = g3.add_node(52)
n8 = g3.add_node(42)
n9 = g3.add_node(35)
n10 = g3.add_node(48)
n11 = g3.add_node(60)
n12 = g3.add_node(70)
n13 = g3.add_node(80)
n14 = g3.add_node(65)
n15 = g3.add_node(75)
n16 = g3.add_node(85)
n17 = g3.add_node(1)
n18 = g3.add_node(2)
n19 = g3.add_node(3)
n20 = g3.add_node(50)


e1 = g3.add_edge(20,30)

g3_degrees = dict(g3.degree)

print("Degrees of G3 are : ",g3_degrees)

nx.draw( nx.gnm_random_graph(20,30,seed=None,directed=False) )

graph_name = "Graph 3"
plt.title(graph_name)
plt.show()

#sort_g1 = (sorted(g1_degrees), reverse = True)
#sort_g2 = (sorted(g2_degrees), reverse = True)
#sort_g3 = (sorted(g3_degrees), reverse = True)

#print (sort_g1)
#print (sort_g2)
#print (sort_g3)


all_dicts = [(k, v1, v2, v3) for k, v1 in g1_degrees.items() for _, v2 in g2_degrees.items() for _, v3 in g3_degrees.items() if k in g2_degrees and k in g3_degrees]

# Sort the list of tuples in descending order
sorted_dicts = sorted(all_dicts, key=lambda x: (x[1], x[2], x[3]), reverse=True)

# Create dictionaries from the sorted tuples
g1_degrees_sorted = {key: value for key, value in g1_degrees.items() if key in [x[0] for x in sorted_dicts]}
g2_degrees_sorted = {key: value for key, value in g2_degrees.items() if key in [x[0] for x in sorted_dicts]}
g3_degrees_sorted = {key: value for key, value in g3_degrees.items() if key in [x[0] for x in sorted_dicts]}

# Print the sorted dictionaries
print("g1_degrees sorted:", g1_degrees_sorted)
print("g2_degrees sorted:", g2_degrees_sorted)
print("g3_degrees sorted:", g3_degrees_sorted)




def k_anonymous_sequence(n, k):
    degree_sequence = [3, 2, 2, 1, 1, 1]
    min_cost = float("inf")
    for i in range(n):
        for j in range(i, n):
            if sum(degree_sequence[i:j+1]) >= k:
                cost = j-i+1-sum(degree_sequence[i:j+1])
                if cost < min_cost:
                    min_cost = cost
                    start = i
                    end = j
    for i in range(start, end+1):
        degree_sequence[i] = k
    return degree_sequence

# n = 6 , k = 2
print("K - Anonymous degree sequence for n = 6 and k = 2 : ", k_anonymous_sequence(6, 2))

# n = 6 , k = 3
print("K - Anonymous degree sequence for n = 6 and k = 3 : ",k_anonymous_sequence(6, 3))


# n = 10 , k = 3
print("K - Anonymous degree sequence for n = 10 and k = 3 : ", k_anonymous_sequence(10, 3))

# n = 10 , k = 4
print("K - Anonymous degree sequence for n = 10 and k = 4 : ",k_anonymous_sequence(10, 4))


# n = 20 , k = 3
print("K - Anonymous degree sequence for n = 20 and k = 3 : ", k_anonymous_sequence(20, 3))

# n = 20 , k = 4
print("K - Anonymous degree sequence for n = 20 and k = 4 : ",k_anonymous_sequence(20, 4))















































#graph_name = "Graph 2"
#plt.title(graph_name)
#plt.show()





