import yaml

def load_selectors():
    with open('config.yaml', 'r') as f:
        selectors = yaml.load(f, yaml.FullLoader)['css_selectors']
    return selectors

def load_start_urls():
    with open('config.yaml', 'r') as f:
        start_urls = yaml.load(f, yaml.FullLoader)['start_urls']
    return start_urls

def load_download_delay():
    with open('config.yaml', 'r') as f:
        download_delay = yaml.load(f, yaml.FullLoader)['download_delay']
    return download_delay

def load_output_path():
    with open('config.yaml', 'r') as f:
        output = yaml.load(f, yaml.FullLoader)['output']
    return output

def get_output_file_format():
    output = load_output_path()
    return output.split('.')[-1]
