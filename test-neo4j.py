from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:11001", auth=("neo4j", "root"))


def print_friends(tx):
    for record in tx.run("MATCH (n:Exercice) return n limit 4"):
        print((record[0]._id))
        print((record[0].labels))
        print(record[0]._properties['question'])

with driver.session() as session:
    session.read_transaction(print_friends)