# Flask Blog
#### This is an online platform where a user can write his own blogs, read blogs from other users, comment on blogs as well as maintain their own profiles by deleting personal blog articles or deleting comments on their own blogs., 08/07/2019


## Description
This is an online platform where a user can write his own blogs, read blogs from other users, comment on blogs as well as maintain their own profiles by deleting personal blog articles or deleting comments on their own blogs.
#### Link to deployed site


## Table of content
1. [Description](#description)
2. [Setup and installations](#setup-and-installations)
3. [Contributing](#contributing)
4. [Bugs](#bugs)
5. [Contact me](#support-and-contact-details)
6. [Licensing](#license)


## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `chmod a+x start.py`
* On your terminal run `./start.py`
* Access the live site using the local host provided

#### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Flask

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/JamesMutahi/flask-blog.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
DEBUG=True
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:5000](http://127.0.0.1:5000/)


## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs
Create an issue mentioning the bug you have found

#### Known bugs
 - N/A



## Support and contact details
Contact [James Mutahi](wilsenock220@gmail.com) for further help/support

### License
[MIT LICENSE](LICENCE)

Copyright (c)2018 **Wilstan Onditi**