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
    
    def authorize(self):
        # TODO: Endpoint /authorize
        # 1. Parsear request con RequestParser
        # 2. Extraer client_id de query_params
        # 3. Validar que client_id coincida con config.client_id
        # 4. Generar authorization_code
        # 5. Guardar authorization_code
        # Retornar: {"authorization_code": "..."}
        print("TODO: OAuthHandler.authorize - Implementar flujo authorize")
        #todavia no pongo logica real, solo un placeholder para probar el endpoint
        return None
    
    def token(self, client_id:str , client_secret:str, code:str):
        # TODO: Endpoint /token
        # 1. Parsear request con RequestParser
        # 2. Extraer client_id, client_secret, code del body
        # 3. Validar client_id y client_secret contra config
        # 4. Validar que code exista y sea válido
        # 5. Generar JWT con jwt_service
        # 6. Limpiar authorization_code usado
        # Retornar: {"access_token": "...", "token_type": "Bearer"}
        """
           recibir credenciales → validar → generar token → devolverlo
        """

        if client_id != self.config.client_id:
            raise ValueError("client_id inválido")
        
        if client_secret != self.config.client_secret:
            raise ValueError("client_secret inválido")

        if not hasattr(self, "authorization_codes"):
            raise ValueError("No hay códigos almacenados")   
        
        #recibir code
        code = self.authorize(client_id,client_secret)
        if not code or code != code:
            raise ValueError("authorization_code inválido o expirado")
        
        stored_code = self.authorization_codes.get(code)
        if not stored_code:
            raise ValueError("authorization_code inválido o expirado")
        
        #. Marcar code como usado (one-time use)
        stored_code["used"] = True
        # crear payload
        payload = {
            "client_id": client_id,
            "exp": 9999999999,  # placeholder de expiración
        }

        token = self.jwt_service.generate_token(payload)
        if not token:
            raise ValueError("Error al generar token")


        print(f"token generado exitosamente: {token}")
        
        return {"access_token": token, "token_type": "Bearer"}
    
    def validate_token(self ):
        # TODO: Endpoint /protected
        # 1. Parsear request con RequestParser
        # 2. Extraer token del header "Authorization: Bearer <token>"
        # 3. Validar token con jwt_service
        # 4. Extraer client_id del token
        # Retornar: {"valid": True/False, "client_id": "..."}
        print("TODO: OAuthHandler.validate_token - Implementar validación")
        return None


