# Guess the Number

## Índice

* [1. Resumen del proyecto](#1-resumen-del-proyecto)
* [2. Funcionalidades](#2-funcionalidades)
* [3. Hitos](#3-hitos)

***

## 1. Resumen del proyecto

Hoy en día, las aplicaciones web son nuestras compañeras constantes. Desde mantenernos conectados en redes sociales hasta facilitarnos el trabajo, están presentes en cada momento. Pero lo que hace que este momento sea realmente emocionante es que estas herramientas no solo nos acompañan, ¡sino que también nos abren las puertas a un mundo fascinante: la interacción con inteligencia artificial!

Por eso, hemos creado una página dinámica llamada Flores Dataverse-chat, que nos permite interactuar con la inteligencia artificial, especificamente la de OpenAI. Esta plataforma nos permite interactuar con las flores, mediante un chat y podemos preguntarles por sus características, habitat, origen, descripción, entre otros detalles

![imagen-chat](src/assets/images/imagen-chat.png)

## 2. Funcionalidades

En este proyecto hemos convertido nuestro Dateverse en SPA (single page aplication), implementado un router que nos permite navegar por las diferentes rutas de la página. También se a implementado el chat que tiene conexión con la API de OpenAI y nos da la posibilidad de interactuar con la inteligencia artificial y consultar información detallada de cada flor. Además de eso, hemos manteniendo las funcionalidades de visualizar, filtrar, ordenar y calcular estadísticas.

![imagen-chat-openAI](src/assets/images/imagen-chat-openai.png)

![implementacion-rutas](src/assets/images/implementación-rutas.png)

Nuestro proyecto cuenta también con una vista que permite integrar una API KEY de OpenAI que permite la interacción con nuestras flores.

![vista-api](src/assets/images/vista-api.png)

## 3. Hitos

### Hito 1

1. Preparamos el área de trabajo: hicimos fork, clonamos proyecto e instalamos dependencias.
2. Organizamos información.
3. Implementamos router, con las funciones setRootEl, setRoutes, renderView y onURLChange. Responsables para las vistas dinámicas de la página.

### Hito 2

1. Migramos los datos de Dataverse-chat y logramos traer a la nueva página las funcionalidades como filtros, estadísticas, etc.
2. Reutilizamos las funciones de Dataverse que permiten aplicar los filtros y cambiar las estadísticas.
3. Migramos también las pruebas unitarias de las funciones de Dataverse.
4. Visualizamos el set de datos en home.js.

![vista-home](src/assets/images/vista-home.png)

### Hito 3

1. Logramos almacenar de forma segura la API que nos permite conectar de manera efectiva a la API de OpenAI, para esto integramos las funciones getApiKey y SetApiKey.
2. Realizamos test para las funciones getApiKey y SetApiKey.
3. Diseñamos la vista de chat individual y la integramos con OpenAI.
4. Integramos a OpenAI utilizando promesas, fetch, then y catch.
5. Escribimos los test para las funciones asíncronas.

![gif-interfaz](src/assets/images/video-dataverse-chat.gif)