import numpy as np

class DIEM:

    def __init__( self, N= None, maxV= 1, minV= 0, n_iter= int(1e5) ):

        self.N= N
        self.maxV= maxV
        self.minV= minV
        self.n_iter= n_iter
        
        self.stats= self.compact_vectorized_DIEM_Stat(N= self.N, maxV= self.maxV, minV= self.minV, n_iter= self.n_iter)
        self.exp_center= self.stats["exp_center"]
        self.vard= self.stats["vard"]

    def compact_vectorized_DIEM_Stat(self, N, maxV, minV, n_iter= int(1e5)):

        range_factor = maxV - minV

        a, b = range_factor * np.random.rand(n_iter, N, 1) + minV, range_factor * np.random.rand(n_iter, N, 1) + minV

        difference= a[:, :, 0] - b[:, :, 0]

        tmp, d= [
            ( lambda svd_out: svd_out[2][np.sum(svd_out[1] > np.amax(svd_out[1]) * np.finfo(svd_out[1].dtype).eps * N, dtype=int):,:].T.conj() )(np.linalg.svd(a[iteration].T, full_matrices=True))
                for iteration in range(n_iter)
            ], np.sqrt(np.sum(difference ** 2, axis=1))

        dort, exp_center, vard= [(lambda x: np.sqrt(np.dot(x, x)))(a[iteration][:, 0]-tmp[iteration][:, 0].reshape(-1, 1)[:, 0]) for iteration in range(n_iter)], np.median(d), np.var(d)

        rv_factor= range_factor/ vard

        return {"exp_center": exp_center, "vard": vard, "std_one": np.std(rv_factor * (d - exp_center)),
                "orth_med": rv_factor * (np.median(dort) - exp_center),
                "min_DIEM": -(rv_factor * exp_center),
                "max_DIEM": rv_factor * (np.sqrt(N) * range_factor - exp_center)
                }

    def get_DIEM(self, a, b):

        return True