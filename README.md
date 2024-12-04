# RAG Testing for Riya and Sam

## A Brief Overview

Welcome! This RAG APP utilizes Hugging Face LLMs and ORCD/general cluster documentation to build a RAG system. A RAG model [https://arxiv.org/abs/2005.11401] is a sort of augmented LLM which utilizes context provided by existing knowledge on a topic to inform its response. This has been shown to greatly reduce hallucinations and increase the accuracy of models.

## Running Your Own ORCD RAG Server

First, you'll want to get on a GPU compute node in Engaging/Satori etc. To do this, run `salloc -N 1 -n 1 --gres=gpu:1 -p mit_normal_gpu --nodelist=nodename`. Note down the number of the node allocated to you; for example, `node2804` has number `2804`.

### Getting a Hugging Face token
In both cases, to run app.py, you'll need to get a Hugging Face token. Create a Hugging Face account at [https://huggingface.co/welcome] and then follow this URL [https://huggingface.co/docs/hub/en/security-tokens] to make a **fine-grained** Hugging Face token. 

Note that some of the Hugging Face LLMs are gated; to run these, you'll need to request access to use the models on the Hugging Face website, which is usually granted within a few hours. Specifically, request access to Llama-3.1-8B-Instruct at [https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct]. Some of the model options available on the app are not gated, so you can use those initially.


### Option 1: Quick & Convenient
Pull this docker image from Dockerhub at [] using `apptainer pull [.]` Even better, use the SIF file `...` in the repository. 

Now, start a container based on this image using the command `apptainer run [.]` Before doing this, make sure you have a Hugging Face token (instructions on this above). This command will run the image, automatically pulling the RAG code/vectorstores. Now, set the `access_token` variable in the app.py file to your HF token. Then, simply run app.py: `flask --app app run --host=0.0.0.0.` This will download our default model and start a Flask server on an available local port.

Finally, open a new terminal (off the compute node) and tunnel into the container using the command `ssh -L 5000:node[number]:8080 -l [username]@eofe10.mit.edu`. Fill in `number` and `username`. Now, you can go to [http://localhost:5000] and interact with the app.

### Option 2
Download this repository. Create your own python environment with `python -m v [env_name].` Pip install the requirements file: `python -m pip install -r requirements.txt`. Now, simply run app.py: `flask --app app run --host=0.0.0.0.` This will download our default model and start a Flask server on an available local port. Now, you can go to [http://localhost:5000] and interact with the app.

## Next Plans

The app will soon enable you to access different vectorstores containing various cluster documentation.

Currently, running inference is a little bit slow. We're currently looking into ways we could quantize models to make them a little bit faster or send our Slurm jobs to run on GPU. Downloading models if you choose to switch models probably is the most inconvenient. We are trying to see if we might be able to cache models somehow, or begin downloading in the background while the user is interacting with the existing models.
