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
	resultado="comandos.py" in result.data() && "files.py" in result.data()
	assert resultado, "No esta listando bien los archivos"

def test_eliminarArchivos(client):
	result=eliminarArchivos(client)
	assert "Todos los archivos no VIP fueron borrados" in result.data, "Hubo problema al borrar los archivos"

