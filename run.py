# Search methods
import unittest
import search


class TestSearch(unittest.TestCase):
    def test_search_AtoB_bfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test A -> B Amplitud")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('A', 'B'
                               , search.romania)
        self.assertEqual(str(search.breadth_first_graph_search(ab).path()), "[<Node B>, <Node F>, <Node S>, <Node A>]")

    def test_search_AtoB_dfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test A -> B Profundidad")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('A', 'B'
                               , search.romania)
        self.assertEqual(str(search.depth_first_graph_search(ab).path()),
                         "[<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]")

    def test_search_OtoE_bfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test O -> E Amplitud")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('O', 'E'
                               , search.romania)
        self.assertEqual(str(search.breadth_first_graph_search(ab).path()),
                         "[<Node E>, <Node H>, <Node U>, <Node B>, <Node F>, <Node S>, <Node O>]")

    def test_search_OtoE_dfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test O -> E Profundidad")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('O', 'E'
                               , search.romania)
        self.assertEqual(str(search.depth_first_graph_search(ab).path()),
                         "[<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]")

    def test_search_GtoZ_bfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test G -> Z Amplitud")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('G', 'Z'
                               , search.romania)
        self.assertEqual(str(search.breadth_first_graph_search(ab).path()), "[<Node Z>, <Node A>, <Node S>,"
                                                                            " <Node F>, <Node B>, <Node G>]")

    def test_search_GtoZ_dfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test G -> Z Profundidad")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('G', 'Z'
                               , search.romania)
        self.assertEqual(str(search.depth_first_graph_search(ab).path()),
                         "[<Node Z>, <Node A>, <Node T>, <Node L>, <Node M>, <Node D>, "
                         "<Node C>, <Node P>, <Node R>, <Node S>, <Node F>, <Node B>, <Node G>]")

    def test_search_NtoD_bfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test N -> D Amplitud")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('N', 'D'
                               , search.romania)
        self.assertEqual(str(search.breadth_first_graph_search(ab).path()), "[<Node D>, <Node C>, <Node P>, "
                                                                            "<Node B>, <Node U>, <Node V>, <Node I>, "
                                                                            "<Node N>]")

    def test_search_NtoD_dfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test N -> D Profundidad")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('N', 'D'
                               , search.romania)
        self.assertEqual(str(search.depth_first_graph_search(ab).path()),
                         "[<Node D>, <Node C>, <Node P>, <Node R>, <Node S>, <Node F>, "
                         "<Node B>, <Node U>, <Node V>, <Node I>, <Node N>]")

    def test_search_MtoF_bfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test M -> F Amplitud")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('M', 'F'
                               , search.romania)
        self.assertEqual(str(search.breadth_first_graph_search(ab).path()), "[<Node F>, <Node S>, <Node R>, "
                                                                            "<Node C>, <Node D>, <Node M>]")

    def test_search_MtoF_dfs(self):
        print("------------------------------------------------------------------------------------------------------")
        print("test M -> F Profundidad")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('M', 'F'
                               , search.romania)
        self.assertEqual(str(search.depth_first_graph_search(ab).path()),
                         "[<Node F>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node T>, <Node L>, <Node M>]")

    def test_bnb_AB(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound: A -> B")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('A', 'B'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_search(ab).path()),
                         "[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]")

    def test_bnb_OE(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound: O -> E")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('O', 'E'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_search(ab).path()),
                         "[<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]")

    def test_bnb_GZ(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound: G -> Z")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('G', 'Z'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_search(ab).path()),
                         "[<Node Z>, <Node A>, <Node S>, <Node R>, <Node P>, <Node B>, <Node G>]")

    def test_bnb_ND(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound: N -> D")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('N', 'D'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_search(ab).path()),
                         "[<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]")

    def test_bnb_MF(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound: M -> F")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('M', 'F'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_search(ab).path()),
                         "[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]")

    def test_bnb_heuristicAB(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound + Heuristica: A -> B")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('A', 'B'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_heuristic_search(ab).path()),
                         "[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]")

    def test_bnb_heuristicOE(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound + Heuristica: O -> E")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('O', 'E'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_heuristic_search(ab).path()),
                         "[<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]")

    def test_bnb_heuristicGZ(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound + Heuristica: G -> Z")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('G', 'Z'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_heuristic_search(ab).path()),
                         "[<Node Z>, <Node A>, <Node S>, <Node R>, <Node P>, <Node B>, <Node G>]")

    def test_bnb_heuristicND(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound + Heuristica: N -> D")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('N', 'D'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_heuristic_search(ab).path()),
                         "[<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]")


    def test_bnb_heuristicMF(self):
        print("------------------------------------------------------------------------------------------------------")
        print("Branch and Bound + Heuristica: M -> F")
        print("------------------------------------------------------------------------------------------------------")
        ab = search.GPSProblem('M', 'F'
                               , search.romania)
        self.assertEqual(str(search.branch_and_bound_heuristic_search(ab).path()),
                         "[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
