from cli_helpers import Digraph

dot = Digraph()


dot.node('8', '8')     
dot.node('3', '3')
dot.node('10', '10')
dot.node('1', '1')
dot.node('6', '6')

dot.edges(["83", "8 10"]) 
dot.edges(["31", "36"])   

dot.render("Arbol_BST", view=False)
