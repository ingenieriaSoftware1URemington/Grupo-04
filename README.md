# Grupo-04
UserColinIdarraga - UserAlexisRios - UserDaniel

## Nombre del Proyecto 
# regressors-regressions-dataset

## Lenguaje

Python se utiliza por su fortaleza Procesamiento de datos,
Automatización de tareas, Manejo de archivos CSV y JSON,
Integración con bases de datos y APIs.
El proyecto usa Python como lenguaje de scripting, no como aplicación interactiva.

# Tipo de Proyecto
🔹Tipo: Proyecto de análisis de datos / generador de dataset

Es un script de investigación cuyo objetivo es

Descargar información histórica de bugs (Bugzilla)

Descargar información de commits

Relacionar bugs con commits que introdujeron regresiones

Exportar esa información en formatos utilizables (CSV y JSON)

# Descripción del fallo

Este proyecto no tiene un bug de lógica, pero sí tiene un punto crítico de fallo en la ejecución.

# ¿Qué fallaba?

Fallo principal:
El script depende de un repositorio externo (mozilla-central) clonado localmente y configurado con git-cinnabar.
Si esta condición no se cumple, el script falla.

En otras palabras:

El código asume que el entorno ya está preparado, pero no valida completamente que lo esté.

📍 Dónde se origina el problema:

    REPO_PATH = "mozilla-central"

📄 main.py

El script intenta acceder a esa ruta sin comprobar si existe o está configurada correctamente.

# ¿Por qué ocurre el fallo?

El proyecto necesita convertir:

hashes de commits de Mercurial

a hashes de Git

Esto solo es posible si:

el repositorio mozilla-central existe localmente

fue clonado usando git-cinnabar

está actualizado

Si cualquiera de esas condiciones falla  el script no puede continuar.

    vcs_map.mercurial_to_git(REPO_PATH, mercurial_hashes)
📄 main.py

# ¿Cómo se manifestaba el error?

Manifestación del fallo:

El script se detiene durante la ejecución

No se generan los archivos finales (dataset.csv, dataset.json)

Aparecen errores en consola

Errores típicos:

FileNotFoundError: mozilla-central

errores relacionados con git-cinnabar

fallos al mapear commits

    Mapping Mercurial commit hashes to Git commit hashes...
