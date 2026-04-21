#EJERCICIO 1 — Mini OAuth Server (100% POO)
#Implementar un OAuth Server simplificado que:

#autentique usuarios
#emita JWT
#valide tokens
#use headers, query params y body params
#tenga configuración desacoplada
# Requisitos obligatorios

#Tenés que implementar estas clases (sí o sí):

#1. OAuthConfig

#Debe contener:

#client_id
#client_secret
#token_expiration
#jwt_secret
#encryption_key
#2. EncryptionService

#Debe:

#cifrar y descifrar strings
#podés usar hashlib o algo simple (no hace falta algo militar)
#3. JWTService

#Debe:

#generar JWT
#validar JWT
#manejar expiración

# No uses magia: entendé qué estás firmando

#4. RequestParser

#Debe parsear una request simulada:

#request = {
#    "headers": {...},
#    "query_params": {...},
#    "body": {...}
#}

#Debe tener métodos:

#get_header(name)
#get_query_param(name)
#get_body_param(name)
#5. OAuthHandler

#Debe implementar:

#authorize(request)
#token(request)
#validate_token(request)
#6. OAuthServer

#Debe:

#recibir requests
#delegar al handler
#simular endpoints:
#/authorize
#/token
#/protected
# Funcionalidad mínima
#1. /authorize
#recibe client_id (query param)
#valida contra config
#devuelve un authorization_code
#2. /token
#recibe:
#client_id
#client_secret
#code
#devuelve un JWT
#3. /protected
#recibe header:
#Authorization: Bearer <token>
#valida JWT
#devuelve datos protegidos

#Restricciones
#TODO con clases (nada procedural suelto)
#no frameworks (ni FastAPI)
#sin copiar librerías completas de OAuth
#tenés que usar:
#headers
#query params
#body params