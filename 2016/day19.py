class Node:
    def __init__(self, v):
        self.v = v

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

n = 3004953

nodes = {}
for i in range(n):
    nodes[i] = Node(i+1)

    if i > 0:
        nodes[i].prev = nodes[i-1]
        nodes[i-1].next = nodes[i]

nodes[0].prev = nodes[n-1]
nodes[n-1].next = nodes[0]

# part 1
# curr = nodes[1]
# while curr.v != curr.next.v:
#     prev = curr
#     curr = curr.next.next
#     prev.delete()

# print(curr.v)

# part 2
curr = nodes[0]
mid = nodes[int(n/2)]

for i in range(n-1):
    mid.delete()
    mid = mid.next
    if (n-i)%2==1: mid = mid.next
    curr = curr.next

print(curr.v)