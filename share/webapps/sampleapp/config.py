#!/bin/env python

########################################################################################################################
#                                    BlackPearl Application configuration file
#
# Full Name = "Tesing"
# Author = "sdf"
# Website = "saf"
# Email ID = "sdf"
#
########################################################################################################################

name= "sampleapp"

# Description: Application Name.
# Example : name = "My First BlackPearl Application"
# Optional: Yes (if not specified: The folder name will be used as application name)

url_prefix="/sampleapp"

# Description: URL Prefix for the web application.
# Example : url_prefix = "/reservation"
# Optional: Yes (if not specified: The folder name will be used as url_prefix)
#
# Note:
#       1. url_prefix should start with '/'. If not, '/' will be automatically prefixed to it with a warning while the
#          server starts.
#       2. if url_prefix=/ then the application will be deployed as root application.
#

handlers = ["sampleapp.handlers"]

# Description: Handlers are the list of python modules which holds the blackpearl web modules.
#
# Example : if python file is (Webapp/handlers.py and in Webapp/login_handlers.py) then
#           handlers = ['Webapp.handler', 'Webapp.login_handlers.py']
#
# Note: Each blackpearl web modules decorated with @weblocation decorate but not defined in the below python modules
#       will be ignored
#

session_enabled = True

# Description: Enables or disables session feature in the webapp.
#
# Example : session_enabled = True

# Note:
#       1. Session are saved in the user browser cookie.
#       2. Sessions are encrypted before saving in cookie, so it safe to save data which are sensitive but try to void
#          saving sensitive data in session.
#       3. Always store less amount of data in session, since it is saved in cookie, server will throw error when
#          storing large data (For example: you can store a string data of size ~2840 bytes maximum).
#

preprocessors = []

# Description: List of python function which need to process the incoming request before handing it to the web modules.
# Example : if preprocessor python functions (ie. functions decorated with @preprocessor decorator)
#           "access_check" and "unique_user_count" defined under Webapp/preprocessors.py file then
#
#           preprocessors = ['Webapp.preprocessors.access_check', 'Webapp.preprocessors.unique_user_count']
#
# Optional: Yes
#
# Note: preprocessors list defined here is for specifying the order of execution only. The python function must be
#       decorated with @preprocessor to define it as preprocessor

posthandlers = []

# Description: List of python function which need to process the outgoing data after the web module handled the request.
# Example : if posthandler python functions (ie. functions decorated with @posthandler decorator)
#           "data_validation_filter" and "data_formatting" defined under Webapp/posthandlers.py file then
#
#           preprocessors = ['Webapp.posthandlers.data_validation_filter', 'Webapp.posthandlers.data_formatting']
#
# Optional: Yes
#
# Note: Posthandlers list defined here is for specifying the order of execution only. The python function must be
#       decorated with @posthandler to define it as posthandler

