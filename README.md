This project is a minimal implementation of the [nbgallery](https://github.com/nbgallery/nbgallery) server and APIs in order to understand the set of endpoints in [nbgallery/controllers](https://github.com/nbgallery/nbgallery/tree/master/app/controllers) and facilitate development of Jupyter notebook extensions.  

I am not 100% comfortable reading/writing/understanding either Javascript or Ruby, and if you aren't either, than this project might help you better understand the `nbgallery` server and the Jupyter `nbextensions` that connect Jupyter to the Gallery.


#### Endpoints
So far in this package the endpoints defined are:

 * GET to `/`, returns links to `/environments` and `/notebooks`
 * GET to `/environments`, returns a json list of environments (`{name, url}`)
 * POST to `/environments` with `{name, url}` to create a new environment in `environments.json` table
 * GET to `/notebooks`, returns an html list of notebooks
 * GET to `/notebooks/<uuid>`, returns a json blob of notebook metadata and content
 * POST to `/stages` with `{title, description, notebook}`, creates a new notebook in `notebooks.json` table and returns a uuid
 
 
#### Databases
When the Docker container is first started, it creates two [`tinydb`](https://tinydb.readthedocs.io/en/latest/index.html) tables (`environments.json` and `notebooks.json`) with example records.  The databases are stored in the same container as the webserver for this minimal example project (unlike `nbgallery`).

#### Docker container
To run this Docker container in a development / interactive mode, clone this repo and build/run the Docker file.

```
git clone https://github.com/nbgallery/nbgallery-api-python
cd nbgallery-api-python
docker build -t nbgallery_api . && docker run -it -p 5000:5000 nbgallery_api
```


#### Test notebook
Once the Docker container is running, the `API test notebook.ipynb` should work to get a list of environments, register a new environment in the database, get a list of notebooks, and create a new notebook in the database.  