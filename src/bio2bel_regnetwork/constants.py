# -*- coding: utf-8 -*-

import os
from bio2bel import get_data_dir

MODULE_NAME = 'regnetwork'
DATA_DIR = get_data_dir(MODULE_NAME)

_base_url = 'http://www.regnetworkweb.org/download'

_human_file_name = 'human.zip'
_mouse_file_name = 'mouse.zip'
_directions_file_name = 'RegulatoryDirections.rar'

HUMAN_URL = f'{_base_url}/{_human_file_name}'
HUMAN_FILE_PATH = os.path.join(DATA_DIR, _human_file_name)

"""
Contents of human.zip:

human.node columns:
 
1. Entrez Gene Identifier
2. Gene Name (from HGNC)

human.source columns:

1. Source Gene Name
2. Source Entrez Gene Identifier
3. Target Gene Name
4. Target Entrez Gene Identifier

ENCODE columns:

1. Source Entrez Gene Identifier?
2. Target Entrez Gene Identifier?

"""

MOUSE_URL = f'{_base_url}/{_mouse_file_name}'
MOUSE_FILE_PATH = os.path.join(DATA_DIR, _mouse_file_name)

DIRECTIONS_URL = f'{_base_url}/{_directions_file_name}'
DIRECTIONS_FILE_PATH = os.path.join(DATA_DIR, _directions_file_name)
