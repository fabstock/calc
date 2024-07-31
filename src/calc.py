
"""
python3 src/calc.py 

This is doc with pydoc.  
To generate HTML documentation for this module issue the
command:
    pydoc3 -w calc

"""


# -*- coding: utf-8 -*-
#!/usr/bin/python3
import pydoc



def saisir():
    """
    Saisir 2 nb .
        nb1 est le 1er nb
        nb2 est le 2nd nb
    """
    nb1=int(input("saisir un 1er nb"))
    nb2=int(input("saisir un 2nd nb"))
    return (nb1,nb2)

def addition(nb1,nb2):
    """
    Addition.
	nb1 est le 1er nb
        nb2 est le 2nd nb
    """
    print("add: ",nb1+nb2) 
    return (nb1+nb2)

def substraction(nb1,nb2):
    """
    Substraction.
        nb1 est le 1er nb
        nb2 est le 2nd nb
    """
    print("sub: ",nb1-nb2) 
    return (nb1-nb2)

def division(nb1,nb2):
    """
    Division.
        nb1 est le 1er nb
        nb2 est le 2nd nb
    """
    print("div: ",nb1/nb2)
    return (nb1/nb2)

def multiplication(nb1,nb2):
    """
    Multiplication.
        nb1 est le 1er nb
        nb2 est le 2nd nb
    """
    print("mul: ",nb1*nb2)
    return (nb1*nb2)

def choix():
    """
      choix des opérations arithmétiques.
       + - / *
    """

    op=input("donner une opération + - / *:")
    liste = ['m', 'd', 's', 'a']

    #match liste:
    match op:
      case "*":
        (nb1,nb2)=saisir()
        multiplication(nb1,nb2)
        #return "multiplication"
      case "/":
        (nb1,nb2)=saisir()
        division(nb1,nb2)
        #return "division"
      case "+":
        (nb1,nb2)=saisir()
        addition(nb1,nb2)
        #return "addition"
      case "-":
        (nb1,nb2)=saisir()
        substraction(nb1,nb2)
        #return "substraction"
      case _:
        return "nop"




def calc():
  """
  fonction principale
  """
  while True:
    print (choix())


if __name__ == "__main__":
       calc()
