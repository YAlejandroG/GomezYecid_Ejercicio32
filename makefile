onda.png : Ejercicio32.py onda.dat
	python Ejercicio32.py

onda.dat : Ejercicio32.x
	./Ejercicio32.x 

Ejercicio32.x : Ejercicio32.cpp
	c++ Ejercicio32.cpp -o Ejercicio32.x
	
clean : 
	rm Ejercicio32.x onda.dat onda.png 
