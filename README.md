![plot](https://drive.google.com/uc?id=138qQPk8hAyeOuNA8ddow3ksZIt0g97gh)

<div align="center">

![License](https://img.shields.io/github/license/BodduSriPavan-111/kitikiplot?color=green)

</div>

# diemsim
<b>diemsim</b> is an optimized Python library to compute "Dimension Insensitive Euclidean Metric (DIEM)", surpassing Cosine similarity for multidimensional comparisons.
<span style="color: blue;"><b>Benchmarking</b></span>

### Latency Benchmarking
Our proposed approaches, </br>
**Compact Vectorization** optimizes latency of the existing function 'DIEM_Stat' by around **46.50%** </br>
![plot](https://drive.google.com/uc?id=1KsxawZw4swPKCPPhUq5yHEQKXzL99tRC)
**Compact Optimized getDIEM** optimizes latency of the existing function 'getDIEM' by **34.27%**
![plot](https://drive.google.com/uc?id=1lTNe5HZDDpjeyKslT-TqDhtW6KdUqVpy)

### Getting Started
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

S1= np.random.rand(N, 1) * (maxV - minV) + minV
S2= np.random.rand(N, 1) * (maxV - minV) + minV

# Initialize DIEM
diem= DIEM( N= N, maxV= maxV, minV= minV, n_iter= n_iter ) 

# Compute DIEM value
value= diem.sim( S1, S2)

print( "Output Value: ", value )
```
Find <b>Quick Start</b> notebook [here](https://github.com/BodduSriPavan-111/diemsim/blob/dev/examples/Quickstart_Usage_Guide.ipynb)

### Key Contributors
<a href="https://www.linkedin.com/in/boddusripavan/"> Boddu Sri Pavan </a>, 
<a href="https://www.linkedin.com/in/chandrasheker-t-44807015/"> Chandrasheker Thummanagoti </a>  </br>

Please refer <a href="https://github.com/BodduSriPavan-111/diemsim/blob/dev/CONTRIBUTING.md">CONTRIBUTING.md</a> for <b>contributions</b> to <i>diemsim</i>

## Acknowledgement
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

## To cite our Python library

> Our citation

## Thank You !
