
import numpy as np



class Graph :
    def __init__(self, points):        
        self.distance_matrix =np.zeros((len(points),len(points)))  
        self.compute_distance_matrix(points)
        



    
    def compute_distance_matrix(self, points):         
        for idx_1 in range(len(points)) : 
            (x1,y1) = points[idx_1]
            point_1 = np.array([x1,y1]) 
            for idx_2 in range((idx_1+1), len(points)):
                (x2,y2) = points[idx_2]
                point_2 = np.array([x2,y2]) 
                current_distance = np.linalg.norm(point_1 - point_2)
                self.distance_matrix[idx_1][idx_2]=current_distance 
                self.distance_matrix[idx_2][idx_1]=current_distance 
         
         

    def get_distance(self, p1, p2):
        return self.distance_matrix[p1][p2]
    


    def show(self) -> str:
        n = self.distance_matrix.shape[0]
        for idx1 in range(n): 
            ss=""
            for idx2 in range(n) :  
                ss+=f" [{round(self.distance_matrix[idx1][idx2],4)}] "
            print(ss)