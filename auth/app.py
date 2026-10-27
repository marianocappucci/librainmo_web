"""Backend de acceso a /docs/ para la landing de LibraInmo -- config sobre
libra_web_kit.docs_auth.

`verify_path` es `/auth/verify`: LibraInmo monta su auth con
`libraauth.session_auth` (`incluir_verify=True` en `app/routers/auth.py`),
como LibraClub, Gestiolibra, MedLibra y VentaLibra.
"""
from libra_web_kit.docs_auth import DocsLoginTheme, build_docs_login_app

app = build_docs_login_app(
    product_name="LibraInmo",
    apex_domain_default="librainmo.com.ar",
    secret_key_env="DOCS_SESSION_SECRET",
    secret_key_default="librainmo-docs-secret-change-me",
    verify_path="/auth/verify",
    slug_placeholder="tu-inmobiliaria",
    # El tono oscuro del lima de la identidad (libra-ui ADR-096): el lima con
    # letra blanca no llega a 4.5:1, igual que en el botón de la app.
    theme=DocsLoginTheme(accent="#4d7c0f", accent_hover="#365314"),
)
