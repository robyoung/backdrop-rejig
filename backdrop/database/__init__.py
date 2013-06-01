from werkzeug.utils import import_string

def from_config(config):
    driver = import_string(
        config.get('DATABASE_DRIVER', 'backdrop.database.mongodb'))

    return driver.Database.from_config(config)
