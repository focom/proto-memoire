if __name__ != '__main__':
    from neo4j import *
    import fileinput
    import helper.gauss as Gauss 
    from DB.createGraph import createQuery
# from createGraph import createQuery
# driver = GraphDatabase.driver("bolt://localhost:11001", auth=("neo4j", "root"))

# theme1 -> theme2
# theme1 -> [3,4] | 3 -> [6,7] | 4 -> [8,9]
# theme2 -> [5] | 5 -> [10,11]


class Graph:
    def __init__(self, student_name):
        self.student_name = student_name
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "root"))

    def get_db(self):
        return self.driver.session()
    
    def getExerciseNode(self,id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._ExerciseNode, id_node)

    def _ExerciseNode(self, tx, id_node):
        db = self.get_db()
        query = f"MATCH (n:Chapitre)<-[]-(e:Exercice) where n.id_node={id_node} return e limit 20"
        # print(query)
        number = 0
        instruction = []
        question = []
        correct = []
        wrong = []
        for record in tx.run(query):
            number += 1
            instruction.append(record[0]._properties['instruction'])
            question.append(record[0]._properties['question'])
            correct.append(record[0]._properties['answer'][0])
            wrong.append(record[0]._properties['answer'][1])
        print(instruction)
        return (id_node,number,instruction,question,correct,wrong)

    def getGradeNode(self, id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._gradeNode, id_node)

    def _gradeNode(self, tx, id_node):
        db = self.get_db()
        query = f"MATCH (s:Student) where s.name='{self.student_name}' match (s)-[:link*1..7]-(n:Chapitre) where n.id_node={id_node} return n;"
        # print(query)
        result = db.run(query)
        for record in result:
            return (record[0]._properties['grade'])

    def getHistoryNode(self, id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._historyNode, id_node)

    def _historyNode(self, tx, id_node):
        db = self.get_db()
        query = f"MATCH (s:Student) where s.name='{self.student_name}' match (s)-[:link*1..7]-(n:Chapitre) where n.id_node={id_node} return n;"
        # print(query)
        result = db.run(query)
        for record in result:
            return (record[0]._properties['history'])

    def getWeightNode(self, id_node):
        with self.driver.session() as session:
            return session.read_transaction(self._weightNode, id_node)

    def _weightNode(self, tx, id_node):
        db = self.get_db()
        query = f"MATCH (s:Student) where s.name='{self.student_name}' match (s)-[:link*1..7]-(n:Chapitre) where n.id_node={id_node} return n;"
        # print(query)
        result = db.run(query)
        for record in result:
            return (record[0]._properties['weight'])

    
    # options -> [id_node,grade]
    def setGrade(self,options):
        with self.driver.session() as session:
            return session.read_transaction(self._setGrade, options)

    def _setGrade(self,tx,options):
        db = self.get_db()
        query = f"MATCH (s:Student) where s.name='{self.student_name}' match (s)-[:link*1..7]-(n:Chapitre) where n.id_node={options[0]} SET n.history=n.score SET n.grade={options[1]}"
        # print(query)
        db.run(query)



    def runUpdateGraph(self):
        with self.driver.session() as session:
            session.read_transaction(self.updateGraph)

    def createStudentGraph(self):
        query = createQuery(self.student_name)
        db = self.get_db()
        print('Nouveau apprenant crée')
        db.run(query)


    # Before Selecting best path
    
    def updateNode (self,parentNode,childNodes):
        parentNode_grade = self.getGradeNode(parentNode)
        print(f'Updating: {parentNode} with {childNodes}')
        print(parentNode_grade)
        # parentNode_grade = self.getGradeNode(parentNode)
        grade_child = []
        for child in childNodes:
            grade_child.append(self.getGradeNode(child))
        print(grade_child)
        new_parent_score = Gauss.getScore(parentNode_grade,grade_child)
        new_parent_score = Gauss.getGrade(new_parent_score)
        print ('Grade parent ',parentNode,': ',new_parent_score,' Grade enfant: ',grade_child)
        self.setGrade([parentNode,new_parent_score])

    def updateGraph(self):
        # theme1 -> theme2
        # theme1 -> [3,4] | 3 -> [6,7] | 4 -> [8,9]
        # theme2 -> [5] | 5 -> [10,11]

        # there is 5 update to do following a certain order
        self.updateNode(3,[6,7])
        self.updateNode(4,[8,9])
        self.updateNode(1,[3,4])
        self.updateNode(5,[10,11])
        self.updateNode(2,[5])

    def selectExercise(self):
        grade1 = self.getGradeNode(1)
        if(grade1 != 4):
            grade3 = self.getGradeNode(3)
            grade4 = self.getGradeNode(4)
            if(grade3 > grade4):
                grade8 = self.getGradeNode(8)
                grade9 = self.getGradeNode(9)
                if(grade8 > grade9):
                    return self.getExerciseNode(9)
                else:
                    return self.getExerciseNode(8)
            else:
                grade6 = self.getGradeNode(6)
                grade7 = self.getGradeNode(7)
                if(grade6 > grade7):
                    return self.getExerciseNode(7)
                else:
                    return self.getExerciseNode(6)
        else:
            grade10 = self.getGradeNode(10)
            grade11 = self.getGradeNode(11)
            if(grade10>grade11):
                return self.getExerciseNode(11)
            else:
                return self.getExerciseNode(10)



        
# if (__name__ == '__main__'):
#     import sys
#     from neo4j import GraphDatabase
#     sys.path.append('..')
#     from createGraph import createQuery
#     import helper.gauss as Gauss
#     graph = Graph('Ancien')
#     # graph.createStudentGraph()
#     print(graph.getGradeNode(6))
#     graph.setGrade([6,3])
#     graph.updateGraph()
#     print(graph.getGradeNode(6))
#     # graph.getExerciseNode(7)
