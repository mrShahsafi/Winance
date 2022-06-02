from django.db.models import Model
from django.db.models import (
    DateTimeField,
    BooleanField,
    CharField,
)


class AbstractModel(Model):
    name = CharField(
        default="No Name",
        max_length=256,
    )
    description = CharField(
        default="no description",
        max_length=256,
    )
    created_date = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True
