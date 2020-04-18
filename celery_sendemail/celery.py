#
# Python3开始，import 默认只做absolute import
#from __future__ import absolute_import, print_function, unicode_literals

from celery import Celery
from celery_sendemail import celeryconfig

# 实例化celery对象，任务调度利器（分布式任务调度模块）
app=Celery('celery_test')

# 加载app配置文件
# 1. app.config_from_object('celery_test.celeryconfig')
# 2.
app.config_from_object(celeryconfig)


if __name__ == '__main__':
    app.start()