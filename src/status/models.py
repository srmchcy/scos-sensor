from django.db import models


MAX_DESCRIPTION_LEN = 1024


class Location(models.Model):
    """Holds the current longitude and latitude of the sensor.

    Primarily used for mapping and geo-filtering.

    """
    active = models.BooleanField(
        default=True,
        help_text="Display this location on /status."
    )
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LEN,
        blank=True,
        help_text="Freeform text description of this location."
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude of the sensor in decimal degrees.",
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        help_text="Longitude of the sensor in decimal degrees.",
    )

    def save(self, *args, **kwargs):
        """Deselect active on all other Locations if self is active."""
        # https://stackoverflow.com/a/44720466/4433645
        if self.active:
            # select all other active items
            qs = type(self).objects.filter(active=True)

            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)

            qs.update(active=False)

        super(Location, self).save(*args, **kwargs)
