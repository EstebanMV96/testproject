import pytest
import files
import json

@pytest.fixture
def client(request):
	client=files.app.test_client()
	return client

def darArchivos(client):
	return client.get('/files',follow_redirects=True)


def eliminarArchivos(client):
	return client.delete('/files',follow_redirects=True)

def recently(client):
	return client.get('/files/recently_created',follow_redirects=True)


def test_darArchivos(client):
	result=darArchivos(client)
	esta="comandos.py" in result.data
	esta1="files.py" in result.data
	assert esta, "comandos.py deberia de aparecer en los archivos listados"
	assert esta1, "files.py deberia de aparecer en los archivos listados"
	assert result.status=="200 OK", "El codigo de respuesta indica un error"
	
	
	
def test_eliminarArchivos(client):
	result=eliminarArchivos(client)
	assert "Todos los archivos no VIP fueron borrados" in result.data 
	assert result.status=="200 OK", "El codigo de respuesta indica un error"


def test_recently(client):
	result=recently(client)
	assert result.status=="200 OK", "El codigo de respuesta no fue el esperado"
