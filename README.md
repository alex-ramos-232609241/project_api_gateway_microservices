
# API Gateway

Este proyecto implementa un API Gateway que se comunica con múltiples microservicios a través de rutas proxy para manejar solicitudes HTTP de usuarios, órdenes y productos.

## Tecnologías utilizadas

- **Python 3.8**
- **Django**
- **Requests**
- **JSON**

## Estructura del Proyecto

El API Gateway actúa como un intermediario entre los clientes y tres microservicios diferentes:

1. **Servicio de Usuarios (`USER_SERVICE_URL`)**
2. **Servicio de Órdenes (`ORDER_SERVICE_URL`)**
3. **Servicio de Productos (`PRODUCT_SERVICE_URL`)**

### Rutas disponibles

El Gateway expone las siguientes rutas para interactuar con los microservicios:

- `/users/{path}`: Redirige las solicitudes al servicio de usuarios.
- `/orders/{path}`: Redirige las solicitudes al servicio de órdenes.
- `/products/{path}`: Redirige las solicitudes al servicio de productos.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/api-gateway.git
   ```
   
2. Crea un entorno virtual y actívalo:

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las URLs de los microservicios en el archivo `views.py`:
   ```python
   USER_SERVICE_URL = 'http://localhost:8001/users/'
   ORDER_SERVICE_URL = 'http://localhost:8002/orders/'
   PRODUCT_SERVICE_URL = 'http://localhost:8003/products/'
   ```

## Uso

### Proxy de Usuarios

- **GET** `/users/{path}`: Redirige a los endpoints GET del servicio de usuarios.
- **POST** `/users/{path}`: Redirige a los endpoints POST del servicio de usuarios, enviando el cuerpo de la solicitud en formato JSON.
- **PUT** `/users/{path}`: Redirige a los endpoints PUT del servicio de usuarios, enviando los datos actualizados.
- **DELETE** `/users/{path}`: Redirige a los endpoints DELETE del servicio de usuarios.

### Proxy de Órdenes

- **GET** `/orders/{path}`: Redirige a los endpoints GET del servicio de órdenes.
- **POST** `/orders/{path}`: Redirige a los endpoints POST del servicio de órdenes.
- **PUT** `/orders/{path}`: Redirige a los endpoints PUT del servicio de órdenes.
- **DELETE** `/orders/{path}`: Redirige a los endpoints DELETE del servicio de órdenes.

### Proxy de Productos

- **GET** `/products/{path}`: Redirige a los endpoints GET del servicio de productos.
- **POST** `/products/{path}`: Redirige a los endpoints POST del servicio de productos.
- **PUT** `/products/{path}`: Redirige a los endpoints PUT del servicio de productos.
- **DELETE** `/products/{path}`: Redirige a los endpoints DELETE del servicio de productos.

## Manejo de Errores

Si una solicitud contiene un cuerpo JSON inválido, el Gateway devolverá un error 400 con el mensaje `Invalid JSON`.

## Ejecución del proyecto

Para ejecutar el servidor de Django:
```bash
python manage.py runserver
```

Por defecto, el servidor se ejecutará en `http://localhost:8000/`, y las solicitudes a los microservicios se manejarán de acuerdo a las rutas definidas.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus sugerencias.

## Licencia

Este proyecto está bajo la licencia MIT.