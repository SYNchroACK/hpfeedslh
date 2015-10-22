## Sections

1. [Approach Explanation](#approach)
2. [HPFeeds Module Evaluation in Honeypots](#evaluation)
3. [Run Example](#run-example)
4. [TODO](#todo)

* * *

<a name="approach"></a>
### Approach Explanation

**Problem:** the lack of events harmonization is an issue for hpfeeds consumers.

**Approach:** in order to solve this problem, hpfeeds should provide to honeypot developers:
* library to generate harmonized events, based on the honeypot custom harmonization configuration
* library to easily connect to hpfeeds broker and send the harmonized events
* document to easily take advantage of the above libraries

**Benefit:** in consumer prespective, they just need to read the harmonization configuration from each honeypot to know exactly which fields will be sent to them through hpfeeds.

* * *

<a name="evaluation"></a>
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

* * *

<a name="run-example"></a>
### Run Example

```
git clone https://github.com/SYNchroACK/hpfeedslh
cd hpfeedslh/
python example.py
```

* * *

<a name="todo"></a>
### TODO

* replace json configuration to xml (will have the possibility to define configuration version)
* create documentation for honeypot developers
* check current hpfeeds library:
```
https://github.com/rep/hpfeeds/blob/master/lib/hpfeeds.py
```
* check the following code (publisher):
```
https://github.com/mushorg/glastopf/blob/master/glastopf/modules/reporting/auxiliary/log_hpfeeds.py
```

* check the following code (consumer):
```
https://github.com/johnnykv/mnemosyne/blob/master/feedpuller/feedpuller.py
https://github.com/johnnykv/mnemosyne/blob/master/persistance/mnemodb.py
```
