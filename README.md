### Run Example

```
git clone https://github.com/SYNchroACK/hpfeedslh
cd hpfeedslh/
python example.py
```

### HPFeeds Module Evaluation in Honeypots

The goals of this evaluation are:
* evaluate if the majority of honeypots are written in python which validate that a harmonization library can be a good approach
* evaluate how currectly honeypots are sending data to hpfeeds

```
[beeswarm]
language = python
repository = https://github.com/honeynet/beeswarm
hpfeeds_module = not found
```

```
[conpot]
language = python
repository = https://github.com/mushorg/conpot
hpfeeds_module = https://github.com/mushorg/conpot/blob/master/conpot/core/loggers/hpfriends.py
```

```
[dionaea]
language = python
repository = https://github.com/rep/dionaea/
hpfeeds_module = https://github.com/rep/dionaea/blob/master/modules/python/scripts/hpfeeds.py
```

```
[glastopf]
language = python
repository = https://github.com/mushorg/glastopf/
hpfeeds_module = https://github.com/mushorg/glastopf/blob/master/glastopf/modules/reporting/auxiliary/log_hpfeeds.py
```

```
[thug]
language = python
repository = https://github.com/buffer/thug/
hpfeeds_module = https://github.com/buffer/thug/blob/master/hpfeeds/hpfeeds.py
```


