from setuptools import setup

setup(
    name="demo1",
    version="1.0",
    py_modules=[],
    include_package_data=True,
    install_requires=["click"],
    entry_points='''
        [console_scripts]
        cooldb=demo:cli
    '''
)
