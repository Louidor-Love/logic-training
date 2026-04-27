"""
    POST /token
    GET /authorize
    GET /protected
    Maneja:
    rutas
    entrada de requests
    conexión con “el mundo externo”

"""
from .OAuthConfig import OAuthConfig
from .OAuthHandler import OAuthHandler
import requests


class OAuthServer:
    def __init__ (self, config: OAuthConfig, handler: OAuthHandler):
        self.config = config
        self.handler = handler

        print("OAuthServer - Configurado con URL:", self.url)
      

    def create_token(self, request: dict):
        """
        recibir credenciales → validar → generar token → devolverlo
        Simula una petición al endpoint /token
        """

        # 🔹 1. Extraer datos del request
        body = request.get("body", {})
        headers = request.get("headers", {})
        query = request.get("query", {})

        client_id = body.get("client_id") or query.get("client_id")
        client_secret = body.get("client_secret") or query.get("client_secret")

        # 2. Validar datos básicos
        if not client_id or not client_secret:
            return {
                "error": "invalid_request",
                "message": "client_id y client_secret son requeridos"
            }

        # 3. Delegar al handler
        try:
            token_response = self.handler.token(request)

        except Exception as e:
            return {
                "error": "invalid_client",
                "message": str(e)
            }

        #  4. Construir respuesta
        return token_response

    def authorize(self, requests):
        pass

    def protected(self, requests):
        pass


