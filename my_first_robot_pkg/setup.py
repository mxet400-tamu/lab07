from setuptools import find_packages, setup

package_name = 'my_first_robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tony Adjartey',
    maintainer_email='tony.adjartey@gmail.com',
    description='MXET 400 - Lab 7: Publishers and Subscribers',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_first_robot_pkg.talker:main',
            'listener = my_first_robot_pkg.listener:main',
            'numbers = my_first_robot_pkg.numbers:main',
            'volume = my_first_robot_pkg.volume:main',
        ],
    },
)
