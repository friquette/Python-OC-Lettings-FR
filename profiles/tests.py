from django.test import Client
from django.shortcuts import reverse
from django.contrib.auth.models import User

from profiles.models import Profile

import pytest


@pytest.fixture
def create_profile(db):
    user = User.objects.create(
        username='HeadlinesGazer',
        first_name='Jamie',
        last_name='Lal',
        email='jssssss33@acee9.live'
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city='Buenos Aires'
    )
    return profile


@pytest.mark.django_db
def test_profiles_index_view():
    client = Client()
    uri = reverse('profiles:profiles_index')
    resp = client.get(uri)

    assert resp.status_code == 200
    assert "<title>Profiles</title>" in str(resp.content)


@pytest.mark.django_db
def test_profile_view(create_profile):
    client = Client()
    uri = reverse('profiles:profile', args=('HeadlinesGazer',))
    resp = client.get(uri)

    assert resp.status_code == 200
    assert "<title>HeadlinesGazer</title>" in str(resp.content)
