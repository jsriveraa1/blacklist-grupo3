# BlackLists - Grupo 3

Microservicio desarrollado en Python utilizando Flask 1.1.1 (debido a que AWS utiliza Python 3.8 fue necesario trabajar con esa versión, se podría validar si se puede ajustar a una versión más actual), desplegado en AWS Beanstalk e integración con AWS RDS (PostgreSQL).
### AWS Beanstalk
#### http://blacklist-grupo3-env.eba-kxn9vy2c.us-east-1.elasticbeanstalk.com/

### Endpoints
| Servicio           | Crear/Notificar correo en blacklist                                                                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Endpoint           | http://blacklist-grupo3-env.eba-kxn9vy2c.us-east-1.elasticbeanstalk.com/blacklists                                                                                  |
| **Authorization**: | True                                                                                                                                                                |
| **Method**:        | Post                                                                                                                                                                |
| **Body**:          | <pre> { <br> &emsp; "email":"js@hotmail.com.es", <br> &emsp; "app_uuid":"7f91f9fe-8672-415b-afcc-c4822ef219ae", <br> &emsp; "blocked_reason":"prueba" <br> } </pre> |                                         
| **Observaciones**: | **blocked_reason** -> Es un campo opcional.                                                                                                                         |

| Servicio           | List correo en blacklist                                                               |
|--------------------|----------------------------------------------------------------------------------------|
| Endpoint           | http://blacklist-grupo3-env.eba-kxn9vy2c.us-east-1.elasticbeanstalk.com/<string:email> |
| **Authorization**: | True                                                                                   |
| **Method**:        | Get                                                                                    |
| **Body**:          | N/A                                                                                    |                                         
| **Observaciones**: | **email** -> Es un campo **obligatorio**.                                              |

| Servicio           | Obtener token                                                                      |
|--------------------|------------------------------------------------------------------------------------|
| Endpoint           | http://blacklist-grupo3-env.eba-kxn9vy2c.us-east-1.elasticbeanstalk.com/blacklists |
| **Authorization**: | False                                                                              |
| **Method**:        | Get                                                                                |
| **Body**:          | N/A                                                                                |                                         
| **Observaciones**: | **token** -> No expira.                                                            |

