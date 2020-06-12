

class Node(object):

    def __init__(self, next_node=None):
        self.next_node = next_node

    @property
    def next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        return new_next


def loop_size(node):
    onestep = node
    twostep = node.next
    while(onestep != twostep):
        twostep = twostep.next.next
        onestep = onestep.next
    onestep = onestep.next
    size = 1
    while(onestep != twostep):
        size += 1
        onestep = onestep.next
    return size



# Alternative_Solution 1
def loop_size1(node):
    turtle, rabbit = node.next, node.next.next

    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count


# Alternative_Solution 2
def loop_size2(n):
    l = []
    while not n in l:
        l.append(n)
        n = n.next
    return len(l) - l.index(n)


# This below wasn't required for the solution but used to set the test up
def test_ll(tail, loop):
    print('tail ' + str(tail))
    print('loop ' + str(loop))

    head = Node()
    print('head ' + str(head))
    nodes = [head]
    print('nodes ' + str(nodes))
    for i in range(2, tail+loop+1):
        print('i ' + str(i))
        head = head.set_next(Node())
        print('head ' + str(head))
        nodes.append(head)
        print('nodes ' + str(nodes))
    print('nodes tail' + str(nodes[tail]))
    nodes[-1].set_next(nodes[tail])
    print('nodes ' + str(nodes))
    print('nodes[-1] ' + str(nodes[-1]))
    print('nodes[0] ' + str(nodes[0]))

    # *******************************
    size = loop_size2(nodes[0])    #*
    # *******************************

    print("Tail: {}, Loop: {}, Size: {}".format(tail, loop, size))

test_ll(1, 4)
# test_ll(999, 1000)
# test_ll(1000, 999)
# test_ll(50, 3)
# test_ll(3, 3)
# test_ll(3, 4)