from __future__ import print_function

import urllib2

import taskflow.engines
from taskflow.patterns import linear_flow as lf
from taskflow import task


def fetch(url):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    return response.getcode()

def flow_watch(state, details):
    print('flow state:{}'.format(state))
    print('flow details:{}'.format(details))

def task_watch(state, details):
    print('task state:{}'.format(state))
    print('task details:{}'.format(details))

class GoogleFetch(task.Task):
    def execute(self, google_url, *args, **kwargs):
        status_code = fetch(google_url)
        print('Google Response Code: {}'.format(status_code))


class AmazonFetch(task.Task):
    def execute(self, amazon_url, *args, **kwargs):
        status_code = fetch(amazon_url)
        print('Amazon Response Code: {}'.format(status_code))


if __name__ == "__main__":
    flow = lf.Flow('simple-linear').add(
        GoogleFetch(),
        AmazonFetch()
    )

    engine = taskflow.engines.load(flow, store=dict(google_url='https://baidu.com',
                                          amazon_url='http://www.tuicool.com/articles/fAfqMf'))


    engine.notifier.register('*', flow_watch)
    engine.atom_notifier.register('*', task_watch)
    engine.run()
