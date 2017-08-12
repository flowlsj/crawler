#! /usr/bin/env python
# --*-- coding:utf-8 --*--

import logging.handlers
from config import CONFIG

handler = logging.handlers.RotatingFileHandler(CONFIG.CRAW_LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
format = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(format)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger(__name__)  # 获取logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)
