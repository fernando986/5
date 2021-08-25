import negocio.heroes as ng

op = -1



def mostrar_heroe(heroe):
    print('ha discrecion')

while op != 0:

    print('(1) Mostrar heroes de DC')
    print('(2) Mostrar heroes de MARVEL')
    print('(3) Buscar heroe por ID')

    op = int(input('Ingreso opcion: '))

    if op == 1:
        heroes = ng.buscar_heroes_por_publisher('DC Comics')
        print(heroes)
    elif op == 2:
        heroes = ng.buscar_heroes_por_publisher('Marvel Comics')
        print(heroes)
    elif op ==3:
        print('Ingresar el ID:')
        h={
        'id': 'dc-superman',
        'superhero':'Superman', 
        'publisher':'DC Comics', 
        'alter_ego':'Kal-El',
        'first_appearance':'Action Comics #1',
        'characters':'Kal-El'}
        mostrar_heroe(h)
        

