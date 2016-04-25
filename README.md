### virtual env

```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### set nltk data dir

From project home

```
mkdir nltk_data
python
>>> import nltk
>>> nltk.download()
press c for configuration
press d for setting data dir
enter full path to project nltk_data dir
press m to return to main menu
press d to enter download menu
type punkt
exit
```

### set nltk_data dir in project

```
vim app/run.py
modify nltk.data.path.append("")
```
