'''
Created on 13.01.2016

@author: Asthmet
'''

c_mine = 'X'
c_empty = '.'
c_flag = '>'
c_covered = '#'


class Plot:

    def __init__( self, x = 0, y = 0 ):
        self.indicator = '.'
        self.flag = '.'
        self.revealed = False

    def getIndicator( self, trueSight = False ):
        if trueSight == True :
            return self.indicator
        else :
            if self.revealed == True :
                return self.indicator
            else :
                return c_covered

    def setIndicator( self, ind = c_empty ):
        if ind == '0' :
            self.indicator = c_empty
        else :
            self.indicator = ind

    def setMine( self ):
        self.indicator = c_mine

    def toggleFlag( self ):
        if self.flag == '' :
            self.flag = c_flag
        else :
            self.flag = ''
            
    def revealPlot( self ):
        self.revealed = True
            
    