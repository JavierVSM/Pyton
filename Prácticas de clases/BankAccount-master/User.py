class User:
    def __init__( self, fN = "N/A", lN = "N/A", age = -1 ):
        # Attributes
        self.firstName = fN
        self.lastName = lN
        self.age = age

    def printUserInfo( self ):
        print( f"First name: {self.firstName}\nLast name: {self.lastName}\nAge: {self.age}" )
