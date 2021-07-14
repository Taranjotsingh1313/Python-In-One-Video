class Grandfather:
    haircolor = 'Brown'

class Dad(Grandfather):
    # haircolor = "Black"
    pass

class Son(Dad):
    # haircolor = "White"
    pass
print(Son.haircolor)
