# Escribe


La instrucción **Escribe** permite mostrar mensajes por pantalla.

#### Formato

```alf
Escribe [mensaje]
```

#### Características

No se parsearán caracteres especiales como `\b`, `\n`, `\t` o comillas.

Después de la ejecución del comando, una nueva línea será añadida.


#### Ejemplos

```alf
Escribe Hola Mundo
```
> Hola mundo

```alf
Escribe "Me llamo Alfred"
```
> "Me llamo Alfred"

```alf
Escribe Buenos días, Sr. Wayne.
Escribe Espero que se lo esté pasando bien.
```
> Buenos días, Sr. Wayne.

> Espero que se lo esté pasando bien.

