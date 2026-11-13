# prueba-estadistica

Tablero de solicitudes con datos ficticios. Edita `datos.json` en la raíz para actualizar la fuente.

El flujo **Publicar tablero** se ejecuta al subir cambios a `main` y también se puede iniciar desde la pestaña **Actions**. Python multiplica `recibidas` y `resueltas` por 10 y genera el JSON que consume el tablero publicado. La fuente conserva los conteos originales. En **Settings → Pages → Source**, selecciona **GitHub Actions**.

Para probar la versión publicada localmente, ejecuta estos comandos desde la raíz del repositorio.

```sh
python scripts/escalar_datos.py
python -m http.server 8765 --directory _site
```

Abre `http://localhost:8765/` para ver el tablero con los datos escalados.
