from random import shuffle
import sys
sys.path.insert(0, '../graph')
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """

        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(f"User{user}")


        # Create friendships
        user_friendships = (num_users * avg_friendships) // 2
        possible_friendships = []
        for user1 in range(1, num_users):
            # print("------------")
            # print(user1)
            # print("num_users", num_users)
            for possible_friend in range(user1 + 1, num_users +1):

                # print(possible_friend)
                possible_friendships.append((user1, possible_friend))
                # print(possible_friendships)
                # print("------------")
        shuffle(possible_friendships)

        for user in range(0, user_friendships):
            # print("user_friendships", possible_friendships)

            # print("possible_friend",possible_friendships[user][0], possible_friendships[user][1])
            self.add_friendship(possible_friendships[user][0], possible_friendships[user][1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        if user_id not in self.friendships:
            return visited
        # !!!! IMPLEMENT ME
        #Implementing a breath first since we are looking for shortest path
        # Create a queue
        queue = Queue()
        # Put the starting point in that
        queue.enqueue([user_id])

        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #    dequeue the first path
            path = queue.dequeue()
            v = path[-1]
        #    If not visited
            if v not in visited:
        #       DO THE THING!
        #       Add to visited
                visited[v] = path
                for friend in self.friendships[v]:
                    path_copy = list(path)
                    path_copy.append(friend)
                    queue.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
