'''
Created on 13.01.2016

@author: Asthmet
'''
import plot_class
import random

class Minesweeper:

    ''' Constructor of the class: start the game for you '''
    def __init__( self, lines = 10, cols = 10 ):
        self._lines = lines
        self._cols = cols
        self._map = [ [plot_class.Plot() for i in range(cols) ] for j in range(lines) ]

    ''' Returns the display of the cell '''
    def getCell( self, x, y ):
        var = self._map[x][y]
        return var.getIndicator( trueSight = True )

    ''' Display the whole map for the player '''
    def displayMap( self, trueSight = False ):
        count = 0
        for line in self._map:
            print( ' ', sep = '', end = '' )
            for col in line:
                if col.getIndicator(trueSight = True) == plot_class.c_mine :
                    count += 1
                print( col.getIndicator( trueSight = trueSight ), sep = '', end = '' )
                print( ' ', sep = '', end = '' )
            print( )
        print( 'Total : ' + str(count) + ' mines' + ' - Format: ' + str(self._cols) + 'x' + str(self._lines) + '\n' )

    ''' Add a random bomb to the map '''
    def randomBomb( self ):
        x = random.randrange( self._lines )
        y = random.randrange( self._cols )

        if self.getCell( x, y ) == plot_class.c_mine :
            self.randomBomb()
        else :
            self._map[x][y].setMine()

    ''' Generate as much bombs as specified '''
    def carpetBomb( self, n = 10 ):
        for i in range(n):
            self.randomBomb()

    ''' Pass through every plot to determine its indicator value '''
    ''' Run this only once after doing the carpet bomb'''
    def scanMap( self ):
        for i, line in enumerate( self._map ) :
            for j, p in enumerate( line ) :
                count = 0
                if p.getIndicator(trueSight = True) == plot_class.c_mine :
                    continue
                else :
                    # up left
                    if i-1 >= 0 and j-1 >= 0 :
                        if self.getCell( i-1, j-1 ) == plot_class.c_mine :
                            count += 1
                    # up top
                    if i-1 >= 0 :
                        if self.getCell( i-1, j ) == plot_class.c_mine :
                            count += 1
                    # up right
                    if i-1 >= 0 and j+1 < self._cols :
                        if self.getCell( i-1, j+1 ) == plot_class.c_mine :
                            count += 1
                    # left
                    if j-1 >= 0 :
                        if self.getCell( i, j-1 ) == plot_class.c_mine :
                            count += 1
                    # right
                    if  j+1 < self._cols :
                        if self.getCell( i, j+1 ) == plot_class.c_mine :
                            count += 1
                    # down left
                    if i+1 < self._lines and j-1 >= 0 :
                        if self.getCell( i+1, j-1 ) == plot_class.c_mine :
                            count += 1
                    # down bottom
                    if i+1 < self._lines :
                        if self.getCell( i+1, j ) == plot_class.c_mine :
                            count += 1
                    # down right
                    if i+1 < self._lines and j+1 < self._cols :
                        if self.getCell( i+1, j+1 ) == plot_class.c_mine :
                            count += 1

                p.setIndicator( str(count) )

    ''' Give the player the first start into the game '''
    def showClue( self ):
        x = random.randrange( self._lines )
        y = random.randrange( self._cols )

        if self.getCell( x, y ) != plot_class.c_empty :
            self.showClue()
        else :
            self._map[x][y].revealPlot()
            self.propagateDiscovery(x, y)

    ''' When a empty plot is found, we look for other similar neighbor '''
    def propagateDiscovery( self, x, y ):
        if self.getCell(x, y) == plot_class.c_empty :

            # Reveal the plot and propagate to the neighbors
            self._map[x][y].revealPlot()

            # up left
            if x-1 >= 0 and y-1 >= 0 and self._map[x-1][y-1].revealed == False :
                self.propagateDiscovery(x-1, y-1)

            # up top
            if x-1 >= 0 and self._map[x-1][y].revealed == False :
                self.propagateDiscovery(x-1, y)

            # up right
            if x-1 >= 0 and y+1 < self._cols and self._map[x-1][y+1].revealed == False :
                self.propagateDiscovery(x-1, y+1)

            # left
            if y-1 >= 0 and self._map[x][y-1].revealed == False :
                self.propagateDiscovery(x, y-1)

            # right
            if y+1 < self._cols and self._map[x][y+1].revealed == False :
                self.propagateDiscovery(x, y+1)

            # down left
            if x+1 < self._lines and y-1 >= 0 and self._map[x+1][y-1].revealed == False :
                self.propagateDiscovery(x+1, y-1)

            # down bottom
            if x+1 < self._lines and self._map[x+1][y].revealed == False :
                self.propagateDiscovery(x+1, y)

            # down right
            if x+1 < self._lines and y+1 < self._cols and self._map[x+1][y+1].revealed == False :
                self.propagateDiscovery(x+1, y+1)

        else :
            # just reveat the plot
            self._map[x][y].revealPlot()

    '''  '''
    def findUnsolvable( self ):
        for i, line in enumerate( self._map ) :
            for j, p in  enumerate( line ) :
                if self.getCell(i, j) == plot_class.c_empty and self._map[i][j].revealed == False  :
                    self.propagateDiscovery(i, j)


#----------------------
# Creating the application
program = Minesweeper( lines = 16, cols = 30 )
program.carpetBomb(50)
program.scanMap()
program.displayMap( trueSight = True )
#program.findUnsolvable()
program.propagateDiscovery( 0, 0)
program.displayMap()
