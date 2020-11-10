from collections import deque


class Item:
    '''
    Representation of items in PriorityQueue.
    For use internally in PriorityQueue class only.
    '''

    def __init__(self, label, key):
        self.label, self.key = label, key


class PriorityQueue:
    '''
    Heap-based priority queue implementation.
    '''

    def __init__(self):
        self.A = []
        self.label2idx = {}

    def min_heapify_up(self, c):
        '''
        Maintains the min-heap property by swapping the item at the given index upwards.
        (You SHOULD NOT call this function. It is used internally for maintaining the heap)
        '''
        if c == 0: return
        p = (c - 1) // 2
        if self.A[p].key > self.A[c].key:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_up(p)

    def min_heapify_down(self, p):
        '''
        Maintains the min-heap property by swapping the iteam at the given index downwards.
        (You SHOULD NOT call this function. It is used internally for maintaining the heap)
        '''
        if p >= len(self.A): return
        l = 2 * p + 1
        r = 2 * p + 2
        if l >= len(self.A): l = p
        if r >= len(self.A): r = p
        c = l if self.A[r].key > self.A[l].key else r
        if self.A[p].key > self.A[c].key:
            self.A[c], self.A[p] = self.A[p], self.A[c]
            self.label2idx[self.A[c].label] = c
            self.label2idx[self.A[p].label] = p
            self.min_heapify_down(c)

    def size(self):
        '''
        Retrieves the number of elements in the priority queue
        Args:
            None
        Returns:
            Size of the priority queue
        '''
        return len(self.A)

    def insert(self, label, key):
        '''
        Inserts a new element into the priority queue
        Args:
            label: Identifying nformation to be stored along with the priority
            key: Priority of the element being inserted
        Returns:
            None
        '''
        self.A.append(Item(label, key))
        idx = len(self.A) - 1
        self.label2idx[self.A[idx].label] = idx
        self.min_heapify_up(idx)

    def extract_min(self):
        '''
        Removes and returns the minimum-priority element in the priority queue
        Args:
            None
        Returns:
            The identifier for the element removed.
        '''
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.label2idx[self.A[0].label] = 0
        del self.label2idx[self.A[-1].label]
        min_label = self.A.pop().label
        self.min_heapify_down(0)
        return min_label

    def decrease_key(self, label, key):
        '''
        Decreases the priority of a given item in the queue
        Args:
            label: Identifying information stored along with priority
            key: New priority of the item with the specified label
        Returns:
            None
        '''
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.A[idx].key:
                self.A[idx].key = key
                self.min_heapify_up(idx)


'''
###################################################
### PLEASE DO NOT MODIFY ANY OF THE CODE ABOVE! ###
### This code is included for your convenience, ###
### but modifications may cause you a headache! ###
###################################################
'''


def bidi(adj, s, t):
    '''
    Implement bidirectional dijkstra.
    Args:
        adj: Routers are identified by unique integer id's. adj[u][v] is the latency between router u and router v.
        For a router, u, with no neighbor adj[u] = {}.
        s: Starting router id.
        t: Destination router id.
    Returns:
        The minimum weighted distance from s to t. If there is no path from s to t, return None.
    Note: Bidirectional dijkstra cuts down the number of nodes you visit. Only insert nodes into your priority queue (and whatever other data structures you may be maintaining)
    when you actually discover them through relaxation.
    '''
    # init aux structures
    rev_adj = reverse_adj(adj)
    forwards_seen, backwards_seen, popped_off_Q = set(), set(), set()
    forwards_dist, backwards_dist = {s:0}, {t:0}
    # forwards_dist.update({u: float('inf') for u in adj})
    # backwards_dist.update({u: float('inf') for u in rev_adj})
    # forwards_dist[s] = 0
    # forwards_dist[t] = 0

    # init queue
    forwards_Q = PriorityQueue()
    backwards_Q = PriorityQueue()

    # insert start node into Q
    forwards_Q.insert(s, 0)
    backwards_Q.insert(t, 0)

    double_break = False
    while forwards_Q.size() > 0 or backwards_Q.size() > 0:
        # search forwards and backwards
        double_break = directional_search(forwards_Q, adj, forwards_dist, forwards_seen, backwards_seen, popped_off_Q, double_break)
        double_break = directional_search(backwards_Q, rev_adj, backwards_dist, backwards_seen, forwards_seen, popped_off_Q, double_break)

        # terminating condition was reached: we've seen a node that has been popped before
        if double_break:
            break

    # find distance of shortest path
    min_distance = float("inf")
    for node in forwards_dist:
        # Check to make sure the node has been visited in the backward direction.
        # Otherwise it will not appear in the distances dictionary.
        if node in backwards_dist:
            min_distance = min(min_distance, forwards_dist[node] + backwards_dist[node])

    if min_distance == float("inf"):
        return None
    return min_distance




def directional_search(Q, adj, dist, seen, other_seen, popped_off_Q, double_break):
    '''conducts dijkstra search forwards or backwards depending on params'''
    if Q.size() <= 0:
        return double_break

    # extract u from Q
    u = Q.extract_min()
    # if u in popped_off_Q:
    #     double_break = True

    # search neighbors of u and try to relax them
    for v in adj[u]:
        new_guy = v not in dist
        try_to_relax(adj, dist, u, v)
        if new_guy:
            Q.insert(v, dist[v]) # add neighbor to Q
        else:
            Q.decrease_key(v, dist[v])

    if u in other_seen:
        return True
    seen.add(u)

    return double_break





def try_to_relax(adj, d, u, v):
    '''relaxes edge given u, v, and some aux data'''
    # try:
    if v not in d:
        d[v] = float('inf')
    if u not in d:
        d[u] = float('inf')

    if d[u] + adj[u][v] < d[v]: # relax edge
        d[v] = d[u] + adj[u][v]


    # add to priority queue

def reverse_adj(adj):
    '''helper func to reverse adj'''
    # rev_adj = {v:{} for _, v_dict in adj.items() for v in v_dict}
    rev_adj = {u:{} for u in adj}
    for u, v_dict in adj.items():
        for v, weight in v_dict.items():
            rev_adj[v][u] = weight
    return rev_adj


if __name__ == '__main__':
    adj = {0: {1: 3, 5: 5}, 1: {3: 3}, 3: {4: 3}, 4: {}, 5: {4: 5}}
    print(reverse_adj(adj))