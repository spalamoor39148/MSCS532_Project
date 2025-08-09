from collections import deque
import heapq

class SocialNetworkGraph:
    def __init__(self):
        # Adjacency list: user_id -> set of connected user_ids
        self.graph = {}

    def add_user(self, user_id):
        """Add a user if not already present."""
        if user_id not in self.graph:
            self.graph[user_id] = set()

    def add_connection(self, user1, user2):
        """
        Add a bidirectional connection (undirected edge)
        between user1 and user2.
        """
        self.add_user(user1)
        self.add_user(user2)
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def get_neighbors(self, user_id):
        """Return the set of neighbors for the given user_id."""
        return self.graph.get(user_id, set())

def bfs_traversal(network_graph, start_user):
    """
    Perform a breadth-first search traversal starting from start_user.
    Prints users in the order visited.
    """
    visited = set()
    queue = deque([start_user])
    visited.add(start_user)

    while queue:
        current_user = queue.popleft()
        print(f"Visited: {current_user}")

        for neighbor in network_graph.get_neighbors(current_user):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def top_k_influential(users_influence, k):
    """
    Return a list of top-k users with highest influence scores.
    users_influence: dict mapping user_id -> influence_score
    """
    heap = []
    for user, score in users_influence.items():
        # Use negative score to simulate max heap with heapq (min heap)
        heapq.heappush(heap, (-score, user))

    top_users = []
    for _ in range(min(k, len(heap))):
        neg_score, user = heapq.heappop(heap)
        top_users.append((user, -neg_score))

    return top_users

# Test and demonstration function
def run_tests():
    print("Creating social network graph...")
    network = SocialNetworkGraph()
    network.add_connection('userA', 'userB')
    network.add_connection('userA', 'userC')
    network.add_connection('userB', 'userD')
    network.add_user('userE')  # userE with no connections

    neighbors_A = network.get_neighbors('userA')
    print(f"Neighbors of userA: {neighbors_A}")  # Should be {'userB', 'userC'}

    neighbors_E = network.get_neighbors('userE')
    print(f"Neighbors of userE: {neighbors_E}")  # Should be empty set

    print("\nPerforming BFS traversal from userA:")
    bfs_traversal(network, 'userA')

    influence_scores = {'userA': 15, 'userB': 10, 'userC': 20, 'userD': 5, 'userE': 8 }

    print("\nTop 3 influential users:")
    top_users = top_k_influential(influence_scores, 3)
    for user, score in top_users:
        print(f"{user}: {score}")

if __name__ == "__main__":
    run_tests()
