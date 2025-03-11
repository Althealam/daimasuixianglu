def bfs(graph, start, end):
    queue=[]
    queue.append([start])
    visited.add(start)

    while queue:
        # current node processing
        node=queue.pop()
        visited.add(node)

        # generate other nodes
        process(node)
        nodes=generate_related_nodes(node)

        # check visited, push node->queue
        queue.push(nodes)
