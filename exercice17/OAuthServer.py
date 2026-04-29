"""
    POST /token -> devuelve token (usando el code)
    GET /authorize -> devuelve code de authorización
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

        # 1. Extraer datos del request
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
            token_response = self.handler.token(client_id, client_secret)

        except Exception as e:
            return {
                "error": "invalid_client",
                "message": str(e)
            }

        #  4. Construir respuesta
        response = {
            "access_token": token_response,
            "token_type": "bearer",
        }

        return response

    def authorize(self, request: dict):
        """ Maneja la autorización (GET /authorize) 
            validar al cliente + iniciar el flujo de autorización
        """
        body = request.get("body", {})
        headers = request.get("headers", {})
        query = request.get("query", {})

        # quién está pidiendo autorización
        client_id = body.get("client_id") or query.get("client_id")
        # dónde redirigir después de autorizar
        redirect_uri = body.get("redirect_uri") or query.get("redirect_uri")
        # qué tipo de respuesta se espera (code, token, etc.)
        response_type = body.get("response_type") or query.get("response_type")

        # solo acepto code como response_type
        if response_type != "code":
            raise ValueError("Only 'code' is accepted as response_type")

        if not client_id or not redirect_uri or not response_type:
            return{
                "error": "invalid_request",
                "message": "client_id, redirect_uri y response_type son requeridos"
            }
        
        try:
            auth_response = self.handler.authorize(client_id, redirect_uri, response_type)
        except Exception as e:
            return{
                "error": "invalid_client", 
                "message": str(e)
            }    
        return auth_response

    def protected(self, requests):
        pass


