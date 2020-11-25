import numpy as np
import pandas as pd
import glob

class KNearestReg1D:
    def __init__(self, n_neighbors=12):
        self.n_neighbors = n_neighbors
    
    def fit(self, x, y):
        if type(x) == list:
            x = np.array(x)
        if type(y) == list:
            y = np.array(y)
        assert len(x.shape) == 1
        assert len(y.shape) == 1
        sorted_xy = sorted(list(zip(x, y)))
        self.sorted_x = [t[0] for t in sorted_xy]
        self.sorted_y = [t[1] for t in sorted_xy]
        
    def predict(self, x):
        if type(x) == list:
            x = np.array(x)
        assert len(x.shape) == 1
        return np.array([self.predict_point(xe) for xe in x])
        
    def predict_point(self, x):
        # 1. 가장 가까운 n_neighbors의 점 찾기
        #   1-1. Binary Search를 이용하여 가장 가까운 x' 찾기
        #   1-2. 위에서 찾은 x'로부터 좌우로 x와 가까운 점 확장
        # 2. 찾은 점 12개를 이용하여 simple linear regression하여 답 구하기
        #    (https://en.wikipedia.org/wiki/Simple_linear_regression)
        
        # 1. 가장 가까운 n_neighbors 점 찾기
        points = self.closest_points(x, n=self.n_neighbors)
        
        # 2. Linear Regression으로 추정하기
        x_near = np.array([t[0] for t in points])
        y_near = np.array([t[1] for t in points])
        sx2 = np.sum((x_near - np.mean(x_near)) ** 2)
        if sx2 == 0:
            return np.mean(y_near)
        sxy = np.sum((x_near - np.mean(x_near)) * (y_near - np.mean(y_near)))
        beta = sxy / sx2
        alpha = np.mean(y_near) - beta * np.mean(x_near)
        return alpha + beta * x
        
    def closest_points(self, x, n):
        import bisect
        # Locate the insertion point for x in a to maintain sorted order
        idx = bisect.bisect(self.sorted_x, x)
        
        # Candidate: (x_diff, x', y')
        candidates = []
        if idx < len(self.sorted_x):
            candidates.append((
                abs(self.sorted_x[idx] - x), self.sorted_x[idx], self.sorted_y[idx]
            ))
        for i in range(n + 1):
            idx_left = idx - i - 1
            if idx_left >= 0:
                candidates.append((
                    abs(self.sorted_x[idx_left] - x), self.sorted_x[idx_left], self.sorted_y[idx_left]
                ))
            idx_right = idx + i + 1
            if idx_right < len(self.sorted_x):
                candidates.append((
                    abs(self.sorted_x[idx_right] - x), self.sorted_x[idx_right], self.sorted_y[idx_right]
                ))
        closests = sorted(candidates)[:n]
        return sorted([(t[1], t[2]) for t in closests])


def build_KNR(file_paths=None, xname='Time (s)', yname='CO (ppm)', n_neighbors=None):
    if file_paths is None:
        file_paths = glob.glob('kaggle/input/train*.csv')
    df = []
    for file_path in file_paths:
        df_tmp = pd.read_csv(file_path)
        df.append(df_tmp)
    df = pd.concat(df)
    x = df[xname].values
    y = df[yname].values
    if n_neighbors is None:
        n_neighbors = len(file_paths)
    knr = KNearestReg1D(n_neighbors=n_neighbors)
    knr.fit(x, y)
    return knr


if __name__ == '__main__':
    knr = KNearestReg1D(n_neighbors=3)
    knr.fit([1,2,3,3.5,5], [4,5,6,7,7.5])
    print(knr.predict([2.5, 3.2, 3.7, 4]))
