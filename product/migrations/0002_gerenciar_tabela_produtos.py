from django.db import migrations


def criar_tabela_ausente(apps, schema_editor):
    # O modelo antigo era unmanaged: a migração inicial não criava a tabela.
    produto = apps.get_model('product', 'Product')
    tabelas = schema_editor.connection.introspection.table_names()
    if produto._meta.db_table not in tabelas:
        schema_editor.create_model(produto)


class Migration(migrations.Migration):
    atomic = False
    dependencies = [('product', '0001_initial')]
    operations = [
        migrations.AlterModelOptions(name='product', options={'managed': True}),
        # Preserva tabelas e dados existentes, inclusive ao reverter a migração.
        migrations.RunPython(criar_tabela_ausente, migrations.RunPython.noop, atomic=False),
    ]
