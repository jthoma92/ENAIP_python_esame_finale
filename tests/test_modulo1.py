import pytest
from progetto.modulo1 import funzione1, funzione2, funzione3, classeDaFinire

def test_funzione1():
    # TODO Aggiungere 2 o più test per coprire funzione1
    assert funzione1(5,2) == 10
    assert funzione1 (9,2) == 18

def test_funzione2():
    # TODO Aggiungere 2 o più test per coprire funzione2
    assert funzione2("John") == "Ciao John felice di vederti!"
    assert funzione2("Corina") == "Ciao Corina felice di vederti!"

def test_funzione3():
    # TODO Aggiungere 2 o più test per coprire funzione3
    assert funzione3(17,3) == 17
    assert funzione3(234, 56) == 234

def test_metodo1():
    istanza = classeDaFinire("Anna", 10, "Milano")
    # TODO: Modificare l'assert per far passare il test
    assert istanza.metodo1() == "Anna ha 10 anni e viene da Milano"

def test_metodo2():
    istanza = classeDaFinire("Mario", 35, "Trieste")
    
    # TODO: Aggiungere un'asserzione per verificare il comportamento del metodo2
    assert istanza.metodo2(5) == "Mario tra 5 anni avrà 40 anni"
