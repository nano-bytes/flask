# Simple ToDo With SQLAlchemy and Authentication

This project contains a simple **ToDo** that uses SQLAlchemy to handle DataBase and uses JWT to handle authentication

* **Contents**
  * Requirements
  * Deploy
  * Endpoints

### Requirements
This micro-service needs the following requirements to work:
>* python >= 3
>* Flask
>* Flask-SQLAlchemy
>* Flask-Migrate
>* Flask-JWT-Extended

### Deploy
To deploy this project it's necessary to create DB and it's tables before running the application, the following code would
 do that:

#### Migrations
Migrations for the service, this must run inside this project folder

```bash
flask db init
```

```bash
flask db migrate
```

```bash
flask db upgrade
```

#### Run
```bash
python run.py
```

### Endpoints

- **POST** register
- **POST** login
- **GET** all ToDo
- **GET** one ToDo
- **POST** a ToDo
- **PUT** a ToDo
- **DELETE** a ToDo

> All **ToDo** endpoints works with *bearer token* and this token is obtained after **login**
