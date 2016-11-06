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


def test_darArchivos(client):
	result=darArchivos(client)
	estaLleno=len(result.data())>0
	assert estaLleno
	
	
	
def test_eliminarArchivos(client):
	result=eliminarArchivos(client)
	assert 200 in result.data(), "Hubo un error al borrar los archivos"

