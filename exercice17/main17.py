# ============================================
# EJERCICIO 17: Mini OAuth Server (100% POO)
# ============================================

class OAuthConfig:
    """
    Configuración centralizada del servidor OAuth
    """
    def __init__(self):
        # TODO: Implementar atributos
        # - client_id
        # - client_secret
        # - token_expiration (segundos)
        # - jwt_secret (para firmar tokens)
        # - encryption_key (para cifrar datos)
        print("TODO: OAuthConfig - Implementar configuración")


class EncryptionService:
    """
    Servicio para cifrar y descifrar strings
    Puede usar hashlib o simple encryption
    """
    def __init__(self, encryption_key):
        # TODO: Guardar encryption_key
        print("TODO: EncryptionService - Guardar clave de encriptación")
    
    def encrypt(self, data):
        # TODO: Cifrar data con encryption_key
        # Retornar: string cifrado
        print(f"TODO: EncryptionService.encrypt - Cifrar: {data}")
        return None
    
    def decrypt(self, encrypted_data):
        # TODO: Descifrar encrypted_data
        # Retornar: string descifrado
        print(f"TODO: EncryptionService.decrypt - Descifrar: {encrypted_data}")
        return None


class JWTService:
    """
    Servicio para generar y validar JWT
    No uses librerías de JWT, implementalo manual
    """
    def __init__(self, jwt_secret, token_expiration):
        # TODO: Guardar jwt_secret y token_expiration
        print("TODO: JWTService - Guardar secret y expiration")
    
    def generate_token(self, client_id):
        # TODO: Crear JWT con:
        # - header: {"alg": "HS256", "typ": "JWT"}
        # - payload: {"client_id": client_id, "exp": timestamp}
        # - signature: HMAC(header.payload, jwt_secret)
        # Retornar: "header.payload.signature"
        print(f"TODO: JWTService.generate_token - Generar JWT para {client_id}")
        return None
    
    def validate_token(self, token):
        # TODO: Validar JWT:
        # - Verificar firma
        # - Verificar que no esté expirado
        # - Extraer payload
        # Retornar: True/False
        print(f"TODO: JWTService.validate_token - Validar {token}")
        return False


class RequestParser:
    """
    Parser para simular requests HTTP con:
    - headers
    - query_params
    - body
    """
    def __init__(self, request):
        # TODO: Guardar request
        # request = {
        #     "headers": {...},
        #     "query_params": {...},
        #     "body": {...}
        # }
        print("TODO: RequestParser - Guardar estructura de request")
    
    def get_header(self, name):
        # TODO: Retornar valor del header 'name'
        # Si no existe, retornar None
        print(f"TODO: RequestParser.get_header - Buscar header: {name}")
        return None
    
    def get_query_param(self, name):
        # TODO: Retornar valor del query param 'name'
        # Si no existe, retornar None
        print(f"TODO: RequestParser.get_query_param - Buscar param: {name}")
        return None
    
    def get_body_param(self, name):
        # TODO: Retornar valor del body param 'name'
        # Si no existe, retornar None
        print(f"TODO: RequestParser.get_body_param - Buscar body: {name}")
        return None


class OAuthHandler:
    """
    Handler que maneja los 3 endpoints OAuth
    """
    def __init__(self, config, jwt_service, encryption_service):
        # TODO: Guardar config, jwt_service, encryption_service
        # Guardar também authorization_codes generados
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


class OAuthServer:
    """
    Servidor que orquesta todo
    Recibe requests y delega al handler
    """
    def __init__(self, config, handler):
        # TODO: Guardar config y handler
        print("TODO: OAuthServer - Guardar config y handler")
    
    def handle_request(self, endpoint, request):
        # TODO: Recibir endpoint (/authorize, /token, /protected)
        # Delegar al handler según el endpoint
        # Retornar respuesta
        # 
        # if endpoint == "/authorize":
        #     return self.handler.authorize(request)
        # elif endpoint == "/token":
        #     return self.handler.token(request)
        # elif endpoint == "/protected":
        #     return self.handler.validate_token(request)
        
        print(f"TODO: OAuthServer.handle_request - Procesar endpoint {endpoint}")
        return None


# ============================================
# EJEMPLO DE USO (CUANDO ESTÉ IMPLEMENTADO)
# ============================================
if __name__ == "__main__":
    # config = OAuthConfig()
    # jwt_service = JWTService(config.jwt_secret, config.token_expiration)
    # encryption_service = EncryptionService(config.encryption_key)
    # handler = OAuthHandler(config, jwt_service, encryption_service)
    # server = OAuthServer(config, handler)
    # 
    # request = {
    #     "headers": {"Authorization": "Bearer token123"},
    #     "query_params": {"client_id": "client_123"},
    #     "body": {"client_secret": "secret_456"}
    # }
    # 
    # response = server.handle_request("/authorize", request)
    # print(response)
    
    print("Clases definidas. Implementa la lógica en cada TODO.")

import tkinter as tk
from login_gui import LoginGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()