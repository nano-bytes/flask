# Simple ToDo With SQLAlchemy

This project contains a simple **ToDo** that uses SQLAlchemy to handle DataBase.

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

- **GET** all ToDo
- **GET** one ToDo
- **POST** a ToDo
- **PUT** a ToDo
- **DELETE** a ToDo


In order to make this service works 