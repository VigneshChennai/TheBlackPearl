#!/usr/bin/env python

# This file is part of BlackPearl.

# BlackPearl is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BlackPearl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BlackPearl.  If not, see <http://www.gnu.org/licenses/>.

import inspect

from BlackPearl.core.decorators import weblocation, webname
from BlackPearl import application
from BlackPearl.core.exceptions import RequestInvalid
from BlackPearl.core import datatype


@weblocation('/applications')
def applications():
    ret = []
    for app in application.deployed_webapps:
        urls = [url for url in app.webmodules.keys()]
        urls.sort()
        preprocessors = [preprocessor['name'] for preprocessor in app.preprocessors]
        preprocessors.sort(key=lambda prep: prep['name'])
        posthandlers = [posthandler['name'] for posthandler in app.posthandlers]
        posthandlers.sort(key=lambda post: post['name'])
        ret.append({
            "name": app.name,
            "description": app.desc,
            "modules": urls,
            "preprocessors": preprocessors,
            "posthandlers": posthandlers,
            "handlers": app.handlers
        })
        ret = sorted(ret, key=lambda data: data['name'])
    return ret


@weblocation('/signature')
def signature(url):
    """Dummy entry"""
    ret = []

    try:
        webapp = application.modules[url]
    except:
        raise RequestInvalid("The URL <%s> not found" % url)

    _signature = webapp.webmodules[url]['signature']
    desc = webapp.webmodules[url]['desc']

    for arg, value in _signature.parameters.items():
        v = {
            "arg": arg,
            "type": repr(value.annotation),
            "type_def": None,
        }

        annotation = value.annotation

        if annotation is inspect.Signature.empty:
            v['type'] = None

        if isinstance(annotation, datatype.Format) or isinstance(annotation, datatype.FormatList):
            v["type_def"] = annotation.data_format

        elif (isinstance(annotation, datatype.Options)
              or isinstance(annotation, datatype.OptionsList)):
            v["type_def"] = annotation.values

        ret.append(v)

    ts = []
    try:
        _testsets = webapp.testsets[url]
    except:
        pass
    else:
        for testset in _testsets:
            ts.append({
                "name": testset['name'],
                "desc": testset['desc']
            })

    return {"signature": ret, "desc": desc, "testsets": ts}


@weblocation('/testing/testsets')
def testsets(url):
    ret = []

    try:
        webapp = application.modules[url]
    except:
        raise RequestInvalid("The URL <%s> not found" % url)

    _testsets = webapp.testsets[url]
    for testset in _testsets:
        ret.append({
            "name": testset['name'],
            "desc": testset['desc']
        })

    return ret


@weblocation('/testing/run')
def run_testset(url, name):
    try:
        webapp = application.modules[url]
    except:
        raise RequestInvalid("The URL <%s> not found" % url)

    _testset = None
    _testsets = webapp.testsets[url]
    for testset in _testsets:
        if testset['name'] == name:
            _testset = testset
            break

    if _testset:
        return _testset['func']()
    else:
        raise RequestInvalid("The name <%s> not found" % name)


@weblocation('/testing/run_all')
def run_all_testset(url):
    try:
        webapp = application.modules[url]
    except:
        raise RequestInvalid("The URL <%s> not found" % url)

    ret = []
    try:
        _testsets = webapp.testsets[url]
    except KeyError:
        raise RequestInvalid("No testsets found for url <%s>" % url)
    for testset in _testsets:
        ret.append({
            "TestSet": testset['name'],
            "data": testset['func']()
        })
    return ret