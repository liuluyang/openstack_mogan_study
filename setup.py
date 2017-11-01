import setuptools

try:
    import multiprocessing

except ImportError:
    pass

setuptools.setup(setup_requires=['pbr>=2.0.0'],pbr=True)
#test by liuluyang-c
