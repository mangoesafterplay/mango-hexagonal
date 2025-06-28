from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

# Leer DATABASE_URL_MIGRATION del entorno
DATABASE_URL_MIGRATION = os.getenv("DATABASE_URL_MIGRATION")

# Alembic config object
config = context.config

# Configurar logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Inyectar el URL en la config de Alembic
if DATABASE_URL_MIGRATION:
    config.set_main_option("sqlalchemy.url", DATABASE_URL_MIGRATION)
else:
    raise RuntimeError("DATABASE_URL_MIGRATION no está definido en tu .env")

# Importar metadatos (tus modelos Base)
from infrastructure.persistence import models
target_metadata = models.Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
