import csv
import httplib
import logging
import multiprocessing
import os
import shutil
import urllib
import xml.etree.ElementTree as ET
from functools import partial
from multiprocessing import Pool

import constants
import globals
import parser_translations
from parserr.parser_enums import TOSRegion
from utils import imageutil

IMAGE_SIZE = {  # top, left, width, height
    'bosscard2': (330, 440),
    'sub_card3': (330, 440),
    'item_tooltip_icon': (80, 80),
    '256_equip_icons': (256, 256),
    '256_costume_icons': (256, 256),
    'acc_item': (256, 256),
    'hair_accesory': (256, 256),
    'item': (80, 80),
    'payment': (80, 80),
}


WHITELIST_BASESKINSET = [
    'bosscard2',
    'sub_card3',
    'wearing_weapon',
]

WHITELIST_RGB = [
    'bosscard2',
    'sub_card3',
]


def parse_entity_icon(icon):
    icon = icon.lower()
    icon_found = None

    if icon == '':
        return None

    if icon in globals.assets_icons:
        icon_found = icon
    elif 'icon_' + icon in globals.assets_icons:
        icon_found = 'icon_' + icon
    elif icon + '_f' in globals.assets_icons:
        icon_found = icon + '_f'
    elif icon + '_m' in globals.assets_icons:
        icon_found = icon + '_m'

    if icon_found is not None:
        #globals.assets_icons_used.append(icon_found)
        return globals.assets_icons[icon_found]
    else:
        # Note: there's nothing we can do about this :'(
        #logging.debug('Missing icon: %s', icon)
        return icon


def parse(region, version_update):
    logging.debug('Parsing assets...')

    parse_icons('baseskinset.xml', version_update)
    parse_icons('classicon.xml', version_update)
    parse_icons('itemicon.xml', version_update)
    parse_icons('mongem.xml', version_update)
    parse_icons('monillust.xml', version_update)
    parse_icons('skillicon.xml', version_update)

    parse_images_jobs(region, version_update)


def parse_icons(file_name, version_update):
    logging.debug('Parsing icons from %s...', file_name)

    data_path = os.path.join(constants.PATH_INPUT_DATA, 'ui.ipf', 'baseskinset', file_name)
    data = ET.parse(data_path).getroot()

    # example: <imagelist category="Monster_icon_boss_02">
    # example: <image name="icon_wizar_energyBolt" file="\icon\skill\wizard\icon_wizar_energyBolt.png" />
    data = [(image, imagelist) for imagelist in data for image in imagelist]

    pool = Pool(processes=multiprocessing.cpu_count())
    pool.map(partial(parse_icons_step, file_name, version_update), data)
    pool.terminate()


def parse_icons_step(file_name, version_update, work):
    image = work[0]
    image_category = work[1].get('category')

    if image.get('file') is None or image.get('name') is None:
        return
    if file_name == 'baseskinset.xml' and image_category not in WHITELIST_BASESKINSET:
        return

    image_file = image.get('file').split('\\')[-1].lower()
    image_name = image.get('name').lower()
    image_rect = tuple(int(x) for x in image.get('imgrect').split()) if len(image.get('imgrect')) else None  # top, left, width, height

    # Copy icon to web assets folder
    copy_from = os.path.join(constants.PATH_INPUT_DATA, 'ui.ipf', *image.get('file').lower().split('\\')[:-1])
    copy_from = os.path.join(copy_from, image_file)
    copy_to = os.path.join(constants.PATH_WEB_ASSETS_ICONS, image_name)

    if not os.path.isfile(copy_from):
        # Note for future self:
        # if you find missing files due to wrong casing, go to the Hotfix at unpacker.py and force lowercase
        #logging.warning('Non-existing icon: %s', copy_from)
        return

    if version_update:
        shutil.copy(copy_from, copy_to)

        # Crop, Resize, Optimize and convert to JPG/PNG
        image_mode = 'RGB' if image_category in WHITELIST_RGB else 'RGBA'
        image_size = IMAGE_SIZE[image_category] if image_category in IMAGE_SIZE else (image_rect[2], image_rect[3])
        image_size = (80, 80) if file_name == 'classicon.xml' else image_size
        image_size = (80, 80) if file_name == 'skillicon.xml' else image_size

        imageutil.optimize(copy_to, image_mode, image_rect, image_size)

    # Store mapping for later use
    globals.assets_icons[image_name] = image_name


def parse_images_jobs(region, version_update):
    if not version_update or region != TOSRegion.iTOS:
        return

    logging.debug('Parsing images for jobs...')
    ies_path = os.path.join(constants.PATH_INPUT_DATA, 'ies.ipf', 'job.ies')

    with open(ies_path, 'rb') as ies_file:
        for row in csv.DictReader(ies_file, delimiter=',', quotechar='"'):
            image_path = os.path.join(constants.PATH_WEB_ASSETS_IMAGES, 'classes', row['ClassName'])
            image_path_f = image_path + '_f.gif'
            image_path_m = image_path + '_m.gif'

            if os.path.exists(image_path_f):
                continue

            name = parser_translations.translate(row['Name'])
            name = ''.join(name.split(' ')).lower()

            treeofsavior_domain = 'treeofsavior.com'
            treeofsavior_path = '/img/class2/class_character/'

            conn = httplib.HTTPSConnection(treeofsavior_domain)
            conn.request('HEAD', treeofsavior_path + name + '_f.gif')

            response = conn.getresponse()
            conn.close()

            if response.status != 200:
                logging.warn('Failed to retrieve job image: %s, status %s', treeofsavior_path + name + '_f.gif', response.status)
                continue

            urllib.urlretrieve('https://' + treeofsavior_domain + treeofsavior_path + name + '_f.gif', image_path_f)
            urllib.urlretrieve('https://' + treeofsavior_domain + treeofsavior_path + name + '_m.gif', image_path_m)


#def parse_clean(version_update):
#    if not version_update:
#        return
#
#    logging.debug('Cleaning unused icons...')
#    for key in globals.assets_icons.keys():
#        if key not in globals.assets_icons_used:
#            path = os.path.join(constants.PATH_WEB_ASSETS_ICONS, key)
#
#            if os.path.isfile(path + '.jpg'):
#                os.remove(path + '.jpg')
#            elif os.path.isfile(path + '.png'):
#                os.remove(path + '.png')
