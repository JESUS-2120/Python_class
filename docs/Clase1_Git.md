# Clase 1: Introduccion a Git y GitHub

### Para que desarrollamos software?

* Resolver problemas
* Que nuestro codigo lo podamos compartir
* Software facil de entender por los demas y que lo pueda modificar despues
* Principal Objetivo: colaborar con mas gente

### Como lo logramos?

* Seguir el estandar para codificar, PEP8 para python, guias de estilo en google
* Notaciones o estandares para nombrado (CamelCase o Upper case)
* Tener encabezado del programa que indique para que sirve, como se ejecuta, etc.
* Tener documentacion interna, mini descripcion de funciones por ejemplo
* Correcto nombrado de los programas
* Definir estructura de directorios y definir un repositorio para guardar
* Tener la vision de un externo acerca de nuestro codigo
* Manejo de versiones, tanto del codigo como de la documentacion

### Controlador de versiones

Versionamiento de **forma manual:** 2 cifras, enteros cambios mayores y el decimal incluye los cambios menores. Ej: myScript_v0.1.py

Versionamiento **automatico:** sistema de control de versiones, controlador de versiones automatizado, manejan archivos de texto plano (no binarios, word, etc.) apoyan en los cambios. Ej: git, mercury. 

Con un **controlador de versiones** es como un Ctrl Z ilimitado, nos permite organizar el trabajo colaborativo tambien. 

### Por que Git?

1. Muy popular, ayuda a manejar nuestros archivos
2. Actualmente muchas comunidades ayudan a su desarrollo

### Como trabajar con Git

**Local:** mi codigo esta en mi maquina, solo yo lo puedo usar

**+GitHub:**codigo disponible para mas personas, en linea, trabajo en conjunto en el entorno web de GitHub. Mucha retroalimentacion

### Trabajo en Git

#### 1. Configurar Git

Para saber si git esta instalado en la maquina ` git --version` en Linux. 

Para configurar Git, esto es necesario para que git sepa quien hace los cambios: para configurar el correo que luego se vincula a github y tambien configurar el nombre de usuario

```
git config --global user.name "tuNombre"  

git config --global user.email "tuCorreo" 
```

Para ver variables en git como el mail y el username `git config --list`

#### 2. Esquema de trabajo de Git

Git tiene 3 escenarios: el repositorio en nuestra compu, ambiente oculto que git crea para gestionar las modificaciones un **area de preparacion** "replicas temporales" `git add`. Ya para conservar la modificacion, **repositorio de Git**, la parte final es algo a lo que ya podemos acceder `git commit`. 

#### 3. Crear repositorios controlados por Git

1. Ubicar sitio de ruta corta en la compu y definir la ruta de trabajo
2. Crear una carpeta
3. Entrar a la carpeta y crear la estructura interna
4. Inicializar el repositorio Git `git init`
5. Revisar que el repositorio si esta `ls -la`
6. Comprobar el estado del repositorio `git status`

**Buenas practias:**docs para texto, libs para librerias, src source para almacenar codigo fuente y test para hacer pruebas de programas o pasar datos externos. 

Git no controla carpetas, controla archivos. No es adecuado tener repositorios anidados, git controla desde una raiz y controla lo que esta dentro, de ahi ya no se tiene que volver a inicializar repositorio, etc. Piensalo como **controlar en cascada**.

### Ejercicio...

Descarga de cursos la carpeta de git y descomprimela para sacar los archivos. 

Le decimos a git que queremos que controle el archivo X.py para ello empleamos `git add`, esto le dira a git que gestione los cambios de este documento. 

Es necesario que pongas un mensaje claro cada que hagas commit, debe indicar que accion ejecutamos para saber las modificaciones de la version por si luego lo queremos recuperar `git commit -m "mensaje que contiene la mini descripcion"`; opcion de -m significa mensaje corto y -a para un mensaje largo. Aqui ya pasamos por las 3 fases del funcionamiento de git.

**Recuerda que siempre es primero `git add` y posterior `git commit` **

Es importante hacer add cada que queremos guardar una modificacion, consolidamos cambios con commit. 