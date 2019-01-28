import webbrowser
from classes.helper.visu import generateHTML 
class Viz:

  def __init__(self,graph):
    self.colors = []
    for i in range(1,13):
      self.colors.append(self.getColor(graph.getGradeNode(i)))


  def getColor(self,grade):
    if (grade == 0):
      return '#999966'
    if (grade == 1):
      return '#cc0000'
    if (grade == 2):
      return '#ff6600'
    if (grade == 3):
      return '#ffff00'
    if (grade == 4):
      return '#00ff00'

  def visual(self):
    html = generateHTML(self.colors)
    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "html/visu.html"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, "w") as text_file:
      text_file.write(html)
    webbrowser.open(abs_file_path)

if __name__ == '__main__':
  import sys
  from graph import Graph
  sys.path.insert('..')
  graph = Graph('Pierre')
  viz = Viz(graph)
  viz.visual()
  