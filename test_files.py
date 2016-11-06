import pytest
import files

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
	assert "200" in result.data

def test_eliminarArchivos(client):
	result=eliminarArchivos(client)
	assert "Todos los archivos no VIP fueron borrados" in result.data

