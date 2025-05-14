"""
File Name: DIEM.py
Description: This file implements DIEM (Dimension Insensitive Euclidean Metric).
Author: Boddu Sri Pavan
Date Created: 04-05-2025
Last Modified: 07-05-2025
"""

# Import necessary library/ libraries
from typing import Union
import numpy as np

class DIEM:
    """
    Class implements DIEM (Dimension Insensitive Euclidean Metric).

    Attributes
    ----------
    N : int
        - Dimension of vector embedding.
    maxV : int or float
        - Assumed upper bound.
    minV : int or float
        - Assumed lower bound.
    n_iter : int
        - No.of random numbers (iterations) to find 'exp_center' and 'vard'.
        - Default is 1e5.
    stats : dict
        - Dictionary containing output of 'compact_vectorized_DIEM_Stat'.
    exp_center : float
        - Expected value.
        - Deterending Euclidean Distance on Median Value.
    vard : float
        - Variance of Euclidean distirbution.
    min_DIEM : float
        - Minimum possible DIEM value.
    max_DIEM : float
        - Maximum possible DIEM value.

    Methods
    -------
    compact_vectorized_DIEM_Stat : Computes required stats to calculate DIEM.
    sim : Computes DIEM value between any two given embeddings of dimension 'N'.
    norm_sim: Computes normalized DIEM value in the range [0,1] between any two given embeddings of dimension 'N'.
    """
    def __init__( self, N: int = None, maxV: float = 1, minV: float = 0, n_iter: int = int(1e5) ):
        """
        Initialize attributes.
        """
        self.N= N
        self.maxV= maxV
        self.minV= minV
        self.n_iter= n_iter

        # Initialize required stats to calculate DIEM
        self.stats= self.compact_vectorized_DIEM_Stat(N= self.N, maxV= self.maxV, minV= self.minV, n_iter= self.n_iter)
        self.exp_center= self.stats["exp_center"]
        self.vard= self.stats["vard"]
        self.min_DIEM= self.stats["min_DIEM"]
        self.max_DIEM= self.stats["max_DIEM"]

    def compact_vectorized_DIEM_Stat(self, N: int, maxV: float, minV: float, n_iter: int = int(1e5)) -> dict:
        """
        Computes required stats to calculate DIEM.

        Parameters
        ----------
        N : int
            - Dimension of vector embedding.
        maxV : int or float
            - Assumed upper bound.
        minV : int or float
            - Assumed lower bound.
        n_iter : int
            - No.of random numbers (iterations) to find 'exp_center' and 'vard'.
            - Default is 1e5.
        
        Returns
        -------
        'dict' with keys:
        exp_center : float
            - Expected value.
            - Deterending Euclidean Distance on Median Value.
        vard : float
            - Variance of Euclidean distirbution.
        std_one : float
            - One Standard Deviation of DIEM.
        orth_med : float
            - Median DIEM of Orthogonal Quantities.
        min_DIEM : float
            - Minimum possible DIEM value.
        max_DIEM : float
            - Maximum possible DIEM value.
        """

        # Calculate 'range_factor' only once to eliminate computation redundancy
        range_factor = maxV - minV

        # Generate two uniform distributions with 'n_iter' no.of samples each of 'N' dimension
        a, b = range_factor * np.random.rand(n_iter, N, 1) + minV, range_factor * np.random.rand(n_iter, N, 1) + minV

        # Calculate difference between corresponding vector embeddings
        difference= a[:, :, 0] - b[:, :, 0]

        # 'tmp' stores null space values of 'a'
        # 'd' stores Euclidean distance values between 'a' and 'b'
        tmp, d= [
            ( lambda svd_out: svd_out[2][np.sum(svd_out[1] > np.amax(svd_out[1]) * np.finfo(svd_out[1].dtype).eps * N, dtype=int):,:].T.conj() )(np.linalg.svd(a[iteration].T, full_matrices=True))
                for iteration in range(n_iter)
            ], np.sqrt(np.sum(difference ** 2, axis=1))

        # 'dort' stores Euclidean distance values between 'a' and 'tmp'
        # 'exp_center' stores deterending Euclidean Distance on Median Value
        # 'vard' stores variance of Euclidean distirbution.
        dort, exp_center, vard= [(lambda x: np.sqrt(np.dot(x, x)))(a[iteration][:, 0]-tmp[iteration][:, 0].reshape(-1, 1)[:, 0]) for iteration in range(n_iter)], np.median(d), np.var(d)

        # Compute 'rv_factor' only once to eliminate computation redundancy
        rv_factor= range_factor/ vard

        return {"exp_center": exp_center, "vard": vard, "std_one": np.std(rv_factor * (d - exp_center)),
                "orth_med": rv_factor * (np.median(dort) - exp_center),
                "min_DIEM": -(rv_factor * exp_center),
                "max_DIEM": rv_factor * (np.sqrt(N) * range_factor - exp_center)
                }
    
    def check_inputs(self, x: Union[list, np.ndarray], y: Union[list, np.ndarray]) -> float:
        """
            Function to convert inputs into 'np.array' and check shapes before computation of DIEM value.
        """
        
        # Convert inputs into 'np.ndarray'
        if isinstance(x, list):
            x= np.asarray(x)

        if isinstance(y, list):
            y= np.asarray(y)
        
        x_dim, y_dim= x.ndim, y.ndim
        # Check shapes
        if x_dim == y_dim and x_dim in [1, 2]:
                    
            return x, y
                
        raise ValueError( f"Dimension of input arrays: {x_dim}, {y_dim}. Dimension of input arrays should be 1-D or 2-D.")
    
        
    def sim(self, a: Union[list, np.ndarray], b: Union[list, np.ndarray], how= None) -> float:
        """
        Computes DIEM value.
        
        Parameters
        ----------
        a : np.ndarray
            - Input vector embedding-1.
        b : np.ndarray
            - Input vector embedding-2.
        how : str
            - 'all_pair': similarity of a[i], b[j]

        Returns
        -------
        DIEM Value : float

        Note
        ----
        This function is the 'compact_optimized_getDIEM' mentioned in 'notebooks/getDIEM_Optimization.ipynb'.
        """
        # Verify inputs
        a, b= self.check_inputs( a, b )

        if a.ndim == 2 and how == "all_pair":

            x= [ [ i-j for j in b] for i in a ]
            return [ [(self.maxV - self.minV) *(np.sqrt(np.dot( j, j))- self.exp_center)/ self.vard for j in i] for i in x ]

        x= a - b

        if x.ndim == 2 and how == None:

            # Indexwise DIEM calculation for two arrays
            return [ (self.maxV - self.minV) *(np.sqrt(np.dot(each_x, each_x))- self.exp_center)/ self.vard for each_x in x ]
        
        # DIEM for two vector embeddings
        return (self.maxV - self.minV) *(np.sqrt(np.dot(x, x))- self.exp_center)/ self.vard


    def norm_sim(self, a: Union[list, np.ndarray], b: Union[list, np.ndarray]) -> float:
        """
        Computes normalized DIEM value in the range [0,1].

        Parameters
        ----------
        a : np.ndarray
            - Input vector embedding-1.
        b : np.ndarray
            - Input vector embedding-2.

        Returns
        -------
        Normalized DIEM Value in the range [0,1]: float
        """

        # Min-Max Normalization
        return (self.sim( a, b ) - self.min_DIEM) / (self.max_DIEM - self.min_DIEM)
