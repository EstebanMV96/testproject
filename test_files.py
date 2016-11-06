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
	estaLleno=False
	estaLleno=len(result.data())>0
	assert estaLleno==True
	
	
	
def test_eliminarArchivos(client):
	result=eliminarArchivos(client)
	assert "Hola" in result.data() 

