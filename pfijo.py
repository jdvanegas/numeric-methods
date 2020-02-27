#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Compendio de programas.
# Matemáticas para Ingeniería. Métodos numéricos con Python.
# Copyright (C) 2020 Los autores del texto.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
# ---------------------------------------------------------------------

# Implementación del método del punto fijo y algunos casos de salida.

from math import *


def pote(x):  # retorna $pote(x)=2^{-x}$
    return pow(2, -x)


def pol(x):  # retorna $pol(x)=\frac{x^2-1}{3}$
    return (x**2-1)/3


def puntofijo(f, p0, tol, n):  # Método del punto fijo
    i = 1
    while i <= n:
        p = (f(p0))
        print("Iter = {0:<2}, p = {1:.16f}".format(i, p))
        if abs(p-p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return

# $pol(x)$, $p_0=0.9$, $Tol=10^{-10}$, $N_0=100$
print ("\n"+r"-- Punto fijo funci\'on pol(x):"+"\n")
puntofijo(pol, 0.9, 1e-10, 100)

# $pote(x)$, $p_0=0.5$, $Tol=10^{-8}$, $N_0=100$
print ("\n"+r"-- Punto fijo funci\'on pote(x):"+"\n")
puntofijo(pote, 0.5, 1e-8, 100)
