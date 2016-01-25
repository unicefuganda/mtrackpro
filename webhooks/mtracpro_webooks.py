#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Sekiwere Samuel"

import web
import psycopg2
import psycopg2.extras
import logging
import requests
import json
import datetime
import re
from settings import conf, MAPPING, XML_TEMPLATE, DEFAULT_DATA_VALUES  # conf is a dictionary with our settings

urls = (
    "/cases", "Cases",
    "/deaths", "Deaths",
    "/dhis2queue", "Dhis2Queue",
    "/test", "Test",
)
app = web.application(urls, globals(), True)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(process)d] %(levelname)-4s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='/var/log/webhooks/access.log',
    filemode='a')

# Helper functions

API_URL = 'http://localhost:8000/api/v1/'
CASES_POSITIONS = {
    'ma': 0, 'dy': 1, 'sa': 2, 'af': 3, 'ae': 4, 'ab': 5, 'mg': 6, 'ch': 7, 'gw': 8,
    'me': 9, 'nt': 10, 'vf': 11, 'pl': 12, 'tf': 13, 'yf': 14, 'tb': 15, 'md': 16, 'pd': 17
}
DELIMITER = '.'
KEYWORDS_DATA_LENGTH = {
    'cases': 16,
    'death': 18,
}

# connection to queue DB for DHIS2 requests
conn = psycopg2.connect(getattr(
    conf, "queuing_db_connection_string", "dbname=skytools user=postgres"))

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute("SELECT id FROM servers WHERE name = 'dhis2'")
res = cur.fetchone()
serverid = None
if res:
    serverid = res['id']


def get_reporting_week(date):
    """Given date, return the reporting week in the format 2016W01
    reports coming in this week are for previous one.
    """
    offset_from_last_sunday = date.weekday() + 1
    last_sunday = date - datetime.timedelta(days=offset_from_last_sunday)
    year, weeknum, _ = last_sunday.isocalendar()
    return "%sW%d" % (year, weeknum)


def parse_message(msg, kw=""):
    msg = msg.strip().lower()
    separators = []
    segments = []
    separator = DELIMITER or '\\s'
    search_str = '[%s]+' % separator
    match = re.search(search_str, msg)
    while match:
        segment = msg[0:match.start()]
        separator = msg[match.start():match.end()]
        segments.append(segment)
        separators.append(separator)
        msg = msg[match.end():]
        match = re.search(search_str, msg)
    segments.append(msg)

    # remove empty segments
    stripped_segments = []
    for segment in segments:
        segment = segment.strip()
        if len(segment):
            stripped_segments.append(segment)

    # do more cleaning here for stuff like ma2 instead of ma.2

    if not len(segments) % 2 == 0:
        return "not all commands have a value"
    command_value_pairs = []
    dummy_resp = ['0' for i in range(KEYWORDS_DATA_LENGTH[kw])]

    for idx, segment in enumerate(segments):
        if segment in CASES_POSITIONS:
            cmd = segment
            if (idx + 1) <= (len(segments) - 1):
                val = segments[idx + 1]
                dummy_resp[CASES_POSITIONS[segment]] = val
            else:
                # return an error
                val = 0
            command_value_pairs.append((cmd, val))
        else:
            continue
    print segments
    return '.'.join(dummy_resp)


