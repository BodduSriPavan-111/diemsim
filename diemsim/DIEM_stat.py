import numpy as np
from scipy.spatial.distance import euclidean
from scipy.linalg import null_space

class DIEM_stat:

    def __init__( self, N= None, maxV= 1, minV= 0, n_iter= 100000 ):

        self.N= N
        self.maxV= maxV
        self.minV= minV
        self.n_iter= n_iter

        self.stats= self._get_stat( N= self.N, maxV= self.maxV, minV= self.minV, n_iter= self.n_iter)
        
        self.d= self.stats["d"]
        self.dort= self.stats["dort"]
        self.exp_center= self.stats["exp_center"]
        self.vard= self.stats["vard"]
        self.orth_med= self.stats["orth_med"]
        self.adjusted_dist= self.stats["adjusted_dist"]
        self.std_one= self.stats["std_one"]
        self.min_DIEM= self.stats["min_DIEM"]
        self.max_DIEM= self.stats["max_DIEM"]


    @staticmethod
    def _get_stat( N, maxV, minV, n_iter):

        d= []
        dort= []

        for j in range(n_iter):

            a= (maxV-minV)*np.random.rand(N, 1)+minV
            b= (maxV-minV)*np.random.rand(N, 1)+minV

            tmp= null_space( a.T )
            ort= tmp[:, 0]

            d.append( euclidean( a.flatten(), b.flatten() ) )
            dort.append( euclidean(a.flatten(), ort) )

        exp_center= np.median( d )
        vard= np.var( d )
        
        orth_med= (maxV-minV)*(np.median(dort)- exp_center)/vard
        adjusted_dist= (maxV-minV)*(np.array(d)-exp_center)/vard

        std_one= np.std( adjusted_dist )

        min_DIEM= -(maxV-minV)*(exp_center/vard)
        max_DIEM= (maxV-minV)*(np.sqrt(N)*(maxV-minV)-exp_center)/vard

        return {"d": d, "dort": dort, "exp_center": exp_center, "vard": vard, 
                "orth_med": orth_med, "adjusted_dist": adjusted_dist, 
                "std_one": std_one, "min_DIEM": min_DIEM, "max_DIEM": max_DIEM}