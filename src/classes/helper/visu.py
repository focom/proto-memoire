
def generateHTML(colors):
    print(colors)
    node1 = f"""id: '1',
        label: 'Theme 1',
        x: 7,
        y: 1,
        size: 1,
        color: '{colors[0]}'"""

    node2 = f"""id: '2',
        label: 'Theme 2',
        x: 12,
        y: 1,
        size: 1,
        color: '{colors[1]}'"""
    node3 = f"""id: '3',
        label: 'Constituant de la phrase',
        x: 5,
        y: 3,
        size: 1,
        color: '{colors[2]}'"""
    node4 = f"""id: '4',
        label: 'Types de phrase et accord du verbe',
        x: 9,
        y: 3,
        size: 1,
        color: '{colors[3]}'"""
    node5 = f"""id: '5',
        label: 'Homophone',
        x: 14,
        y: 3,
        size: 1,
        color: '{colors[4]}'"""
    node6 = f"""id: '6',
        label: 'Apprentissage',
        x: 4,
        y: 5,
        size: 1,
        color: '{colors[5]}'"""
    node7 = f"""id: '7',
        label: 'Appronfondissement',
        x: 6,
        y: 5,
        size: 1,
        color: '{colors[6]}'"""
    node8 = f"""id: '8',
        label: 'Type de phrase',
        x: 8,
        y: 5,
        size: 1,
        color: '{colors[7]}'"""
    node9 = f"""id: '9',
        label: 'Accord du verbe',
        x: 10,
        y: 5,
        size: 1,
        color: '{colors[8]}'"""
    node10 = f"""id: '10',
        label: 'Homonyme',
        x: 13,
        y: 5,
        size: 1,
        color: '{colors[9]}'"""
    node11 = f"""id: '11',
        label: 'Autre Cas',
        x: 15,
        y: 5,
        size: 1,
        color: '{colors[10]}'"""

    html = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <!-- START SIGMA IMPORTS -->
  <script src="./src/sigma.core.js"></script>
    <script src="./src/conrad.js"></script>
    <script src="./src/utils/sigma.utils.js"></script>
    <script src="./src/utils/sigma.polyfills.js"></script>
    <script src="./src/sigma.settings.js"></script>
    <script src="./src/classes/sigma.classes.dispatcher.js"></script>
    <script src="./src/classes/sigma.classes.configurable.js"></script>
    <script src="./src/classes/sigma.classes.graph.js"></script>
    <script src="./src/classes/sigma.classes.camera.js"></script>
    <script src="./src/classes/sigma.classes.quad.js"></script>
    <script src="./src/classes/sigma.classes.edgequad.js"></script>
    <script src="./src/captors/sigma.captors.mouse.js"></script>
    <script src="./src/captors/sigma.captors.touch.js"></script>
    <script src="./src/renderers/sigma.renderers.canvas.js"></script>
    <script src="./src/renderers/sigma.renderers.webgl.js"></script>
    <script src="./src/renderers/sigma.renderers.svg.js"></script>
    <script src="./src/renderers/sigma.renderers.def.js"></script>
    <script src="./src/renderers/webgl/sigma.webgl.nodes.def.js"></script>
    <script src="./src/renderers/webgl/sigma.webgl.nodes.fast.js"></script>
    <script src="./src/renderers/webgl/sigma.webgl.edges.def.js"></script>
    <script src="./src/renderers/webgl/sigma.webgl.edges.fast.js"></script>
    <script src="./src/renderers/webgl/sigma.webgl.edges.arrow.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.labels.def.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.hovers.def.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.nodes.def.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edges.def.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edges.curve.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edges.arrow.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edges.curvedArrow.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edgehovers.def.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edgehovers.curve.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edgehovers.arrow.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.edgehovers.curvedArrow.js"></script>
    <script src="./src/renderers/canvas/sigma.canvas.extremities.def.js"></script>
    <script src="./src/renderers/svg/sigma.svg.utils.js"></script>
    <script src="./src/renderers/svg/sigma.svg.nodes.def.js"></script>
    <script src="./src/renderers/svg/sigma.svg.edges.def.js"></script>
    <script src="./src/renderers/svg/sigma.svg.edges.curve.js"></script>
    <script src="./src/renderers/svg/sigma.svg.labels.def.js"></script>
    <script src="./src/renderers/svg/sigma.svg.hovers.def.js"></script>
    <script src="./src/middlewares/sigma.middlewares.rescale.js"></script>
    <script src="./src/middlewares/sigma.middlewares.copy.js"></script>
    <script src="./src/misc/sigma.misc.animation.js"></script>
    <script src="./src/misc/sigma.misc.bindEvents.js"></script>
    <script src="./src/misc/sigma.misc.bindDOMEvents.js"></script>
    <script src="./src/misc/sigma.misc.drawHovers.js"></script>
    <!-- END SIGMA IMPORTS -->
    <title>Visualisation prototype</title>
    <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css">
  </head>

  <body>
    <div id="container">
      <style>
        #graph-container {
          top: 50px;
          bottom: 50px;
          left: 50px;
          right: 50px;
          position: absolute;
        }
      </style>
      <div id="graph-container"></div>
    </div>
    <script>
      /**
      * This is a basic example on how to instantiate sigma. A random graph is
      * generated and stored in the "graph" variable, and then sigma is instantiated
      * directly with the graph.
      *
      * The simple instance of sigma is enough to make it render the graph on the on
      * the screen, since the graph is given directly to the constructor.
      */
      var i,
        s,
        N = 2,
        E = 1,
        g = {
          nodes: [{"""+node1+"""
      },{"""+node2+"""
      },{"""+node3+"""
      },{"""+node4+"""
      },{"""+node5+"""
      },{"""+node6+"""
      },{"""+node7+"""
      },{"""+node8+"""
      },{"""+node9+"""
      },{"""+node10+"""
      },{"""+node11+"""
      }],
          edges: [{
          id: '1',
          source: 1,
          target: 2,
          size: 1,
          color: '#000000'
        },{
          id: '2',
          source: '3',
          target: '1',
          size: 1,
          color: '#000000'
        },{
          id: '4',
          source: '6',
          target: '3',
          size: 1,
          color: '#000000'
        },{
          id: '5',
          source: '7',
          target: '3',
          size: 1,
          color: '#000000'
        },{
          id: '6',
          source: '8',
          target: '4',
          size: 1,
          color: '#000000'
        },{
          id: '7',
          source: '9',
          target: '4',
          size: 1,
          color: '#000000'
        },{
          id: '8',
          source: '5',
          target: '2',
          size: 1,
          color: '#000000'
        },{
          id: '9',
          source: '10',
          target: '5',
          size: 1,
          color: '#000000'
        },{
          id: '10',
          source: '11',
          target: '5',
          size: 1,
          color: '#000000'
        },{
          id: '11',
          source: '4',
          target: '1',
          size: 1,
          color: '#000000'
        }]
        };

      // Instantiate sigma:
      s = new sigma({
        graph: g,
        container: 'graph-container',
        settings: {
          sideMargin: 1,
          defaultLabelSize: 16,
          labelThreshold: 2
        }
      });
    </script>
  </body>

  </html>
  """
    return html