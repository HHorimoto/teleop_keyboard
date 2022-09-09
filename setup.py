from setuptools import setup
import os
from glob import glob

package_name = 'teleop_keyboard'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Hiroto Horimoto',
    maintainer_email='81685394+HHorimoto@users.noreply.github.com',
    description='This package is for control robot with keyborad ROS2',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_keyboard = teleop_keyboard.teleop_keyboard:main'
        ],
    },
)
