This project is a minimal implementation of the [nbgallery](https://github.com/nbgallery/nbgallery) server and APIs in order to facilitate development of Jupyter notebook extensions.

The primary API features this project captures for nbextension development are:
 * POST from a Jupyter notebook to nbgallery to create a new notebook in nbgallery
 * PUT from a Jupyter notebook to nbgallery to update an existing notebook in nbgallery
 * POST from a Jupyter tree to nbgallery to register a new environment
 * GET to endpoints like `/starred` to auto-download notebooks from Jupyter tree
 * Endpoint in nbgallery server that shows a button to POST from nbgallery to Jupyter API to "run in Jupyter"
 
The features that aren't included in this package but are important for testing still are:
 * In Jupyter, check if current notebook is different from uploaded notebook in gallery and prompt for updates
 