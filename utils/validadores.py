import re

def validar_no_vacio(valor, campo="Campo"):
    """
    Verifica que un campo no esté vacío
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError(f"{campo} no puede estar vacío")


def validar_longitud(valor, minimo=1, maximo=255, campo="Campo"):
    """
    Verifica que el texto tenga una longitud válida
    """
    longitud = len(str(valor))
    if longitud < minimo or longitud > maximo:
        raise ValueError(f"{campo} debe tener entre {minimo} y {maximo} caracteres")


def validar_email(correo):
    """
    Verifica que el correo tenga formato válido
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron, correo):
        raise ValueError("Correo inválido")


def validar_solo_numeros(valor, campo="Campo"):
    """
    Verifica que solo contenga números
    """
    if not str(valor).isdigit():
        raise ValueError(f"{campo} debe contener solo números")


def validar_rango(valor, minimo=None, maximo=None, campo="Campo"):
    """
    Verifica que un número esté dentro de un rango
    """
    try:
        numero = float(valor)
    except:
        raise ValueError(f"{campo} debe ser numérico")

    if minimo is not None and numero < minimo:
        raise ValueError(f"{campo} no puede ser menor a {minimo}")

    if maximo is not None and numero > maximo:
        raise ValueError(f"{campo} no puede ser mayor a {maximo}")


def validar_texto_seguro(valor, campo="Campo"):
    """
    Evita caracteres peligrosos
    """
    patron = r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑ.,_-]+$'
    if not re.match(patron, valor):
        raise ValueError(f"{campo} contiene caracteres no permitidos")


def validar_password(clave):
    """
    Verifica que la contraseña sea segura
    """
    if len(clave) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")

    if not re.search(r'[A-Z]', clave):
        raise ValueError("Debe tener una mayúscula")

    if not re.search(r'[a-z]', clave):
        raise ValueError("Debe tener una minúscula")

    if not re.search(r'[0-9]', clave):
        raise ValueError("Debe tener un número")