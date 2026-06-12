"""Unit tests for the Flask application - Task 1 CI/CD Azure."""

import pytest
import json
from app.app import app


@pytest.fixture
def client():
    """Flask test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestRootEndpoint:
    def test_index_returns_200(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_index_returns_json(self, client):
        response = client.get('/')
        assert response.content_type == 'application/json'

    def test_index_contains_message(self, client):
        response = client.get('/')
        data = json.loads(response.data)
        assert 'message' in data
        assert 'CodeAlpha' in data['message']

    def test_index_contains_status(self, client):
        response = client.get('/')
        data = json.loads(response.data)
        assert data['status'] == 'running'


class TestHealthEndpoint:
    def test_health_returns_200(self, client):
        response = client.get('/health')
        assert response.status_code == 200

    def test_health_returns_json(self, client):
        response = client.get('/health')
        assert response.content_type == 'application/json'

    def test_health_status_is_healthy(self, client):
        response = client.get('/health')
        data = json.loads(response.data)
        assert data['status'] == 'healthy'

    def test_health_contains_service_name(self, client):
        response = client.get('/health')
        data = json.loads(response.data)
        assert data['service'] == 'codealpha-webapp'

    def test_health_contains_timestamp(self, client):
        response = client.get('/health')
        data = json.loads(response.data)
        assert 'timestamp' in data


class TestInfoEndpoint:
    def test_info_returns_200(self, client):
        response = client.get('/info')
        assert response.status_code == 200

    def test_info_returns_json(self, client):
        response = client.get('/info')
        assert response.content_type == 'application/json'

    def test_info_contains_app_name(self, client):
        response = client.get('/info')
        data = json.loads(response.data)
        assert data['app'] == 'codealpha-webapp'


class TestNotFound:
    def test_unknown_route_returns_404(self, client):
        response = client.get('/nonexistent')
        assert response.status_code == 404
