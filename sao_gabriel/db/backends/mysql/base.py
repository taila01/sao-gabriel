"""Connector/Python with correctly quoted literals in Django schema SQL."""

from mysql.connector.django.base import DatabaseWrapper as ConnectorDatabaseWrapper
from mysql.connector.django.schema import DatabaseSchemaEditor as ConnectorSchemaEditor


class DatabaseSchemaEditor(ConnectorSchemaEditor):
    def quote_value(self, value):
        # Connector/Python 9.7 only escapes schema values, omitting SQL quotes.
        # Follow its cursor parameter conversion, including the active SQL mode.
        self.connection.ensure_connection()
        connection = self.connection.connection
        converter = connection.converter
        converted = converter.to_mysql(value)
        escaped = converter.escape(converted, connection.sql_mode)
        quoted = converter.quote(escaped)
        if isinstance(quoted, (bytes, bytearray)):
            quoted = quoted.decode(connection.python_charset)
        return quoted


class DatabaseWrapper(ConnectorDatabaseWrapper):
    SchemaEditorClass = DatabaseSchemaEditor
