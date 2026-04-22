from OAuthConfig import OAuthConfig


"""
  configuración
"""
class OAuthConfig:
  def __init__(self, client_id, client_secret, token_endpoint, jwt_secret, encryption_key, redirect_uri):
    self.client_id = client_id
    self.client_secret = client_secret
    self.token_endpoint = token_endpoint
    self.jwt_secret = jwt_secret
    self.encryption_key = encryption_key
    self.redirect_uri = redirect_uri


  def cifrar(self, data):
    # Lógica de cifrado
    pass

  def descifrar(self, data):
    # Lógica de descifrado
    pass


  def generar_jwt(self, payload):   
    # Lógica de generación de JWT
    pass

  def validar_jwt(self, token):
    # Lógica de validación de JWT
    pass

  def manage_expiration(self, token):
    # Lógica de manejo de expiración
    pass

   