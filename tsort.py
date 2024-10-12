from dataclasses import dataclass
from typing import List

import stack_array
from stack_array import *

@dataclass
class Vertex:
    adjacencies: List

    def __post_init__(self) -> None:
        self.in_degree: int = 0     # the number of edges into vertex

def tsort(vertices: List) -> str:
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if not vertices:
        raise ValueError("input contains no edges")
    if (len(vertices) % 2) != 0:
        raise ValueError("input contains an odd number of tokens")

    vert_dict = {}

    encountered = []

    ret_str = ""

    stk = stack_array.Stack(len(vertices))

    for i in range(0, len(vertices), 2):                                                                                #creates dictionary with each vertex, its adjacency list and its in degree

        if vertices[i] not in encountered:
            encountered.append(vertices[i])
            vert_dict[vertices[i]] = Vertex([vertices[i + 1]])

        elif vertices[i] in encountered:
            vert_dict[vertices[i]].adjacencies.append(vertices[i + 1])


        if vertices[i + 1] not in encountered:
            encountered.append(vertices[i + 1])
            vert_dict[vertices[i + 1]] = Vertex([])
            vert_dict[vertices[i + 1]].in_degree = 1

        elif vertices[i + 1] in encountered:
            vert_dict[vertices[i + 1]].in_degree += 1



    for i in encountered:
        if vert_dict[i].in_degree == 0:
            stk.push(i)

    while not stk.is_empty():
        peeked = stk.peek()
        ret_str += "{}\n".format(peeked)
        stk.pop()
        for i in vert_dict[peeked].adjacencies:
            vert_dict[i].in_degree -= 1
            if vert_dict[i].in_degree == 0:
                stk.push(i)

    #str_as_list = "\n".split(ret_str)
    str_as_list = ret_str.split("\n")

    if len(encountered) > len(str_as_list):
        raise ValueError("input contains a cycle")



    return ret_str











