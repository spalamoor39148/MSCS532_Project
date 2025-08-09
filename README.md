# MSCS532_Project
# Social Network Graph Proof of Concept

## Project Overview
This project implements a foundational social network graph using Python. It models users and their connections with an adjacency list data structure, supporting core operations essential for social network analysis such as adding users, creating connections, performing breadth-first search (BFS) traversal, and ranking users by influence.

The implementation serves as a proof of concept (PoC) for building scalable social network analytics tools.

---

## Features
- **Dynamic user management:** Add users to the network on demand.
- **Bidirectional connections:** Establish mutual links between users.
- **Neighbor retrieval:** Efficiently access immediate connections of any user.
- **Graph traversal:** Perform BFS to explore network connectivity.
- **Influence ranking:** Retrieve the top-k users by influence score using a priority queue.

---

## Getting Started

### Prerequisites
- Python 3.6 or later (uses only standard libraries)

### Running the Code
Clone the repository and run the main script to execute built-in tests demonstrating core functionality:

```bash
python Social_network_graph.py
```

You should see output showing neighbor sets, BFS traversal order, and top influential users.

---

## Example Output

```
Creating social network graph...
Neighbors of userA: {'userB', 'userC'}
Neighbors of userE: set()

Performing BFS traversal from userA:
Visited: userA
Visited: userB
Visited: userC
Visited: userD

Top 3 influential users:
userC: 20
userA: 15
userB: 10
```

---

## Project Structure

```
social-network/
├── Social_network_graph.py                               # Core implementation and tests
├── README.md                                             # Project overview and instructions
└── Project Phase 2 Deliverable 2.docx                    # design notes and documentation
```

---

## Next Steps and Enhancements

Future development could include:
- Implementing advanced influence metrics such as PageRank or community detection algorithms.
- Adding functionality for removing users and connections dynamically.
- Scaling the data structure for large networks using databases or distributed systems.
- Developing a user interface or API for interactive querying and visualization.

---

## References

Borgatti, S. P., & Everett, M. G. (2006). A graph-theoretic perspective on centrality. *Social Networks*, *28*(4), 466–484. https://doi.org/10.1016/j.socnet.2005.11.005

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms* (3rd ed.). MIT Press.

Leskovec, J., Rajaraman, A., & Ullman, J. D. (2020). *Mining of massive datasets* (3rd ed.). Cambridge University Press.

---

## Author

Name — Sri Sai Palamoor

