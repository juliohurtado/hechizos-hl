from django.db import models
from django.utils.text import slugify


class Group(models.Model):
    name_choices = (
        ("Neutrales", "Neutrales"),
        ("Orden del Fénix", "Orden del Fénix"),
        ("Marca Tenebrosa", "Marca Tenebrosa"),
        ("Libros de Hechizos", "Libros de Hechizos"),
        ("Paladines", "Orden de la Mano de Plata"),
        ("Oscuros", "Orden Oscura"),
        ("Sacerdotes", "Orden de Avalón"),
    )
    name = models.CharField(max_length=64, choices=name_choices, unique=True)
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_name_display()


class Range(models.Model):
    name = models.CharField(max_length=64)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="ranges")
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Range, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)
    description = models.TextField()
    range = models.ManyToManyField(Range)

    type_choices = (
        ("e", "Efecto"),
        ("r", "Rayo"),
        ("i", "Invocación"),
        ("o", "Invocación - Efecto"),
        ("ei", "Efecto - Invocación"),
        ("eq", "Equipable"),
        ("om", "Onda Mágica"),
        ("ro", "Rolistico"),
        ("oe", "Onda Expansiva"),
    )

    method_choices = (
        ("V", "Verbal"),
        ("N", "No Verbal"),
        ("R", "Rolistico"),
    )

    object_choices = (
        ("V", "Con Varita"),
        ("N", "Sin Varita"),
        ("O", "Objeto"),
    )

    type = models.CharField(max_length=2, choices=type_choices, default="e")
    method = models.CharField(max_length=1, choices=method_choices, default="V")
    object = models.CharField(max_length=1, choices=object_choices, default="V")
    battles = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name).lower()

        super(Spell, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-battles", "name"]
