# Modelos de aprendizaje

Se presentan dos tipos de modelos de aprendizaje:

1. Modelos generativos: Para generar texto y aprovecharlo en los bots de comunicación
2. Modelos clasifiadores: Para aprovecharlo en tareas dicotomicas.

Este texto se presenta como un pre-proyecto que muestra los objetivos de los modelos y algunos modelos de acceso abierto y de paga, junto con algunos de los requisitos necesarios para implementar los modelos. 

## Introudcción

Los modelos de aprendizaje maquina son un conjunto de técnicas y algoritmos que buscan obtener conocimiento a partir de los datos. El aprendizaje máquina tiene muchas áreas de estudio y puede ser dirigido a cualquier tipo de datos lo que ha genearodo una serie de sub-areas como el aprendizaje profundo. 

Actualmente los modelos generativos, como ChatGPT, gemini o llama, se han popularizado de tal forma que todas las compañias buscan implementar modelos de inteligencia artificial para mejorar las interacciones con el usuario. Sin embargo, los libros especializados recomiendan el uso de modelos de aprendizaje en tareas repetitivas que puedan presentar patrones y de las cuales exista una gran cantidad de ejemplos que permita recuperar información.

### Modelos generativos

Los modelos generativos, como su nombre lo indica, son modelos que buscan generar nueva información a partir de ejemplos anteriores. Los modelos generativos pueden ser entrenados para generar: imágenes, audio, video o texto y pueden ser aplicados en un sin fin de tareas. 

Para nuestros fines buscamos modelos generativos de lenguaje de gran tamaño (Large Languaje Models, por sus siglas en ingles), algunos de los modelos más populares que contienen parte en españon:

1. Llama
2. Flor
3. Google Bert
4. GPT-NeoX
5. Alpaca-LoRA
6. Bing-GPT
7. Edge-GPT

### Modelos de clasificación

Los modelos de clasificación aprovechan algoritmos para clasificar en conjuntos a partir de los datos, un ejemplo típico de modelos de clasificación es el K-NN. Sin embargo, los modelos de clasificación pueden ir más allá si se sabe definir el problema para que la solución sea dicotómica. Por ejemplo, se puede entrenar un modelo de clasificación que busque detectar el cáncer sobre un conjunto de imágenes. Una vez entrenado, el modelo tendrá la tarea de clasificar si la imagen de entrada tiene, o no, cancer.

Estos modelos pueden ser simples, como un K-NN o complejos como una red neuronal. Algunos modelos de clasificación de imágenes son:

1. GANs
2. MobileNet
3. Trasnformers
4. PerceptronMulticapa

## Requisitos

Para ambos modelos los requisitos son similares, la ejecución de cada uno será la diferencia principal. Para ambos modelos es necesario contar con un servidor que ejecute el modelo y permita, de algua forma, consumir las respuestas generadas, además de poder alimnetarlo con neuvos ejemplos. 

Para el modelo generativo, es necesario 1) seleccionar el mejor modelo 2) decir si se quiere contratar o si se quiere montar de forma local. En el primer caso uno debe ocuparse de integrar el modelo generativo junto con la aplicación que se va a alimentar. En el segundo caso, primero se debe crear un entorno de desarrollo, instalar el modelo  y ejecutarlo de forma continua. La decisión dependerá del costo, por un lado del costo de renta y por otro lado del consto de mantenimiento, 

Para el modelo de clasificación es un poco más complejo, pues no existe un modelo que este implementado para el fin particular. Por lo que es necesario elegir un par de modelos, obtener un gran conjunto de datos de entrenamiento etiquetados, entrenar los modelos y evaluar el desempeño a fin de elegir un modelo con el que se quiera trabajar. Después de ello, es necesario dejar corriendo el modelo entrenado para ser consumido después por la aplicación.
