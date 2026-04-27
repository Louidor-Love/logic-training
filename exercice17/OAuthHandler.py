"""
  manipulador de solicitudes OAuth / lógica de negocio
"""
from .OAuthConfig import OAuthConfig


class OAuthHandler:
    """
    Handler que maneja los 3 endpoints OAuth
    """
    def __init__(self, config: OAuthConfig, jwt_service, encryption_service):
        self.config = config
        self.jwt_service = jwt_service
        self.encryption_service = encryption_service
     
        print("TODO: OAuthHandler - Guardar servicios y config")
    
    def authorize(self, request):
        # TODO: Endpoint /authorize
        # 1. Parsear request con RequestParser
        # 2. Extraer client_id de query_params
        # 3. Validar que client_id coincida con config.client_id
        # 4. Generar authorization_code
        # 5. Guardar authorization_code
        # Retornar: {"authorization_code": "..."}
        print("TODO: OAuthHandler.authorize - Implementar flujo authorize")
        return None
    
    def token(self, request):
        # TODO: Endpoint /token
        # 1. Parsear request con RequestParser
        # 2. Extraer client_id, client_secret, code del body
        # 3. Validar client_id y client_secret contra config
        # 4. Validar que code exista y sea válido
        # 5. Generar JWT con jwt_service
        # 6. Limpiar authorization_code usado
        # Retornar: {"access_token": "...", "token_type": "Bearer"}
        print("TODO: OAuthHandler.token - Implementar flujo token")
        return None
    
    def validate_token(self, request):
        # TODO: Endpoint /protected
        # 1. Parsear request con RequestParser
        # 2. Extraer token del header "Authorization: Bearer <token>"
        # 3. Validar token con jwt_service
        # 4. Extraer client_id del token
        # Retornar: {"valid": True/False, "client_id": "..."}
        print("TODO: OAuthHandler.validate_token - Implementar validación")
        return None


