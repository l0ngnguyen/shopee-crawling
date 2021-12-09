import yaml

def load_specific_config(config_type):
    with open('config.yaml', 'r') as f:
        config = yaml.load(f, yaml.FullLoader)[config_type]
    return config

def get_output_file_format():
    output = load_specific_config('output')
    return output.split('.')[-1]
