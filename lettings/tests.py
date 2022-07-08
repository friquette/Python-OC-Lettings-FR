from django.test import Client
from django.shortcuts import reverse

from lettings.models import Address, Letting
import pytest


@pytest.fixture
def create_letting(db):
    address = Address.objects.create(
        number=588,
        street='Argyle Avenue',
        city='East Meadow',
        state='NY',
        zip_code=11554,
        country_iso_code='USA'
    )
    letting = Letting.objects.create(
        title='Underground Hygge',
        address=address
    )
    return letting


@pytest.mark.django_db
def test_lettings_index_view():
    from django.conf import settings

    settings.DATABASES['default']['NAME'] = 'copied_db'
    client = Client()
    uri = reverse('lettings:lettings_index')
    resp = client.get(uri)

    assert resp.status_code == 200
    assert "<title>Lettings</title>" in str(resp.content)


@pytest.mark.django_db
def test_letting_view(create_letting):
    client = Client()
    uri = reverse('lettings:letting', args=(1,))
    resp = client.get(uri)

    assert resp.status_code == 200
    assert "<title>Underground Hygge</title>" in str(resp.content)
