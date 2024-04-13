from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from music_application_rev.web.validators import validate_string_alphanumeric


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_string_alphanumeric,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    PRICE_MIN_VALUE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LEN,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=MUSICS,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )

    class Meta:
        ordering = ('pk',)
