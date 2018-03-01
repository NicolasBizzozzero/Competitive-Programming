#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:23:39 2018

@author: meadriss
"""
from parser import Ride, read

def nearestClient( pos, clients):
    sortie = sorted(clients, key = lambda c: c.distance_totale(pos))
    return sortie
      

#F, rides, T, B= read("instances/a_example.in") 

#print("la liste trié")
#print(nearestClient(1,2,rides,0,T))
    
    