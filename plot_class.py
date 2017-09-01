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

    ''' Returns the value of the indicator based on visibility'''
    def getIndicator( self, trueSight = False ):
        if trueSight == True :
            return self.indicator
        else :
            if self.revealed == True :
                return self.indicator
            else :
                return c_covered

    ''' Set the value of the plot to $ind '''
    def setIndicator( self, ind = c_empty ):
        if ind == '0' :
            self.indicator = c_empty
        else :
            self.indicator = ind

    ''' Set the value of the plot to MINE '''
    def setMine( self ):
        self.indicator = c_mine

    ''' Change the flag state of a plot '''
    def toggleFlag( self ):
        if self.flag == '' :
            self.flag = c_flag
        else :
            self.flag = ''

    ''' Reveal the plot to the user  (no effect when trueSight is active)'''
    def revealPlot( self ):
        self.revealed = True
