from neo4j import *

# driver = GraphDatabase.driver("bolt://localhost:11001", auth=("neo4j", "root"))
 
# theme1 -> theme2
# theme1 -> [1,2] | 1 -> [4,5] | 2 -> [6,7]
# theme2 -> [3] | 3 -> [8,9]

class Graph:
  def __init__(self,adress,user,password):
    self.driver = GraphDatabase.driver("adress", auth=("neo4j", "root"))
  
  def updateGraph():
    # Take care of small part of tree

