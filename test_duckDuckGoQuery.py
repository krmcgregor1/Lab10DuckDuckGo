# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:02:59 2020

@author: KaiMcGregor
"""
import pytest
import requests


url = 'https://api.duckduckgo.com'
params = {'q':'presidents of the united states.', 'format':'json'}
r = requests.get(url, params=params)
PRESIDENTDUMP = ''.join([x['Text'] for x in r.json()['RelatedTopics'] if 'Text' in x.keys()])




@pytest.mark.parametrize('president_name', ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren', 
                                            'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
                                            'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison',
                                            'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge',
                                            'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon',
                                            'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump'])
def test_president_names(president_name):
    assert president_name in PRESIDENTDUMP