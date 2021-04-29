# django

## Proyecto para la realización de REST:API con django REST Framework

### Nombre de la aplicación my_app

- El proyeto cuenta con la implementación del módulo admin.

- Se realiza de tal manera que los requests [GET] y [POST], se encuentran en las siguientes direcciones para los modelos implementados:

  - listreviews/
  - listtransactions/
  - listpropertytypes/
  - liststates/
  - listcities/
  - listcategories/
  - listproperties/

- Los requests para [PUT], [PATCH] y [DELETE] se encuentran de la siguiente manera:

  - updatereviews/<id>
  - updatetransactions/<id>
  - updatepropertytypes/<id>
  - updatestates/<id>
  - updatecities/<id>
  - updatecategories/<id>
  - updateproperties/<id>
  
## [GET]

Implementación convencional, se obtiene la información en la base de datos

## [POST]

Implementación convencional, ingresa registro a la base de daros

## [PUT]

Implementación convencional, realiza la actualización de un registro por medio de su "id" (requiere de todos los campos)

## [PATCH]

Realiza la actualización por medio de su "id", permite cambios parciales

## [DELETE]

Realiza la eliminación del registro por su "id"

