# Import the API module to serve API requests
import api
# Import the documentation module to serve documentation requests
import documentation

import justpy as jp

# Define a route for API requests, pointing to the serve method in the API module
jp.Route("/api", api.API.serve)
# Define a route for requests to the root URL, pointing to the serve method in the documentation module
jp.Route("/", documentation.Doc.serve)
jp.justpy()