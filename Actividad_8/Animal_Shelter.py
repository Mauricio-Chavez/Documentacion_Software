import datetime
class Animal:
    """
        Clase que representa a un animal ( Perro )
    """
    def __init__(self,name,age,breed,date):
        """
                Constructor de la clase Animal.

                Argumentos y Atributos de la Clase:
                    name (str): Nombre del animal.
                    age (int): Edad del animal.
                    breed (str): Raza del animal.
                    date (datetime): Fecha de ingreso del animal.
        """
        self.name=name
        self.age=age
        self.breed=breed
        self.date=date
        self.next=None


class Queue:
    """
      Clase que representa una cola de adopción de animales.
    """
    def __init__(self):
        """
                Constructor de la clase Queue.
                 Atributos:
                    First (Animal): Apunta al primer Animalito de la Fila.
                    Length (int): Nos dice cuantos Animalitos hay en la cola.
                    Last(Animal): Apunta al ultimo Animalito de la Fila.

        """
        self.first=None
        self.length=0
        self.last=None
    def dog_enqueue(self,name,age,breed):
        """
                Agrega un perro a la cola de adopción.

                Argumentos:
                    name (str): Nombre del perro.
                    age (int): Edad del perro.
                    breed (str): Raza del perro.
        """
        date=datetime.datetime.now()
        new_node=Animal(name,age,breed,date)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return
    def print_queue(self):
        """
                Imprime los animales disponibles en la cola de adopción.
        """
        tem=self.first
        while tem is not None:
            print("-----------------------------------------")
            print(f"Name: {tem.name} Age: {tem.age} Breed: {tem.breed} Date: {tem.date}")
            print("-----------------------------------------")
            tem = tem.next
    def dog_dequeue(self):
        """
               Adquiere un perro de la cola y lo elimina de la misma.

               Returns:
                   Animal|False: El perro adquirido o False si la cola está vacía.
        """
        tem = self.first
        if self.first==None:

            return False
        else:
            if self.first==self.last:
                self.first=None
                self.last=None
            else:
                self.first=tem.next
                tem.next=None

        self.length-=1
        return tem




my_queue=Queue()
selection=0
"""
    Menú de Seleccion de de la operacion que se requiere realizar en el programa

"""
while True:
    print("\n")
    print("1.-Ingresar un Animalito")
    print("2.-Imprimir los animalitos disponibles")
    print("3.-Adoptar un Animalito")
    print("4.-Salir")
    selection=int(input())
    match selection:
        case 1:
            name=str(input("Ingresa el nombre del Animalito: \n"))
            age=int(input("Ingresa la edad del Animalito: \n"))
            breed=str(input("Ingresa la raza del Animalito: \n"))
            my_queue.dog_enqueue(name,age,breed)
        case 2:
            my_queue.print_queue()
        case 3:
            r = my_queue.dog_dequeue()
            if r==False:
                print("De momento ya no tenemos mas animalitos en adopcion")
            else:
                print("------------------------------------------")
                print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                print("------------------------------------------")
        case 4:
            print("Saliendo...")
            exit()