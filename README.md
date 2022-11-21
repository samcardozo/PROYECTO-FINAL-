# Proyecto final: REBELS, juego de Palabras Rápidas
Proyecto final algoritmos y programación 
# INTRODUCCION
A medida que crecemos vamos afianzando nuestras capacidades cognitivas, pero también las vamos perdiendo, bien sea por la edad, por enfermedad o simplemente por falta de entrenamiento.
Adiestrar la mente, es tan importante como mantener el cuerpo saludable mediante ejercicio, es necesario ejercitar nuestra mente y afianzar la agilidad de pensamiento para evitar o reducir el riesgo de deterioro cognitivo o de enfermedades como pérdida de memoria y Alzheimer. Igualmente, para los pequeños que inician su aprendizaje, el entrenamiento del cerebro los prepara para perfeccionar alguno o varios de sus procesos mentales para su vida de adolescentes, jóvenes y adultos. 
Este proyecto final, busca ofrecer una manera divertida y entretenida para ejercitar la mente, tanto para niños, jóvenes o adultos mayores, permitiendo a través de Rebels - Palabras Rápidas, reforzar la memoria y la agilidad mental, mediante el conocimiento y la concentración.
El juego se desarrolló con bajo el editor de código Visual Studio Code y el lenguaje de programación Python, mediante el uso de librerías de Pygame, string, random y Sys.
# REBELS - Palabras rápidas
Este juego está diseñado para entrenar de una manera divertida, la agilidad mental y el conocimiento, desafiando a los jugadores a buscar palabras que contengan las letras que se le disponen de manera aleatoria, así el jugador tiene la posibilidad de encontrar palabras que incluyan dichas letras, sin importar el orden donde se presenten. El juego tiene tres niveles de dificultad, que dependen del puntaje, el primero le proporciona al jugador una letra, el segundo dos letras y el tercero tres letras; asimismo contará con tres vidas que le dan la posibilidad de realizarlo en tres intentos, aumentando la puntuación obtenida. Entre más rápido se adivine la palabra y menos intentos utilice, mejor será el entrenamiento y la diversión. 
El juego afianza la capacidad de concentración, de lenguaje, de comunicación, y la estimulación cognitiva.
# Programas usados
•	Visual Studio Code (VS Code 1.73): es el editor de código fuente más popular, por su optimo uso y agilidad para el desarrollo de proyectos; es multiplataforma, ya que se encuentra disponible para Windows, macOS y Linux. Fue desarrollado por Microsoft, para ser ejecutable en el escritorio, mediante el uso de innumerables extensiones que permiten escribir, depurar y ejecutar código en diversos lenguajes de programación. 

![image](https://user-images.githubusercontent.com/114431024/202961419-48ca8486-dd72-4668-bad1-ba8296cb1f7b.png)

Entre sus principales características están:
a.	La intelliSense, que permite editar código, así como autocompletar y resaltar la sintaxis, incluso de manera personalizada.
b.	La depuración que permite encontrar errores en el código rápidamente antes de la ejecución de este.
c.	Las extensiones (para C++, C#, Java, Python, PHP, Go, .NET), ayudan a personalizar y crear funciones adicionales, sin afectar el rendimiento del editor y mejorando la experiencia.
d.	El soporte integrado, para JavaScript, TypeScript y Node.js

•	Python: es un lenguaje de programación de código abierto, multiplataforma, versátil y fácil de aprender y usar por los desarrolladores; solo requiere un sistema operativo actualizado, un editor de código y un buen smartphone, computador o Tablet. Su uso es muy amplio, sirve para scripting y automatización, para desarrollo de software, para análisis de datos, machine learning e inteligencia artificial, blockchain, desarrollo de video juegos, desarrollo web, entre otros.

![image](https://user-images.githubusercontent.com/114431024/202961803-b888c8d6-15c6-4dd1-abbb-1dbdf7b8451c.png)

Características:
a.	Sintaxis básica
b.	Productivo, ya que permite programar con menos líneas de código.
c.	Biblioteca estándar con códigos reutilizables.
d.	Compatible con lenguajes de programación como Java, C y C++.

# Código de REBELS - Palabras Rápidas.
Para la creación de REBELS, se utilizaron las siguientes librerías: 
•	Pygame: con el lenguaje de programación de Python, esta librería es utilizada para el desarrollo de videojuegos en 2D; esta basada en SDL, que permite la gestión de gráficos, imágenes, audio y periféricos.
En el desarrollo del juego, las librerías de Pygame permitieron la creación del fondo de las ventanas que se visualizan en el inicio y durante el juego.
![image](https://user-images.githubusercontent.com/114431024/202961537-c418e144-734c-41b4-940a-3554481ef836.png)

•	String o formato de cadena de caracteres personalizado: el código de REBELS, utiliza esta librería para la selección de las letras que se le dispondrán al jugador como base para los tres niveles del juego.
•	Rrandom: permite la selección aleatoria de letras, en los diferentes niveles del juego y para cada uno de los jugadores que interactúen con el.
•	Sys: librería que permitió la implementación de la ventana de juego, así como el uso del teclado/mouse.
El código generado puede consultase en el archivo denominado Proyecto.py
Figura 1. Código REBELS – Palabras Rápidas

# Interfaz
•	Inicio: la Figura 2, muestra la interfaz de inicio, la cual desctibe las instrucciones de REBELS. 

![image](https://user-images.githubusercontent.com/114431024/202960875-6d53512e-3e91-4f72-be56-c10a179aa37d.png)

Figura 2. Interfaz de inicio
•	Durante el juego, se mostrará una ventana que visualiza las letras seleccionadas arbitrariamente por REBELS, para que el jugador rápidamente ingrese la palabra que contenga dicha letra (Figura 3).

![image](https://user-images.githubusercontent.com/114431024/202960922-5b9e9df7-e725-42ca-b689-5094077face2.png)

Figura 3. Interfaz del juego activo.
•	Obtención de puntos: en cada nivel el jugador ingresará las palabras en lo posible sin agotar las tres vidas, y obteniendo el mayor puntaje posible. (Figura 4)

![image](https://user-images.githubusercontent.com/114431024/202961056-89b7a469-3fd3-42b8-ac2d-47e2ce4d1277.png)

Figura 4. Interfaz fin del juego

# Conclusiones
Durante el desarrollo del código de REBELS, lo más complicado fue conseguir separar la palabra ingresada, en una lista de letras, para validar la coincidencia entre las letras aleatorias otorgadas por REBELS y la palabra seleccionada.
Al comienzo, se pensó incluir en el juego un tipo de temporizador, sin embargo, resultó que no permitía avanzar hasta no parar el tiempo o simplemente no reducía las vidas, por lo que se optó por no implementarlo.
Otro reto fue la implementación del algoritmo con la librería pygame, ya que al ser nueva fue un reto la impresión del texto y la escritura de las palabras, lo cual se solucionó investigando más sobre la librería y probando diferentes alternativas de código, hasta lograr conseguirlo.
