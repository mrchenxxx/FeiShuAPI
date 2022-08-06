from setuptools import setup, find_packages

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()


setup(name='feishuapi',
      version='0.0.10',
      description='Python feishu API SDK',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='taitai',
      author_email='834482351@qq.com',
      url='https://github.com/mrchenxxx/FeiShuAPI',
      license='MIT',
      packages=find_packages(),
      keywords=["python-feishu", "feishu", "lark", "飞书"],
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',

      )
