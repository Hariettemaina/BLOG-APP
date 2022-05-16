# Blog

 A personal Blog where users can subscribe, post and comment on articles posted.

## Author

 **Hariette Maina**



## Description

 This is an app that allows users to view and submit blogs. A web application where users will submit their blogs and other users will leave comments to give their feedback on them.

## User Stories

As a user I would like:

> * to view the blog posts submitted
> * to comment on blog posts
> * to view the most recent posts
> * to be alerted when a new post is made by joining a subscription.
> * to sign in to the blog.
> * to create a blog from the application.
> * to delete comments that I find insulting or degrading.

## How to use it

> * Internet connection
> * Click jolly-blogs.herokuapp.com) <br/>
  or <br/>
> * Copy jolly-blogs.herokuapp.com) and  Paste the link on your prefered browser

## How it works

> * A user can sign up
> * A user can subscribe to receive email notifications
> * A user can also post comments and articles.

## Technologies Used

> * Python3.8
> * Flask framework
> * Bootstrap and Css
> * PostgreSQL
> * SQLAlchemy

## Setup/Installation Requirements

### Prerequisites

> * Internet access
> * ```git clonehttps://github.com/Hariettemaina/BLOG-APP```
> * ```cd Blog```

#### To install a virtual environment

> * ```pip install pipenv`` 
> * ```python3.8 manage.py shell```

#### To install all dependencies

> * ```python3.8 -m pip install -r requirements.txt```

#### To change the config_name parameter from 'production' to 'development'

> * Inside the manage.py module  i.e:- ```app = create_app('production')``` should be ```app = create_app('development')```
> * Then run ```python3.8 manage.py server``` to get the app running  navigate to ```http://127.0.0.1:5000/``` and it will open in your browser

## Dependancy Installments

> * pipenv install python3.8
> * pipenv  install flask
> * pipenv install flask-bootstrap
> * pipenv  install flask-script
> * pipenv install flask-wtf
> * pipenv  install flask-migrate
> * pipenv  install flask-login
> * pipenv  install Flask-Mail
> * pipenv install flask-uploads



## Support and Contact Details

> You can reach out to me at hariettemaina@gmail.com
for Reviews, Advice, Collaborations and Comments

## Licence

MIT License

Copyright (c) 2022 **Hariettemaina**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

> --------------------------------------------------------