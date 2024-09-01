**DJANGO CHARITY SITE**

![5380108367386765337](https://github.com/user-attachments/assets/c0025cd8-7140-43fa-b0c6-7c2aa505fc85)


In this project I made a functional website with various interesting features, such as:
- Stripe Donations
- Blog with search, category and tag filters
- Custom Information and custom Social Icons

How to run this project:

*Firstly*, you will need Python, but let's imagine that you already have it.

*Secondly*, you will need virtual environment

How to create a virtual python environment:

1. Pick a folder for a project
2. Use

```python -m venv venv``` for Windows or

```python3 -m venv venv``` for Linux.

3. Enter your vitrual environment ```source test/bin/activate``` for Linux or

```test/Scripts/activate.bat``` In Windows CMD 

```test/Scripts/Activate.ps1``` In Windows Powershell

Now we can set up my project:

1. ```git clone https://github.com/JuicyS8da/Django_Charity``` (to your folder)
2. ```pip install -r requirements.txt```
3. Rename ```.env-example``` to ```.env```
4. Create new django project key, or open settings.py in "charity" folder and change SECRET_KEY to get_random_secret_key() 
5. ```python manage.py runserver```
6. Put http://127.0.0.1:8000/ into url field in your browser
7. (optional) If you want to user django admin http://127.0.0.1:8000/admin/, default superuser is:

Login: admin

Password: 123

or you can create your own superuser by putting this command into your console:
```python manage.py createsuperuser```
