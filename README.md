# TestTask

### Installation and setup
After cloning this repository to your local folder, you can use vagrant for testing.<br />
1. Run command ```vagrant up``` in folder where Vagrantfile is situated. You will have a fully running virtual machine. You can SSH into this machine with ```vagrant ssh```, and when you are done playing around, you can terminate the virtual machine with vagrant destroy. <br />
2. Then go to vagrant folder in you virtual machine (```cd /vagrant```) and install all requirements using ```sudo pip3 install -r requirements.txt``` <br />
3. Than you need to configure you database:<br />
- ```sudo -u postgres psql```
- ```create user mydatabaseuser;```
- ```create database dbtaskbase owner mydatabaseuser;```
- ```\password mydatabaseuser;   (password for this user to db = mypassword)```
- ```python3 manage.py makemigrations```
- ```python3 manage.py migrate```
- ```python3 manage.py createsuperuser```

<br />
4. And than you can run your server:
- using default dev settings ```python3 manage.py runserver 0.0.0.0:8000```
- or exactly with dev settings ```python3 manage.py runserver 0.0.0.0:8000 --settings=TestTask.settings.local```
- or with production settings ```python3 manage.py runserver 0.0.0.0:8000 --settings=TestTask.settings.production --insecure``
<<<<<<< HEAD

=======
>>>>>>> 6df2baf7cec74e7255325082352cb85db70eb85a
