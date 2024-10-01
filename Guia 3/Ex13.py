"""    
Recordar que el vecindario de un vértice v es el conjunto N(v) que contiene a todos los vértices
adyacentes a v. El vecindario cerrado es N[v] = N(v) ∪ {v}. Dos vértices u y v son gemelos
cuando N(u) = N(v), mientras que son mellizos cuando N[u] = N[v] (Figura 2). 
"""

"""
a) Observar que las relaciones de gemelos y mellizos son relaciones de equivalencia (i.e., son
reflexivas, transitivas y simétricas).    

Para que dos vertices sean gemelos, todos sus vecinos tienen que ser iguales. 
Pero hay que tener en cuenta que en N(u) no esta incluido u, igual con N(v) y v

Entonces, digamos que tenemos dos vertices u y v, donde N(u) == N(v)
Eso requiere que, tengan el mismo vecindario. Si esto es asi, entre los 2 no son vecinos.
! Tener en cuenta que esto es asi si no puede ser vecino de si mismo (pseudografo)

Ahora veamos el caso de N[u] == N[v] mellisos Esto nos agrega a u y v a sus respectivos vecindarios.
Para que se cumplan ambas cosas a la vez, u tendria que estar en N[v] y v en N[u]. 
Pero como dijimos v y u no pueden ser vecinos.

Si v != u y se cumplen las relaciones se llega a absurdo, 

Por ende esto solo se cumple cuando v == u.
"""

"""
Probar que el siguiente algoritmo encuentra la partición de V (G) en vértices mellizos. Ayu-
da: demostrar por invariante que, luego del paso i, u y w pertenecen al mismo conjunto de
Pi si y sólo si N[u] ∩{v1,...,vi}= N[w] ∩{v1,...,vi}.
1. Sea P0 = {V (G)} (P es un conjunto de conjuntos)
2. Sea v1,...,vn un ordenamiento cualquiera de V (G).
3. Para i desde 1 hasta n:
4. Poner Pi := {W ∩N[vi] | W ∈Pi−1} ∪ {W \N[vi] | W ∈Pi−1}.
5. Pn es la partición buscada


Veamos un poco lo que nos plantea el problema. 
El algoritmo encuentra la particion de vertices en vertices mellizos
1. Inicializa con una particion P_0 que sea todos los vectores. P[0] == V(G)
2. Se explica solo en enunciado
3. for (i = 1; i<n; n++){
    P_i= 
}

! No termino de comprender la 4rta linea, W de donde sale y que representa. Es un universal? que es?

"""
