class BinaryNode:
    def __init__(self , value , left=None , rigth= None):
        self.data=value
        self.left=left
        self.rigth=rigth

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.__insert_nodo(self.root,value)
        
    def __insert_nodo(self, nodo, value):
        if nodo.data ==value: 
            pass
        elif value < nodo.data:
            if nodo.left ==None:
                nodo.left=BinaryNode(value)
            else:
                self.__insert_nodo( nodo.left ,value)
        else:  #--->
            if nodo.rigth == None:
                nodo.rigth = BinaryNode( value)
            else:
                self.__insert_nodo( nodo.rigth , value)
    
    def remove(self,value):
        if self.root == None:
            print("árbol vacío")
            return None
        else:
            if self.root==value:
                pass
            else :
                self.__remove(self.root,value)

    def __remove(self,nodo, value):
        if nodo ==None:
            print("no existe en el árbol") 
        elif nodo.data==value:
            if nodo.left ==None and nodo.rigth==None:
                nodo=None
            elif nodo.left!=None and nodo.rigth==None:
                nodo = nodo.left
                nodo.left =None
            elif nodo.left ==None and nodo.rigth !=None:
                nodo=nodo.rigth
                nodo.rigth =None
            elif nodo.left!=None and nodo.rigth!=None:
                nodo=nodo.left
                nodo.left=nodo.left.left
        elif value<nodo.data:
            return self.__remove(nodo.left,value)
        else:
            return self.__remove(nodo.rigth,value)

    def search(self,value):
        if self.root==None:
            print("árbol vacío")
            return None
        else:
            return self.__search(self.root,value)

    def __search(self,nodo,value):
        if nodo==None:
            print("no existe en el árbol") 
            return None
        elif nodo.data== value:
            print("Encontrado", nodo.data)
            return nodo
        elif value<nodo.data:
            return self.__search(nodo.left,value)
        else:
            return self.__search(nodo.rigth,value)  
    

    def  recorrido_pos(self,nodo):
        if nodo!= None:
            self.recorrido_pos(nodo.left)
            self.recorrido_pos(nodo.rigth)
            print( str(nodo.data),end=",")
    
    def  recorrido_pre(self,nodo):
        if nodo!=None:
            print(str(nodo.data),end=",")
            self.recorrido_pre(nodo.left)
            self.recorrido_pre(nodo.rigth)
    
    def  recorrido_in(self,nodo):
        if nodo!=None:
            self.recorrido_in(nodo.left)
            print(str(nodo.data),end=",")
            self.recorrido_in(nodo.rigth) 
    def transversal(self,formato="pos-orden"):
            if formato =="pos-orden":
                self.recorrido_pos(self.root)
            elif formato =="pre-orden":
                self.recorrido_pre(self.root)
            else: # inorden
                self.recorrido_in( self.root)
            print()    

arbol1 = BinarySearchTree()
arbol1.insert(60)
arbol1.insert(30)
arbol1.insert(15)
arbol1.insert(40)
arbol1.insert(5)
arbol1.insert(75)
arbol1.insert(85)
arbol1.insert(90)
arbol1.transversal("\n pos-orden")
arbol1.transversal("preo-rden\n")
arbol1.transversal("in-orden\n")
res = arbol1.search(15)
print(res,"\n") # apunta a la localizacion de la memoria donde se almacena el nodo res
#15
print(res.data,"\n") 
print(res.left.data,"\n")

arbol1.remove(15)
arbol1.transversal("inorden")