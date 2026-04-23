import datetime


"""
  configuración
"""
class OAuthConfig:
  def __init__(self, client_id, client_secret, token_endpoint, jwt_secret, encryption_key):
    # identificador del cliente(la app,el frontend,otra api)
    self.client_id = client_id
    # secreto compartido para autenticar al cliente en question(no usuario,sino la app que hace la petición)
    self.client_secret = client_secret
    # endpoint para obtener el token (en este ejercicio no lo usaremos realmente, 
    # pero en un caso real sería la URL del servidor de autenticación)
    self.token_endpoint = token_endpoint  
    # clave secreta para firmar los tokens JWT (en un caso real, 
    # esto debe ser un valor seguro y no compartido públicamente)
    self.jwt_secret = jwt_secret
    # clave para cifrar datos sensibles (en un caso real, esto también debe ser seguro)
    self.encryption_key = encryption_key
    # tiempo en segundos, de expiración del token actual (en un caso real, esto se calcularía al generar el token)
    self.token_expiration_time = None  
  


  def validate(self):
    if not self.client_id:
      raise ValueError("client_id is required")
    if not self.client_secret:
      raise ValueError("client_secret is required")
    if not self.token_endpoint:
      raise ValueError("token_endpoint is required")
    if not self.jwt_secret:
      raise ValueError("jwt_secret is required")
    if not self.encryption_key:
      raise ValueError("encryption_key is required")


  def token_expiration_seconds(self, token_expiration_time):
    """ Calcula los segundos restantes hasta la expiracion del token """
    if not token_expiration_time:
      return None
    
    # timestamp actual en segundos
    now = datetime.datetime.now().timestamp()
    
    # si la expiración es menor que ahora, ya expiró
    if token_expiration_time < now:
      print("Token ya expiró")
      return 0
    
    # calcular segundos restantes
    seconds_left = token_expiration_time - now
    print(f"Token expira en {seconds_left:.2f} segundos")
    return seconds_left
     

  def set_token_expiration(self, expires_in):
    """Guarda el timestamp de expiración basado en segundos desde ahora"""
    self.token_expiration_time = datetime.datetime.now().timestamp() + expires_in   
