
# Project Django Portafolio

A simple blog application created using Django framework.

## Setup


### Install Python

Install Python 3.10

### Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Install virtualenv

Virtualenv una herramienta para crear entornos virtuales de Python. Esto es útil para aislar las dependencias de un proyecto de las dependencias de otros proyectos.

```bash
pip install virtualenv
```

### Crear una máquina virtual

```bash
virtualenv venv --python=python3.10
```

### Activar la máquina virtual

```bash
source venv/bin/activate
```

- windows

```bash
venv\Scripts\activate

venv/Scripts/activate.ps1
```

### Requirements

Instalar las módulos necesarios para iniciar el proyecto
```bash
pip install -r requirements.txt
```
    
## Para la base de datos

### Migraciones en la base de datos

Run migrations with the following commands

```bash
  python manage.py makemigrations
```

```bash
  python manage.py migrate
```
## Use ngrok
Si se prueba la aplicación en ngrok cambiar la variable ALLOWED_HOSTS en  djangoPorfolio/settings.py, reemplazar el primer elemento con el endpoint que sale en tu app
```bash
  ALLOWED_HOSTS = ['fc1d-181-67-205-182.ngrok.io', 'localhost','127.0.0.1']
```
También agregar con la url que la aplicación ngrok te da
```bash
  CSRF_TRUSTED_ORIGINS = ['https://0517-181-67-205-182.sa.ngrok.io']
```
## Run Locally

Start the server

```bash
  python manage.py runserver
```
## Authors

- [Raisa Orellana](https://github.com/Raisa320)


