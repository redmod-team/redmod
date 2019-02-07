# Reduced complexity models 

This is a collection of scripts to construct reduced complexity models
based on a blackbox simulation code called at different parameters.

Current functionality covers uncertainty quantification via PCE with 
chaospy as a backend. Support for surrogate models via Gaussian Progress 
Regression is under development.


## HowTo

1. Create a directory `<dir>` containing `redmod_conf.py` and `interface.py` specific for your code.
   If your code is based on text configuration files for each run, copy the according directory to `<dir>/template`
   and replace values of parameters to be varied within UQ/surrogate models by placeholders `{param}`.
   
2. Preprocessing:  
   ```
   python /path/to/redmod.py <dir> uq pre
   ```
   to generate points where model is evaluated, and possibly run directories based on `template`.
   Evaluation points are stored inside `<dir>/run/input.txt`
  
3. Running model: 
   ```
   python /path/to/redmod.py <dir> uq run
   ```
   to start simulations at all the points. If `uq.backend` is of type `PythonFunction`, results
   of model runs are stored in `<dir>/run/output.txt`. Otherwise output is stored in model code-specific format.
  
4. Postprocessing: 
   ```
   python /path/to/redmod.py <dir> uq post
   ```
   to get postprocessing results from UQ via PCE.
   (not fully operational yet)
  
## User-supplied files
* `redmod_conf.py`
  * Set `uq.backend` to a class available inside `redmod.uq` (currently only `ChaosPy` available)
  * Add uncertain parameters and their distributions via `uq.params['<param>'] = <distribution>`
  * Optional: set `run.backend` to a class available inside `redmod.run`
  
* `interface.py`
  * `shape()` should return shape of the model output as a list of integers.
  * `get_output()` should return model output as a numpy array of shape `interface.shape()`.
    The current path is the respective run directory. Can be skipped if `uq.backend` is of type `PythonFunction`.
  
