evaporative-demand-drought-index
================================

A simple package for calculating the Evaporative-Demand-Drought-Index (EDDI).


Installation
------------

For now clone and pip install,

.. code-block:: bash

   git clone https://github.com/WSWUP/evaporative-demand-drought-index.git


It is recommended to use the provided conda environment file to handle dependencies as opposed to pip, so before installing (below) move to the the root directory and install and activate the virtual environment:

.. code-block:: bash

   conda env create -f environment.yml
   conda activate eddi

next install using pip,

.. code-block:: bash

   pip install -e .

If all went well the ``eddi`` package should be added to your Python path and you should be able to run the following without errors:

.. code-block:: python

   from eddi import EDDI, eddi_1d
