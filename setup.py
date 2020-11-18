import setuptools

setuptools.setup(
    name="templated-dictionary",
    version="1.0",
    author="Miroslav Suchý",
    author_email="msuchy@redhat.com",
    description="Dictinary with Jinja2 expansion",
    long_description="""Dictionary where __getitem__() is run through Jinja2 template.""",
    long_description_content_type="text/markdown",
    url="https://github.com/xsuchy/templated-dictionary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv2+",
        "Operating System :: OS Independent",
    ],
    license='GPLv2+',
    packages=['templated-dictionary'],
    include_package_data=True,
    zip_safe=False,
)
