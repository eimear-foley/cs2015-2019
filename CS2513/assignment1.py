class Light(object):

    def __init__(self, state, wattage):

        """Light is a class defined by the following instance variables:
             - state of lightbuld i.e. on or off
             - wattage of lightbuld"""
        
        self._state = state  
        self._wattage = wattage 

    def __str__(self):

        """String representation of the instance variables of the class 'Light'
           i.e. 'state', 'wattage' """

        descriptive_str = ("Lightbulb: State = %s, Wattage = %i" % (self._state, self._wattage))
        return descriptive_str

    def getState(self):

        """Returns the current state of the lightbulb i.e. on or off """
        return ('Lightbulb is %s' % (self._state))

    def getWattage(self):

        """Returns the wattage of the lightbulb. """
        return ('Lightbuld wattage is %i' % (self._wattage))

    def setWattage(self, value):

        """Sets wattage of lightbulb to value specified by user. """

        if str(value).isdigit() and value > 0:
            self._wattage = value
            return("Lightbulb wattage is %i" % (self._wattage))
        else:
            return('%s is not a valid value. Please set the lightbulb to a valid wattage value.' % (value))

    def switchLight(self):

        """Switches lightbulb to inverted version of current state. """
        
        if self._state == 'on':
            self._state = 'off'
        else:
            self._state = 'on'
            
        return('Lightbuld is now %s' % (self._state))

    wattage = property(getWattage, setWattage)
    state = property(getState)

def main():
   
    """Test block which is execute only when the module is run,
       not when it is imported."""

    led = Light('on', 50)
    print(led)

    print(led.state)
    print(led.wattage)
    led.wattage = 100
    print(led.wattage)
    led.wattage = -10
    print(led.wattage)

    print(led.switchLight())
    
if __name__ == "__main__":
    main()
