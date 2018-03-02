# Project Phase 1

(historic and real-time databases are "MongoDB databases as a service", deployed and hosted by AWS)

## Instructions for running historic database (UNIX commands):

- `cd home` 
- `git clone git@github.com:jdakka/568_project_phase_1.git` 
- `virtualenv $HOME/venv`
- `source $HOME/venv/bin/activate`
- `pip install pandas pymongo googlefinance.client`
- `cd 568_project_phase_1` 
- `python historic_database.py` 

## Instructions for running real-time database using cron (UNIX only): 

- `sudo crontab -e`
```
SHELL=/bin/sh
MAILTO=<username>
*/1 * * * * $HOME/568_project_phase_1/my_script.sh >> $HOME/568_project_phase_1/out.log 2>&1

**Make sure you change $HOME into the actual pwd or cron won't know where to look
```

- `vi $PATH_TO_GIT/my_script.sh`
- `modify $PATH_TO_GIT`

### To access db from shell:

- (make sure `mongo` is installed)
- Access historic_database: `mongo ds027729.mlab.com:27729/historic_database -u user -p user`
- Access realtime_database: `mongo ds151508.mlab.com:51508/realtime_database -u user -p user`
- `use historic_database` or `use realtime_database` 
- `show collections`

### Additional commands for queries

- `db.<collectionname>.find()`
- `db.<collectionname.find().sort({Timestamp: -1})`
- `db.<collectionname>.find().sort({Timestamp: -1}).limit(1)`

### To store each collection as .json:

- launch `mongo` from terminal, open new terminal: 

- `mongoexport -c <collection_name> --uri=mongodb://user:user@ds027729.mlab.com:27729/historic_database --out historic_<collection_name>_stocks.json`


### To clean-up collections:

`python cleanup.py`
