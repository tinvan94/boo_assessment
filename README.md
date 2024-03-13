# **Installment**
System is the core backend system that is powered by Python.

## 1.0 Pre-requisites
Install Python and these databases

1. Python 3.9.11
   - Install 3.9.11: pyenv install 3.9.11
   - Switch to 3.9.11: pyenv global 3.9.11 => check we are using it: python -V == 3.9.11
   - Install pipenv for 3.9.11: pip install pipenv
   - Create .venv for 3.9.11: pipenv install

2. Mongo
    * Use official Mongo instructions (https://www.mongodb.com/docs/manual/administration/install-community/)
    * System will automatically create the database and collections necessary.


#### 2.0 create local configuration files
```
cd $REPOSITORY_ROOT
cp .env.sample  .env
```