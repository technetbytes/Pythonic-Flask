#!/usr/bin/python
# -*- coding: utf-8 -*-

import cloudinary
from cloudinary.uploader import upload
from config.asset import AssetConfiguration
from utilities import constant
import numpy as np
import urllib.request
import cv2


class FileManager:
    '''Using this class user can upload different asset in different repositories'''
    def __init__(self, storage_type):
        if storage_type is None:
            self.storage_type = constant.STORAGE_TYPE_CLOUDINARY
        else:
            self.storage_type = storage_type

    def load_config(self):
        if self.storage_type == constant.STORAGE_TYPE_CLOUDINARY:
            config = AssetConfiguration(None)
            cloud_name = config.cloud_name
            api_key = config.api_key
            api_secret = config.api_secret
            cloudinary.config(cloud_name=cloud_name, api_key=api_key,
                              api_secret=api_secret)
            return
        elif self.storage_type == constant.STORAGE_TYPE_S3:
            pass

    def upload_file(self, file_name, custom_name=None):
        if self.storage_type == constant.STORAGE_TYPE_CLOUDINARY:
            if custom_name is None:
                return upload(file_name)
            else:
                return upload(file_name, public_id=custom_name)
        elif self.storage_type == constant.STORAGE_TYPE_S3:
            pass

    def get_file_url(self, file_name):
        if self.storage_type == constant.STORAGE_TYPE_CLOUDINARY:
            return cloudinary.utils.cloudinary_url(file_name)
        elif self.storage_type == constant.STORAGE_TYPE_S3:
            pass

    def get_image(self, file_name):
        if self.storage_type == constant.STORAGE_TYPE_CLOUDINARY:

            # download the image, convert it to a NumPy array, and then read....

            with urllib.request.urlopen(file_name) as url:
                image = np.asarray(bytearray(url.read()), dtype='uint8'
                                   )

            # it into OpenCV format

            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            # return the image

            return image
        elif self.storage_type == constant.STORAGE_TYPE_S3:
            pass