# Documentació del codi

## Observacions i aclariments previs a la correcció del codi:

Tot el codi i la documentació ha estat realitzada en equip de persones, Aarón Arenas Tomás i Marc Cervera Rosell.

A continuacó s'adjunten els enllaços als perfils de GitHub dels autors:
Aarón Arenas | Marc Cervera
------------ | ------------
https://github.com/aaron-at97 | https://github.com/marc7666

IMPORTANT: **Els errors de pylint desabilitats al llarg del codi son falsos positius de l'eina pylint**

## Fitxers i mètodes:

### Greedy recursiu:

En aquest fitxer s'ha passat a recursiu el mètode del fitxer _greedy.py_.

### Greedy iteratiu:

### Backtracking recursiu:

En aquest fitxer s'ha passat a recursiu el mètode del fitxer _backtracking.py_.

### Backtracking iteratiu:

### Dynamic programming recursiu:

En aquest fitxer s'ha passat a recursiu el mètode del fitxer _dynamic_programming.py_.

### Dynamic programming iteratiu:

### Read file:

Primera ment s’ha implementat un script anomenat ‘read_file.py’, el qual llegeix el fitxer línia a línia.

Primerament, es passa cada línia del fitxer per la funció strip() per eliminar possibles espais en blanc.

En segon lloc, s’introdueix la totalitat del fitxer a l’interior d’una llista, per així facilitar la feina posterior.

Seguidament, amb l’ajuda de la funció map() s’obtenen les variables pertanyents a les dades del problema (variables n, h, aplha, beta). Per obtenir cada valor per separat, s’empra la següent línia de codi:

n, h, alpha, beta = map(int, filtered_reader[0].split(data_separation))

La funció map, en aquest cas, converteix a enter la posició 0 del filtered_reader, posició en la qual es troben les variables en qüestió. Gràcies a la funció split(), s’obté cada valor per separat. data_separation és un paràmetre de la funció de lectura del fitxer que indica el criteri de separació a aplicar en el moment de la crida a la funció split().

Abans de retornar res, amb la mateixa estratègia, s’introdueix en una llista anomenada values les tuples (x, y) les quals representen les coordenades del terreny.

Finalment, és retorna la llista values, n, h, aplha i beta.

### Makefile:

Amb la comanda _make lint_, s'executarà l'eina pylint per a tots els fitxers de codi.

Amb la comanda _make test_, s'executaràn tots els arxius del directori de testos.

Amb la comanda _make test2_, s'execuatràn els testos més ràpids. S'ha triat aquesta via per facilitar la correcció a l'equip docent.

Amb la comanda _make all_ s'executaràn a més de tots els testos, l'eina pylint.

### arbol.py:

### calculs.py:

En obrir 
