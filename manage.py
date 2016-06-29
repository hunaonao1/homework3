# -*- encoding=UTF-8 -*-

from homework3 import app
from flask_script import Manager

manger=Manager(app)

if __name__=='__mian__':
    manger.run()
