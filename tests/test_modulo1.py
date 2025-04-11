import pytest
from progetto.modulo1 import funzione1, funzione2, classeDaFinire

def test_funzione1():
    # TODO Aggiungere 2 o più test per coprire funzione1
    pass

def test_funzione2():
    # TODO Aggiungere 2 o più test per coprire funzione2
    pass

def test_funzione2():
    # TODO Aggiungere 2 o più test per coprire funzione3
    pass

def test_metodo1():
    istanza = classeDaFinire("Nome")
    assert istanza.metodo2() == "  "

def test_metodo2():
    istanza = classeDaFinire("Test")
    istanza.metodo2(5)
    # TODO: Aggiungere un'asserzione per verificare il comportamento del metodo2
    pass