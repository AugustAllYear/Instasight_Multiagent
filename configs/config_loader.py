import os
import yaml
from dotenv import load_dotenv

load_dotenv()  # load .env file

def load_config(config_path="configs/config.yaml"):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    # Override with environment variables if present
    for key in config.get('api', {}):
        env_var = config['api'].get(key + '_env')
        if env_var and os.getenv(env_var):
            config['api'][key] = os.getenv(env_var)
    return config