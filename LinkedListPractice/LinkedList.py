from Node import Node

class LinkedList:
    def __init__( self ):
        self.head = None
    
    def insertLast( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
    
    def printList( self ):
        current = self.head
        while current != None:
            print( current.val )
            current = current.next

    def insertFirst( self, val )
        newNode = Node( val )
        if self.head == None: #Paso 1, decir que es un node, pasando de head a newNode
            self.head = newNode
        else:
          newNode.next= self.head  #Paso 2: el next apunta al último, el último se llama none, por lo que hay que cambiar que apunte al principio (head)
          self.head=newNode #paso 3, ahora que el node está frente al head, hay que cambiarlo para que sea el nuevo head.

    def findNode( self, val ):
        current = self.head
        while current != None:
            if current.val == val: #esto significa que encontramos un match
                return current #Esto va a devolver todo el Object
            current = current.next
        return None

    def deleteNode ( self, val ):
        current = self.head
        previous = self.head #Es necesario un previo, para que salte el que hay que borrar

#If para corregir el problema del While que se explica adelante:
        if self.head.val==val:
            self.head=self.head.next
            current.next=None

#El siguiente While no funciona para el primer valor, pues convierte el primer Next a un None, esto destruye la cadena. 
        while current != None and current.val != val:
            previous = current #Esto mueve el previuos al siguiente node
            current = current.next #Esto mueve el current al siguiente node.
            #Esta combinación hace que las variables se muevan de uno en uno hasta hacer match

        if current != None:
            previous.next = current.next
            current.next = None
