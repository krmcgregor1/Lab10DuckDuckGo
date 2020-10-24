# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:02:59 2020

@author: KaiMcGregor
"""
import pytest
import requests



@pytest.fixture
def duckDuckGoQuery():
    url = 'https://api.duckduckgo.com'
    params = {'q':'presidents of the united states', 'format':'json'}
    r = requests.get(url, params=params)
    return r.text



@pytest.mark.parametrize('president_name', ['George Washington', 'John Adams', 'Thomas Jefferson', 'James Madison', 'James Monroe', 'John Quincy Adams', 'Andrew Jackson', 'Martin Van Buren', 
                                            'William Henry Harrison', 'John Tyler', 'James K. Polk', 'Zachary Taylor', 'Millard Fillmore', 'Franklin Pierce', 'James Buchanan', 'Abraham Lincoln',
                                            'Andrew Johnson', 'Ulysses S. Grant', 'Rutherford B. Hayes', 'James Garfield', 'Chester A. Arthur', 'Grover Cleveland', 'Benjamin Harrison',
                                            'Grover Cleveland', 'William McKinley', 'Theodore Roosevelt', 'William Howard Taft', 'Woodrow Wilson', 'Warren G. Harding', 'Calvin Coolidge',
                                            'Herbert Hoover', 'Franklin D. Roosevelt', 'Harry S. Truman', 'Dwight D. Eisenhower', 'John F. Kennedy', 'Lyndon B. Johnson', 'Richard M. Nixon',
                                            'Gerald R. Ford', 'James Carter', 'Ronald Reagan', 'George H. W. Bush', 'William J. Clinton', 'George W. Bush', 'Barack Obama', 'Donald J. Trump'])
def test_president_names(duckDuckGoQuery, president_name):
    assert president_name in duckDuckGoQuery