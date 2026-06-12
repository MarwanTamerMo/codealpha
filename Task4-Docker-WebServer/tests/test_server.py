"""Tests for the Docker web server - Task 4."""

import pytest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestIndex:
    def test_index_returns_200(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_index_contains_codealpha(self, client):
        response = client.get('/')
        assert b'CodeAlpha' in response.data

    def test_index_contains_docker(self, client):
        response = client.get('/')
        assert b'Docker' in response.data or b'docker' in response.data


class TestHealth:
    def test_health_returns_200(self, client):
        response = client.get('/health')
        assert response.status_code == 200

    def test_health_json(self, client):
        response = client.get('/health')
        assert response.content_type == 'application/json'

    def test_health_status_healthy(self, client):
        data = json.loads(client.get('/health').data)
        assert data['status'] == 'healthy'

    def test_health_service_name(self, client):
        data = json.loads(client.get('/health').data)
        assert data['service'] == 'codealpha-docker-webserver'

    def test_health_has_timestamp(self, client):
        data = json.loads(client.get('/health').data)
        assert 'timestamp' in data


class TestApiInfo:
    def test_info_returns_200(self, client):
        assert client.get('/api/info').status_code == 200

    def test_info_is_json(self, client):
        assert client.get('/api/info').content_type == 'application/json'

    def test_info_app_name(self, client):
        data = json.loads(client.get('/api/info').data)
        assert data['app'] == 'codealpha-docker-webserver'

    def test_info_has_python(self, client):
        data = json.loads(client.get('/api/info').data)
        assert 'python' in data


class TestApiStats:
    def test_stats_returns_200(self, client):
        assert client.get('/api/stats').status_code == 200

    def test_stats_has_uptime(self, client):
        data = json.loads(client.get('/api/stats').data)
        assert 'uptime' in data

    def test_stats_has_timestamps(self, client):
        data = json.loads(client.get('/api/stats').data)
        assert 'start_time' in data
        assert 'current_time' in data


class TestNotFound:
    def test_404(self, client):
        assert client.get('/nonexistent-page').status_code == 404
