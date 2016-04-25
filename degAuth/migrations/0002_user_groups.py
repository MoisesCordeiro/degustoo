from django.db import models, migrations

def create_all_group(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Group = apps.get_model("auth", "Group")

    group_count = Group.objects.all().count()
    if not group_count:
        grupos = []

        # Groups
        grupos.append(Group(name='Administrador'))
        grupos.append(Group(name='Restaurante'))
        grupos.append(Group(name='Cliente'))

        Group.objects.bulk_create(grupos)

class Migration(migrations.Migration):

    dependencies = [
        ('degAuth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_all_group),
    ]