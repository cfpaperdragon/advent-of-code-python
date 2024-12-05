from aoc.year2024.graph import DirectedGraph as Graph


def test_graph():
    graph = Graph()
    graph.add_path(47, 53)
    graph.add_path(97, 13)
    graph.add_path(97, 61)
    graph.add_path(97, 47)
    graph.add_path(75, 29)
    graph.add_path(61, 13)
    graph.print()
    assert True

