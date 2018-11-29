import sqlite3
import os.path,sys

class Students:
  def __init__ (self, name, level):
    self.name = name
    self.level = level
     
  def saveStudents(self):
    conn = sqlite3.connect(os.path.dirname(__file__)+'/../DB/proto.db3')
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?,?,?)", [None,self.name, self.level])
    conn.commit()
    conn.close()
 
  def findStudents(self):
    conn = sqlite3.connect(os.path.dirname(__file__)+'/../DB/proto.db3')
    c = conn.cursor()

    return True


if __name__ == "__main__":
  
  # print(os.path.dirname(__file__))
  # print("")
  # print(os.path.dirname(__file__)+'/../DB/proto.db3')
  # print(environ.Path())
  etudiant = Students("Jeanne", "Bad")
  etudiant.saveStudents()