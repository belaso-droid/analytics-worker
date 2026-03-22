import logging
import time
import json
from datetime import datetime
from typing import Dict, List, Optional

def get_current_timestamp() -> int:
    return int(time.time())

def create_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def load_json_config(config_file: str) -> Dict:
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except json.JSONDecodeError as e:
        logging.error(f"Failed to load JSON config: {e}")
        return {}

def load_config(config_file: str) -> Dict:
    config = load_json_config(config_file)
    return config

def extract_event_data(data: Dict) -> Dict:
    event_data = {}
    for key, value in data.items():
        if key.startswith('event_'):
            event_data[key] = value
    return event_data

def format_event_timestamp(timestamp: Optional[int]) -> str:
    if timestamp:
        return datetime.fromtimestamp(timestamp).isoformat()
    else:
        return None

def format_event_data(event_data: Dict) -> List[Dict]:
    event_list = []
    for event in event_data.values():
        event_dict = {
            'timestamp': format_event_timestamp(event['timestamp']),
            'name': event['name'],
            'properties': event.get('properties', {})
        }
        event_list.append(event_dict)
    return event_list