# Project Phase 1

(historic and real-time databases are "MongoDB databases as a service", deployed and hosted by AWS)

## Instructions for running historic database :


- `virtualenv $HOME/venv`
- `source $HOME/venv/bin/activate`
- `pip install pandas pymongo googlefinance.client`
- `python historic_database.py` 

## Instructions for running real-time database using cron (UNIX only): 

- sudo crontab -e
```
SHELL=/bin/sh
MAILTO=<username>
*/1 * * * * $PATH_TO_GIT/my_script.sh >> $PATH_TO_OUTPUT/out.log 2>&1
```

- `vi $PATH_TO_GIT/my_script.sh`
- `modify $PATH_TO_GIT`

### To access db from shell:

- (make sure MongoDB is installed)
- `mongo ds027729.mlab.com:27729/historic_database -u user -p user`
- `use historic_database`
- `show collections`

### Additional commands for queries

- `db.<collectionname>.find()`
- `db.<collectionname.find().sort({Timestamp: -1})`
- `db.<collectionname>.find().sort({Timestamp: -1}).limit(1)`

### To store each collection as .json:

- launch mongo from terminal, open new terminal: 

- `mongoexport -c <collection_name> --uri=mongodb://user:user@ds027729.mlab.com:27729/historic_database --out historic_<collection_name>_stocks.json`


### To clean-up collections:

`python cleanup.py`
