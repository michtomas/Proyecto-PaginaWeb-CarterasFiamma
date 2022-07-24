class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get('carro')
        #crear carro si no esta hecho antes:
        if not carro:
            carro=self.session['carro']={} #el carro es un diccionario
        #else:
            #si ya habia un carro y la persona sale la pagina y vuelve queremos recuperarlo
        self.carro=carro

    def agregar_producto(self,producto):
        if(str(producto.id) not in self.carro.keys()): #si no esta el id en las keys del carro
            self.carro[producto.id]={"id":producto.id, "nombre":producto.nombre,"color":producto.color , "precio":str(producto.precio), "cantidad":1,"imagen":producto.imagen.url}
        else:
            pass #no se puede agregar mas de un producto en este caso, capaz mostrar un mensaje???
        
        self.guardarCarro()#actualizar carrito
    
    def guardarCarro(self): #funcion guardar/actualizar carrito
        self.session['carro']=self.carro
        self.session.modified=True

    def eliminar_producto(self,producto):
        if(str(producto.id) in self.carro.keys()):
            del(self.carro[str(producto.id)])
            self.guardarCarro()
    
    def vaciar_carro(self):
        self.session['carro']={}
        self.session.modified=True
