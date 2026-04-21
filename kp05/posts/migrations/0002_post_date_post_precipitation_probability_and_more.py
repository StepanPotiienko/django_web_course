from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="precipitation_probability",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="pressure",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="temperature",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="wind_speed",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
