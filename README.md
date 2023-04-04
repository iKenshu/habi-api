## Habi API

Una API que hace consultas a la base de datos en raw SQL para traer diferentes datos y que además permita a los usuarios utilizar ciertos filtros para mejor búsqueda de la propiedad.

## Tecnologías a usar

- Python
- FastAPI
- SQLAlchemy
- Pytest
- ruff para la legibilidad del código junto con black

**Algunas dudas que tenía al incio**

¿Cómo hago para ejecutar SQL puro?

Terminé investigando y recordando que una manera sencilla de hacerlo es con SQLAlchemy así que me fuí por esa opción.

¿Cómo abordar el desarrollo?

No lo tuve muy claro al inicio, pero poco a poco fui resolviendo cada problema al que me enfrentaba y ya empezó a tomar formar junto con la organización de carpetas adecuada y modular.

## Cómo ejecutar

Para ejectuar el código debes tener instalado Python y crear tu propio entorno virtual para no instalar las dependecias directamente en tu PC.

Después que hayas instalado las dependencias. Para ejecutar la aplicación con FastAPI debes correr el siguiente comando:

`uvicorn app.main:app`

### ENDPOINTS

`/ GET` Esto solo devuelve un mensaje de bienvenida.

`/property/all GET` Esto devolverá todos los inmuebles que existen en la base de datos con el estado de "pre_venta", "en_venta" y "vendido"

`/property/ GET` Este recibe paramétros query como city, status, year. En caso de no recibir ninguna funcionará igual que `/all/`

Todos devuelven una respuesta JSON con atributos dirección, precio, ciudad, descripción y estado del inmueble.

## Sobre la nueva tabla de "me gusta"

**El modelo entidad relación**:

![](https://i.imgur.com/63s6g0N.png)

Usando la base de datos de pruebas como ejemplo con las tablas existente, cree una nueva tabla llamada likes con tres atributos: id, created_date, user_id y property_id. Los últimos dos referenciando a las tablas de user y property.

`user_id`: es un entero asociado a la tabla de user, de uno a muchos con la intención de que un usuario pueda darle me gusta a muchas propiedades.

`property_id`: es un entero asociado a la tablea property, de uno a muchos con la intención de que una propiedad pueda tener muchos me gusta.

`created_date`: un tipo de dato fecha y tiempo para saber el momento preciso en que la persona le dio like a cierta propiedad.

También se tuvo en cuenta que se podría agregar otro tipo de atributo como `status` entre activo o inactivo en caso de que no se quisiera eliminar por completo un registro en la tabla al momento de que la persona le quitase el like a cierta propiedad. Creo que para este caso puede ser mejor no tener almacenados tantos registros en la base de datos ya que no aporta valor agregado tener un registro de los cambios de los likes.

**SQL**

```
CREATE TABLE likes (
    id INT PRIMARY KEY NOT NULL,
    created_date DATETIME NOT NULL,
    user_id INT NOT NULL,
    property_id INT NOT NULL,

    CONSTRAINT UC_LIKE UNIQUE (user_id, property_id)
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (property_id) REFERENCES property(id)
);

```
