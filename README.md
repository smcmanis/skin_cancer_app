## Project Structure

```
.
├── data 
│   └── HAM1000_dataset
│       └── ...
├── skin_cancer 
│   ├── assets
│   ├── model
│   └── app.py
├── ...

```
| Folder/File | Description | 
| ----------- | ----------- |
| data | Contains all datasets  |
| skin_cancer/assets | CSS, JS, images... | 
| skin_cancer/model | CNN stuff |
| skin_cancer/app.py | Manages and run the Dash app |

## Installation
### Prerequisites
- Python 3.1+ and preferably virtual enviornment software (pipenv, venv, etc)
### Install

Clone the repo and enter the directory:
```bash
$ git clone https://github.com/smcmanis/skin_cancer_app.git  
$ cd skin_cancer_app 
```

To install with pip:  
```bash
$ pip install requirements.txt
```

To install with pipenv:  
```bash
$ pipenv shell
$ pipenv install
```


## Run
Start the app:
```bash
$ python skin_cancer_app/app.py
```
Then navigate to http://0.0.0.0:5001/ in a browser. You can access it from any other device on your local network by swapping 0.0.0.0 with the computer's local IP address e.g. http://192.168.0.4:5001/

