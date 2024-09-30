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

Ahora veamos el caso de N[u] == N[v] Esto nos agrega a u y v a sus respectivos vecindarios.
Para que se cumplan ambas cosas a la vez, u tendria que estar en N[v] y v en N[u]. 
Pero como dijimos v y u no pueden ser vecinos.

Si v != u y se cumplen las relaciones se llega a absurdo, 

Por ende esto solo se cumple cuando v == u.
"""

"""

"""
