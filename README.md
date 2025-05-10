![plot](https://drive.google.com/uc?id=138qQPk8hAyeOuNA8ddow3ksZIt0g97gh)

<div align="center">

![PyPI](https://img.shields.io/pypi/v/diemsim?color=blueviolet)
[![PyPI Downloads](https://static.pepy.tech/badge/diemsim)](https://pepy.tech/projects/diemsim)
![Built with NumPy](https://img.shields.io/badge/Built%20with-NumPy-gold?logo=numpy&logoColor=gold)
[![DOI](https://zenodo.org/badge/973683630.svg)](https://doi.org/10.5281/zenodo.15351274)
![License](https://img.shields.io/github/license/BodduSriPavan-111/kitikiplot?color=success)

</div>

# diemsim
<b>diemsim</b> is an optimized Python library to compute "Dimension Insensitive Euclidean Metric (DIEM)", surpassing Cosine similarity for multidimensional comparisons.

## Latency Benchmarking
Our proposed approaches, </br>
**Compact Vectorization** optimizes latency of the existing function 'DIEM_Stat' by around **46.50%** </br>
![plot](https://drive.google.com/uc?id=1KsxawZw4swPKCPPhUq5yHEQKXzL99tRC)
**Compact Optimized getDIEM** optimizes latency of the existing function 'getDIEM' by **34.27%**
![plot](https://drive.google.com/uc?id=1lTNe5HZDDpjeyKslT-TqDhtW6KdUqVpy)

## Getting Started
Install the package via pip:
```
pip install diemsim
```
#### Usage
```py
from diemsim import DIEM

N= 12
maxV= 1
minV= 0
n_iter= int(1e5)

S1= np.random.rand(N) * (maxV - minV) + minV
S2= np.random.rand(N) * (maxV - minV) + minV

# Initialize DIEM
diem= DIEM( N= N, maxV= maxV, minV= minV, n_iter= n_iter ) 

# Compute DIEM value
value= diem.sim( S1, S2)

print( "Output Value: ", value )
```
Find <b>Quick Start</b> notebook [here](https://github.com/BodduSriPavan-111/diemsim/blob/dev/examples/Quickstart_Usage_Guide.ipynb)

## Key Contributors
<a href="https://www.linkedin.com/in/boddusripavan/"> Boddu Sri Pavan </a>, 
<a href="https://www.linkedin.com/in/chandrasheker-t-44807015/"> Chandrasheker Thummanagoti </a>  </br>

Please refer <a href="https://github.com/BodduSriPavan-111/diemsim/blob/dev/CONTRIBUTING.md">CONTRIBUTING.md</a> for <b>contributions</b> to <i>diemsim</i>

## To cite our Python library
BibTeX
> @software{diemsim,  </br>
>  title        = {diemsim: A Python Library Implementing Dimension Insensitive Euclidean Metric (DIEM)},  </br>
>  author       = {Boddu Sri Pavan, Chandrasheker Thummanagoti},  </br>
>  year         = {2025},  </br>
>  publisher    = {Zenodo},  </br>
>  version      = {v1.0.0},  </br>
>  doi          = {10.5281/zenodo.15351274},  </br>
>  url          = {https://doi.org/10.5281/zenodo.15351274}  </br>
> }

APA
> BodduSriPavan111. (2025). BodduSriPavan-111/diemsim: Initial Release (v0.0.1). Zenodo. https://doi.org/10.5281/zenodo.15351275

## Acknowledgements
BibTeX
> @misc{tessari2025surpassingcosinesimilaritymultidimensional,  </br>
>      title={Surpassing Cosine Similarity for Multidimensional Comparisons: Dimension Insensitive Euclidean Metric},   </br>
>      author={Federico Tessari and Kunpeng Yao and Neville Hogan},  </br>
>      year={2025},  </br>
>      eprint={2407.08623},  </br>
>      archivePrefix={arXiv},  </br>
>      primaryClass={cs.LG},  </br>
>      url={https://arxiv.org/abs/2407.08623},   </br>
>}

## Thank You !