def post_request(data, url=conf['default_api_uri']):
    response = requests.post(url, data=data, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token %s' % conf['api_token']})
    return response


def get_request(url):
    response = requests.get(url, headers={
        'Content-type': 'application/json',
        'Authorization': 'Token %s' % conf['api_token']})
    return response


def get_available_fields():
    response = requests.get(
        '%sfields.json' % API_URL, headers={
            'Content-type': 'application/json',
            'Authorization': 'Token %s' % conf['api_token']})
    results = [k['key'] for k in json.loads(response.text)['results']]
    return results


def add_reporter_fields():
    our_fields = [
        {'label': 'facility', 'value_type': 'T'},
        {'label': 'facilityuuid', 'value_type': 'T'},
        {'label': 'district', 'value_type': 'I'},
        {'label': 'village', 'value_type': 'T'},
    ]
    fields = get_available_fields()
    for f in our_fields:
        if f['label'] not in fields:
            res = post_request(
                json.dumps(f), '%sfields.json' % API_URL)
            print res.text


def push_reporters():
    # with open('test.csv') as f:
    with open('reporters.csv') as f:
        for l in f:
            fields = {}
            val = l.strip().split('#')
            name = val[0] if val[0] != '#' else ''
            phone = '+' + val[1]
            if len(phone) >= 12:
                fields['district'] = val[2]
                fields['facility'] = val[3] if val[3] != '#' else ''
                fields['facilityuuid'] = val[6] if val[6] != '#' else ''
                data = {
                    "name": name, "phone": phone, "language": "eng",
                    "groups": val[4].split(","),
                    "fields": fields
                }
                post_data = json.dumps(data)
                res = post_request(post_data)
                # print post_data
                print res.text


def queue_submission(serverid, post_xml, year, week):
    """Queue request and return True if successfully queued"""
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute(
            "INSERT INTO requests (serverid, request_body, week, year) "
            "VALUES(%s, %s, %s, %s)", (serverid, post_xml, week, year))
        conn.commit()
    except:
        return False
    return True


class Cases:
    def GET(self):
        return json.dumps({"message": "0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0"})

    def POST(self):
        params = web.input()
        values = json.loads(params['values'])  # only way we can get out Rapidpro values in webpy
        msg_list = [v.get('value') for v in values if v.get('label') == 'msg']
        if msg_list:
            msg = msg_list[0]
            if msg.startswith('.'):
                msg = msg[1:]
        # print msg
        message = parse_message(msg, 'cases')

        return json.dumps({"message": message})


class Deaths:
    def GET(self):
        return json.dumps({"message": "0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0"})

    def POST(self):
        params = web.input()
        values = json.loads(params['values'])  # only way we can get out Rapidpro values in webpy
        msg_list = [v.get('value') for v in values if v.get('label') == 'msg']
        if msg_list:
            msg = msg_list[0]
            if msg.startswith('.'):
                msg = msg[1:]
        # print msg
        message = parse_message(msg, 'death')

        return json.dumps({"message": message})


class Test:
    def GET(self):
        return json.dumps({"message": "1.2.3"})

    def POST(self):
        return json.dumps({"message": "1+0+3+4+5+6+7+8+9+10+11+12+13+14+15+16.0.0"})


class Dhis2Queue:
    def GET(self):
        return json.dumps({"status": "success"})

    def POST(self):
        params = web.input(facilityuuid="", form="")
        print params.facilityuuid
        print params.phone
        values = json.loads(params['values'])  # only way we can get out Rapidpro values in webpy
        dataValues = ""
        if params.facilityuuid:
            for v in values:
                val = v.get('value')
                try:
                    val = int(float(val))
                except:
                    pass
                label = v.get('label')
                if val and val.__str__().isdigit():
                    slug = "%s_%s" % (params.form, label)
                    print "%s=>%s" % (slug, val), MAPPING[slug]
                    dataValues += (
                        "<dataValue dataElement='%s' categoryOptionCombo="
                        "'%s' value='%s' />\n" %
                        (MAPPING[slug]['dhis2_uuid'], MAPPING[slug]['dhis2_combo_id'], val))
            if not dataValues and params.form in ('cases', 'death'):
                dataValues = DEFAULT_DATA_VALUES[params.form]

            if dataValues:
                args_dict = {
                    'complete_date': datetime.datetime.now().strftime("%Y-%m-%d"),
                    'period': get_reporting_week(datetime.datetime.now()),
                    'orgunit': params.facilityuuid,
                    'datavales': dataValues
                }

                post_xml = XML_TEMPLATE % args_dict
                year, week = tuple(args_dict['period'].split('W'))
                print post_xml
                # now ready to queue to DB for pushing to DHIS2
                resp = queue_submission(serverid, post_xml, year, week)
                print "Resp:", resp

        return json.dumps({"status": "success"})


# print get_available_fields()
# add_reporter_fields()
# push_reporters()

if __name__ == "__main__":
    app.run()
application = app.wsgifunc()
wsgiapp = app.wsgifunc()
