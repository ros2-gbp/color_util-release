from setuptools import setup

package_name = 'color_util'

setup(
    name=package_name,
    version='1.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    license='BSD',
    author='David V. Lu!!',
    author_email='david@metrorobots.com',
    description='An almost dependency-less library for converting between color spaces',
)
