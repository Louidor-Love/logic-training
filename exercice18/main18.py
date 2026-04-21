#Objetivo

#Construir una API que:

#use tu OAuth Server del ejercicio 1
#tenga roles (admin/user)
#cifre datos sensibles
#use headers + params correctamente

# Nuevas clases
#1. User
#id
#username
#password (cifrado)
#role
#2. UserRepository
#guardar usuarios
#buscar por username
#3. AuthService
#login(username, password)
#usa:
#EncryptionService
#OAuthHandler
#4. ProtectedResourceHandler

#Endpoints:

#GET /profile
#GET /admin
#POST /data

#Reglas de negocio
#/profile
#requiere JWT válido
#devuelve datos del usuario
#/admin
#requiere role = admin
#si no → error 403
#/data
#recibe JSON (body)
#cifra contenido antes de guardarlo
#devuelve contenido cifrado

# Requisitos de seguridad
#passwords SIEMPRE cifrados
#tokens SIEMPRE validados
#usar headers correctamente:
#Authorization: Bearer <token>

# Casos que DEBEN funcionar
#login correcto → token válido
#login incorrecto → error
#token inválido → acceso denegado
#usuario sin rol admin → bloqueado
#datos cifrados → no legibles directamente

# Qué evalúo acá
#integración de TODO el sistema
#diseño limpio (no spaghetti)
#control de acceso real
#uso correcto de headers / params
#separación de capas

# Dificultades intencionales

#a validar : JWT → no podés validar ,OAuth → no entendés el flujo ,headers → no podés autenticar ,POO → se vuelve inmantenible ,encryption → rompés seguridad

# BONUS :

#refresh tokens
#expiración + renovación
#middleware de autorización

#Recomendación :RequestParser ,OAuthConfig ,EncryptionService ,JWTService ,OAuthHandler ,OAuthServer ,AuthService + Users