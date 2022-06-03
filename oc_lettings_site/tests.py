from django.test import Client
from django.shortcuts import reverse


def test_index_page():
    client = Client()
    uri = reverse('index')
    resp = client.get(uri)
    assert resp.status_code == 200
    assert "Holiday Homes" in str(resp.content)
