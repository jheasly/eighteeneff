#! /usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: use stdout instead of print
# TODO: maybe a regex for zips.csv hunting!
# TODO: maybe datasette!

import csv
import pprint

def get_zipcode_rate_area(zipcode):
    '''
    Given a zipcode string

    '64148'
    
    returns a list of the state abbreviation, rate_area, and plan type
    
    ['MO', '3', 'Silver']

    '''

    # the biggest, turdiest .csv file of them all ... 
    with open('data/zips.csv', 'r') as zipcode_rate_areas:
        zipcode_rate_areas_reader = csv.reader(zipcode_rate_areas)
        for zipcode_rate_area_row in zipcode_rate_areas_reader:
            if zipcode in zipcode_rate_area_row:
                return [
                    zipcode_rate_area_row[1],
                    zipcode_rate_area_row[-1],
                    'Silver',
                ]

def get_plans(zipcode_plan_area_iter):
    '''
    Given state abbreviation, rate_area and plan type strings

    ['MO', '3', 'Silver']
    
    returns a second lowest cost silver plan:
    
    '245.2'
    
    '''

    with open('data/plans.csv') as plans:
        plans_reader = csv.reader(plans)
        silver_plans = []
        for plan_row in plans_reader:
            if set(zipcode_plan_area_iter).issubset(plan_row):
                silver_plans.append(plan_row[-2])
        if silver_plans:
                # remove dupes
                silver_plans = list(set(silver_plans))
                # sort
                silver_plans.sort()
                try:
                    return silver_plans[1]
                except IndexError:
                    return None
        else:
            return None

def main():
    with open('data/slcsp.csv', 'r') as slcsp_zipcodes:
        zipcodes_reader = csv.reader(slcsp_zipcodes)
        first_row = next(zipcodes_reader)
        print('{},{}'.format(first_row[0], first_row[1]))
        for zipcode_row in zipcodes_reader:
            slcsp = get_plans(get_zipcode_rate_area(zipcode_row[0]))
            try:
                print('{},{:.2f}'.format(zipcode_row[0], float(slcsp)))
            except TypeError:
                print('{},'.format(zipcode_row[0],))

if __name__ == '__main__':
    main()
