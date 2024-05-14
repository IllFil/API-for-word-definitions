import definition

import json
import justpy as jp
class API:

    @classmethod
    def serve(cls,req):
        try:
            wp = jp.WebPage()
            word = req.query_params.get('w')

            if not word:
                # If 'w' parameter is missing, raise a BadRequestError
                raise jp.BadRequestError("Missing 'w' parameter")

            defined = definition.Definition(word).get()

            if not defined:
                # If no definition was found, return a custom error response
                error_response = {
                    "error": "Definition not found for the word '{}'".format(word)
                }
                # Set an appropriate HTTP status code (e.g., 404 for Not Found)
                wp.status_code = 404
            else:
                # If a definition was found, create the response dictionary
                response = {
                    "word": word,
                    "definition": defined
                }

            # Serialize the response dictionary to JSON and assign it to the WebPage's HTML content
            wp.html = json.dumps(response)
            return wp
        except Exception as e:
            # If any unexpected error occurs, handle it and return an error response
            error_response = {
                "error": str(e)
            }
            # Create a new JustPy WebPage object for the error response
            error_wp = jp.WebPage()
            # Serialize the error response dictionary to JSON and assign it to the WebPage's HTML content
            error_wp.html = json.dumps(error_response)
            # Set the HTTP status code to indicate the error (e.g., 500 for Internal Server Error)
            error_wp.status_code = 500
            # Return the error WebPage object
            return error_wp