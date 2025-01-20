from django.db import models
from cloudinary.models import CloudinaryField


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
    video = CloudinaryField(blank=True, null=True, verbose_name="Відео")
    description = models.TextField(verbose_name="Опис", blank=True)
    file_ol = models.FileField(upload_to="ol/", verbose_name="Файл для скачування")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опитувальний лист"
        verbose_name_plural = "Трансформатор - Опитувальні листи"


class TransformTm(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Потужність трансформаторів ТМ та ТМЖ"
    )
    image = models.ImageField(
        upload_to="img_tm/", verbose_name="Креслення трансформаторів ТМ та ТМЖ"
    )
    file_tm = models.FileField(
        upload_to="drawing_tm/",
        verbose_name="Скачати креслення трансформаторів ТМ та ТМЖ",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор ТМ та ТМЖ"
        verbose_name_plural = "Трансформатори ТМ та ТМЖ"


class TransformTmg(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Потужність трансформаторів ТМГ та ТМЖГ"
    )
    image = models.ImageField(
        upload_to="img_tmg/", verbose_name="Креслення трансформаторів ТМГ та ТМЖГ"
    )
    file_tmg = models.FileField(
        upload_to="drawing_tmg/",
        verbose_name="Скачати креслення трансформаторів ТМГ та ТМЖГ",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор ТМГ та ТМЖГ"
        verbose_name_plural = "Трансформатори ТМГ та ТМЖГ"


class TransformTmz(models.Model):
    name = models.CharField(max_length=255, verbose_name="Трансформатори ТМЗ")
    image = models.ImageField(
        upload_to="img_tmz/", verbose_name="Креслення трансформаторів ТМЗ"
    )
    file_tmz = models.FileField(
        upload_to="drawing_tmz/", verbose_name="Скачати креслення трансформаторів ТМЗ"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор ТМЗ"
        verbose_name_plural = "Трансформатори ТМЗ"


class TransformYZ(models.Model):
    name = models.CharField(max_length=255, verbose_name="Трансформатори серії Y/Z")
    image = models.ImageField(
        upload_to="img_yz/", verbose_name="Креслення трансформаторів Y/Z"
    )
    file_yz = models.FileField(
        upload_to="drawing_yz/", verbose_name="Скачати креслення трансформаторів Y/Z"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трансформатор Y/Z"
        verbose_name_plural = "Трансформатори Y/Z"


class InformKTP(models.Model):
    title = models.CharField(max_length=150, verbose_name="КТП (опитовий лист)")
    video = models.FileField(
        upload_to="video/", verbose_name="Відео", blank=True, null=True
    )
    description = models.TextField(verbose_name="Опис", blank=True)
    file_ol = models.FileField(upload_to="ol/", verbose_name="Файл для скачування")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опитувальний лист"
        verbose_name_plural = "КТП - Опитувальні листи"
