# diemsim
Dimension Insensitive Euclidean Metric

![plot](https://drive.google.com/uc?id=138qQPk8hAyeOuNA8ddow3ksZIt0g97gh)

<div align="center">

![PyPI](https://img.shields.io/pypi/v/kitikiplot?color=blueviolet)
![PyPI - Downloads](https://img.shields.io/pypi/dm/kitikiplot?color=gold)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14632005.svg)](https://doi.org/10.5281/zenodo.14632005)
![License](https://img.shields.io/github/license/BodduSriPavan-111/kitikiplot?color=green)

</div>

# diemsim

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

diem= DIEM( N= N, maxV= maxV, minV= minV, n_iter= n_iter ) 

value= diem.sim( S1, S2)

print( "Output Value: ", value )
```
Check out the complete <b>guide of customization</b> [here](https://github.com/BodduSriPavan-111/kitikiplot/blob/main/examples/Usage_Guide.ipynb).


Please refer <a href="https://github.com/BodduSriPavan-111/kitikiplot/blob/main/CONTRIBUTING.md">CONTRIBUTING.md</a> for <b>contributions</b> to kitikiplot.

### Key Contributor
<a href="https://www.linkedin.com/in/boddusripavan/"> Boddu Sri Pavan </a>

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
