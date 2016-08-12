# The Swear-Jar
Continuos speech recognition for the swear jar in da office

## TODO
* add more swear words
* maybe a unique JAR instead of multiple ? 

### Check the status
[https://swear-jar-office.herokuapp.com/swear/](https://swear-jar-office.herokuapp.com/swear/)

### How to run

* Download the package and go inside the **swear** folder

* Edit the ```swear_jar.py``` and insert your name with the capital initial letter
```python
payload = {
    'name': 'Your name'
}
```
* In the terminal run: 
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python swear_jar.py
```
