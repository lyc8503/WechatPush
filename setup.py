import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wechat_push",
    version="1.0.1",
    author="lyc8503",
    author_email="lyc8503@foxmail.com",
    description="Push your messages to wechat easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyc8503/WechatPush",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.27.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)
