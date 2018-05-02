from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='rest_vk_api',
      packages=['rest_vk_api'],
      description='REST VK API',
      long_description=readme,
      version='1.0',
      url='https://github.com/vadimk2016/rest-vk-api',
      author='Vadim Kuznetsov',
      author_email='vadim.kuznyetsov@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3',
          'Topic :: Internet'
      ],
      keywords='rest-vk-api',
      python_requires='>=3',
      install_requires=[
          'beautifulsoup4==4.6.0',
          'certifi==2018.4.16',
          'chardet==3.0.4',
          'idna==2.6',
          'requests==2.18.4',
          'urllib3==1.22',
          'v-vk-api==1.3',
          'Django==2.0.4',
          'django-rest-framework==0.1.0',
          'djangorestframework==3.8.2',
          'idna==2.6',
          'pytz==2018.4',
      ],
      )
