from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Dependências, se houver
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Outros campos do modelo
            ],
        ),
    ]