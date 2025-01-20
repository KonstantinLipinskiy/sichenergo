from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class TransformItem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Серія")
    image = CloudinaryField(
        default="static/deps/img/trans.png", verbose_name="Зображення"
    )
    detail_url = models.URLField(blank=True, null=True, verbose_name="Посилання")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "transform"
        verbose_name = "Серію"
        verbose_name_plural = "Серія трансформатора"


class InformTransform(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Трансформатор (опитовий лист)"
    )
    video =  models.FileField(upload_to='videos/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    description = models.TextField(verbose_name="Опис", blank=True)
    file_ol = CloudinaryField(resource_type='auto', verbose_name="Файл для скачування" )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опитувальний лист"
        verbose_name_plural = "Трансформатор - Опитувальні листи"


class TransformTm(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Потужність трансформаторів ТМ та ТМЖ"
    )
    image = CloudinaryField(
        default="static/deps/img/trans.png", verbose_name="Зображення"
    )
    file_tm = CloudinaryField(resource_type='raw', verbose_name="Скачати креслення трансформаторів ТМ та ТМЖ" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор ТМ та ТМЖ"
        verbose_name_plural = "Трансформатори ТМ та ТМЖ"


class TransformTmg(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Потужність трансформаторів ТМГ та ТМЖГ"
    )
    image = CloudinaryField(
        default="static/deps/img/trans.png", verbose_name="Зображення"
    )
    file_tmg = CloudinaryField(resource_type='raw', verbose_name="Скачати креслення трансформаторів ТМГ та ТМЖГ" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор ТМГ та ТМЖГ"
        verbose_name_plural = "Трансформатори ТМГ та ТМЖГ"


class TransformTmz(models.Model):
    name = models.CharField(max_length=255, verbose_name="Трансформатори ТМЗ")
    image = CloudinaryField(
        default="static/deps/img/trans.png", verbose_name="Зображення"
    )
    file_tmz = CloudinaryField(resource_type='raw', verbose_name="Скачати креслення трансформаторів ТМЗ" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор ТМЗ"
        verbose_name_plural = "Трансформатори ТМЗ"


class TransformYZ(models.Model):
    name = models.CharField(max_length=255, verbose_name="Трансформатори серії Y/Z")
    image = CloudinaryField(
        default="static/deps/img/trans.png", verbose_name="Зображення"
    )
    file_yz = CloudinaryField(resource_type='raw', verbose_name="Скачати креслення трансформаторів Y/Z" )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор Y/Z"
        verbose_name_plural = "Трансформатори Y/Z"


class InformKTP(models.Model):
    title = models.CharField(max_length=150, verbose_name="КТП (опитовий лист)")
    video =  models.FileField(upload_to='videos/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    description = models.TextField(verbose_name="Опис", blank=True)
    file_ol = CloudinaryField(resource_type='auto', verbose_name="Файл для скачування" )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опитувальний лист"
        verbose_name_plural = "КТП - Опитувальні листи"
