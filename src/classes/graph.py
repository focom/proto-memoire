from neo4j import *

# driver = GraphDatabase.driver("bolt://localhost:11001", auth=("neo4j", "root"))

# theme1 -> theme2
# theme1 -> [1,2] | 1 -> [4,5] | 2 -> [6,7]
# theme2 -> [3] | 3 -> [8,9]


class Graph:
    def __init__(self, adress, user, password):
        self.driver = GraphDatabase.driver(adress, auth=(user, password))

    def get_db(self):
        return self.driver.session()

    def getScoreNode(self, id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._scoreNode, id_node)

    def _scoreNode(self, tx, id_node):
        db = self.get_db()
        query = f"MATCH (n:Chapitre) where n.id_node='{id_node}' return n"
        print(query)
        result = db.run(query)
        for record in result:
            return (record[0]._properties['grade'])

    def getHistoryNode(self, id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._historyNode, id_node)

    def _historyNode(self, id_node):
        db = self.get_db()
        query = f"MATCH (n:Chapitre) where n.id_node='{id_node}' return n"
        print(query)
        result = db.run(query)
        for record in result:
            return (record[0]._properties['history'])

    def getWeightNode(self, id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._weightNode, id_node)

    def _weightNode(self, id_node):
        db = self.get_db()
        query = f"MATCH (n:Chapitre) where n.id_node='{id_node}' return n"
        print(query)
        result = db.run(query)
        for record in result:
            return (record[0]._properties['weight'])

    def setHistory(self, id_node,history):
        with self.driver.session() as session:
            return session.read_transaction(self._historyNodeSetter, id_node,history)

    def _historyNodeSetter(self, id_node, history):
        db = self.get_db()
        query = f"MATCH (n:Chapitre) where n.id_node='{id_node}' set n.history=history"
        print(query)
        db.run(query)

    def updateGraph(self, tx):
        # Take care of small part of tree
        # select 8 and 9 and apply to 3.

        score8 = 0
        score9 = 0
        score3 = 0
        history3 = 0

        scoreSmall = [0, 0, 0]

        for record in tx.run("MATCH (n:Chapitre) return n where n.id_chap=8"):
            print(record[0]._properties['grade'])
        for record in tx.run("MATCH (n:Chapitre) return n where n.id_chap=9"):
            print(record[0]._properties['grade'])
        for record in tx.run("MATCH (n:Chapitre) return n where n.id_chap=3"):
            print(record[0]._properties['grade'])

    def runUpdateGraph(self):
        with self.driver.session() as session:
            session.read_transaction(self.updateGraph)


if (__name__ == '__main__'):
    graph = Graph('bolt://localhost:7687', 'neo4j', 'root')
    # graph.getScoreNode({'id_node':'4'})
    print(graph.getScoreNode('4'))
