# LibraInmo — Sitio web / landing

Landing de marketing de [LibraInmo](https://librainmo.com.ar), la administración de alquileres de la familia
Libra. Mismo patrón que `libraclub_web` y `libracargo_web`: HTML estático servido por nginx en un contenedor
Docker, con lo compartido saliendo de [`libra-web-kit`](https://github.com/marianocappucci/libra-web-kit).

## Qué se edita acá y qué no

| Archivo | Origen |
|---|---|
| `public/index.html` | **A mano**, en este repo |
| `public/img/casa-hero.jpg` | Foto del hero, aportada por el humano (la misma del fondo del login de la app) |
| `public/img/demo-*.jpg` | Capturas reales de la app con los datos ficticios de `scripts/semilla_demo.py` |
| `public/css/style.css` | **Generado** por `libra-web-kit/scripts/generate_css.py`; no editar |
| `public/img/marca.svg`, `favicon.svg` | **Generados** por `generate_favicon.py` (copias de libra-ui) |
| `public/docs/` | **Generado** por `generate_docs.py`; el contenido vive en `libra_web_kit/docs_content/librainmo/` |
| `public/legal/` | **Generado** por `generate_legal.py`, desde `libraauth.terminos` |

## Acceso a `/docs/`

`auth/` es la configuración de `libra_web_kit.docs_auth`: valida usuario y contraseña contra
`https://{subdominio}.librainmo.com.ar/auth/verify` con el secreto compartido `DOCS_AUTH_SECRET`, que tiene que
ser el mismo en el `.env` de esta landing (en el VPS) y en el de cada instancia. No hay tabla de usuarios propia.

## Deploy

`.github/workflows/deploy.yml`: un push a `main` sincroniza al VPS (`/root/librainmo_web/`) y reconstruye el
contenedor (workflow compartido `libra-web-kit/deploy-vps.yml`), que compara el `index.html` servido contra el
sincronizado. Sirve en `127.0.0.1:8106`, detrás de NPM.

## Desarrollo local

```bash
cd public && python3 -m http.server 8126
```
