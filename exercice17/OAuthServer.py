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


        # validar que existen los parámetros necesarios
        if not client_id or not redirect_uri or not response_type:
            return{
                "error": "invalid_request",
                "message": "client_id, redirect_uri y response_type son requeridos"
            }
        
        # solo acepto code como response_type
        if response_type != "code":
            return {
                "error": "unsupported_response_type",
                "message": "Only 'code' is accepted as response_type"           
           }
        
        try:
            auth_response = self.handler.authorize(client_id, redirect_uri, response_type)
        except Exception as e:
            return{
                "error": "invalid_client", 
                "message": str(e)
            } 
           
        code = {
            "code": auth_response
        }

        return code
    

    def protected(self, request: dict):
        """ Maneja el endpoint protegido (GET /protected)
            validar token y devolver recurso protegido
        """
        headers = request.get("headers", {})

        auth_header = headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return {
                "error" : "invalid_header",
                "message": "Authorization header debe existir yempezar con 'Bearer '"
            }
        
        token = headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return {
                "error" : "missing_token",
                "message": "token requerido"
            }

        try:
            protected_data = self.handler.protected(token)
        except Exception as e:
            return {
                "error": "invalid_token",
                "message": str(e)
            }    
        
        protected_data = {
            "data": protected_data
        }

        return protected_data


