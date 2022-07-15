from setuptools import setup

package_name = 'ros2_sealer_driver'
submodule = 'ros2_sealer_driver/drivers'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodule],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rpl',
    maintainer_email='sanjivp27@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sealerNode = ros2_sealer_driver.sealerNode:main'
        ],
    },
)
