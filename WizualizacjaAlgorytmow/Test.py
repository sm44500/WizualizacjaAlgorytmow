from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import QTest
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import random
from algorithms.example.MinSearch import MinSearch
import time

class PrettyWidget(QWidget):

    def __init__(self,snapshot):
        super(PrettyWidget, self).__init__()
        font = QFont()
        font.setPointSize(16)
        self.initUI(snapshot)

    def initUI(self,snapshot):
        self.setGeometry(100, 100, 1200, 600)
        self.center()
        self.setWindowTitle('S Plot')
        grid = QGridLayout()
        self.setLayout(grid)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 0, 1, 9, 9)
        #self.addNodes(snapshot)
        # self.addNodz()
        #self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addNodes(self,snapshot):
        self.figure.clf()

        Nodes = nx.Graph()
        Nodes.add_nodes_from(snapshot.data)
        #for i in range(len(snapshot.data)):
            #Nodes.add_node(snapshot.data[i],weight=i)
            
        X = set( n for n, d in Nodes.nodes(data=True) )
        #print( [ d for n, d in Nodes.nodes(data=True) ] )
        pos = dict()
        pos.update( (element, (i, 1)) for i, element in enumerate(snapshot.data) )
        # pos.update((0, (len(X)+1, 1)))
        # pos.append( (element, (i, 1)) for i, element in enumerate(X) )
        ax1 = plt.axes( [ 0.0, 0.0, 1.0, 1.0 ] )

        import collections
        tmp_color=list()
        for i in range(len(snapshot.data)):
            tmp_color.append(snapshot.highlights[i])
        
        
        nx.draw(Nodes, pos=pos, with_labels=True, node_size=50**2, ax=ax1, node_color=tmp_color)

        # B.add_nodes_from([1, 2, 3, 4], bipartite=0)
        # B.add_nodes_from(['a', 'b', 'c', 'd', 'e'], bipartite=1)
        # B.add_edges_from([(1, 'a'), (2, 'c'), (3, 'd'), (3, 'e'), (4, 'e'), (4, 'd')])

        # X = set( n for n, d in B.nodes(data=True) )
        # Y = set(B) - X

        # X = sorted(X, reverse=True)
        # Y = sorted(Y, reverse=True)

        # pos = dict()
        # pos.update( (n, (i, 1)) for i, n in enumerate(X) ) # put nodes from X at x=1
        # pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
        # nx.draw( Nodes, pos=pos, with_labels=True)
        self.canvas.draw_idle()

    def addNodz(self):
        import Nodz.nodz_main as nodz_main
        nodz = nodz_main.Nodz(None)
        nodz.initialize()
        nodz.show()

        layout = QVBoxLayout()
        self.figure.clf()
        nodeA = nodz.createNode(name='a',preset='node_preset_1',position=None)
        nodz.createAttribute(node=nodeA, name='Attr1', index=-1, plug=True, socket=False, dataType=str)

        qp = QPainter()
        nodz.drawFrame( qp )
        self.canvas.draw_event( qp )
        self.canvas.draw_idle()


if __name__ == '__main__':


    algo=MinSearch()
    algo.add_element(10)
    algo.add_element(15)
    algo.add_element(1)
    algo.add_element(71)
    algo.add_element(-21)
    algo.execute()
    #for snapshot in algo.snapshots:
      #  print(snapshot.description)
       # print(snapshot.highlights)
      #  print(snapshot.data)
        
  #  print(algo.snapshots[-1].highlights[4])    
    

    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    app.setStyle(QStyleFactory.create("gtk"))
    screen = PrettyWidget(None)
    for snapshot in algo.snapshots: 
        screen.addNodes(snapshot)
        screen.show()
        print(snapshot.description)
        QTest.qWait(2000)
    sys.exit(app.exec_())
    
    
    