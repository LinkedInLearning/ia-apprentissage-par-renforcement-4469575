import numpy as np


class Pheromone :
    def __init__(self, pheromone_size, phero_min, phero_max, evap_rate):
         self.pheromone_matrix =np.full((pheromone_size, pheromone_size), phero_min, dtype=float) 
         self.phero_max = phero_max
         self.phero_min = phero_min
         self.evap_rate = (1-evap_rate) 
         self.pheromone_size = pheromone_size 

    def get_phoromone(self, p1, p2):
         return self.pheromone_matrix[p1][p2] 
    
    def evaporate(self): 
        self.pheromone_matrix = self.pheromone_matrix * self.evap_rate
        self._check_pheromone_limits()
          
    
    def  reward(self, solution, cost): 
        reward_amount = 1/cost
        #print(f"Reward with {reward_amount} amount")
        for idx in range(len(solution)-1):
            self._set_pheromone(solution[idx], solution[idx+1], reward_amount)
            self._set_pheromone(solution[idx+1], solution[idx], reward_amount) #Symmetric pheromone
        
        self._set_pheromone(solution[len(solution)-1], solution[0], reward_amount)
        self._set_pheromone(solution[0], solution[len(solution)-1], reward_amount) #Symmetric pheromone




    def _set_pheromone(self, p1, p2, phero_val):
        self.pheromone_matrix[p1][p2] = self.pheromone_matrix[p1][p2] + phero_val 
        self._check_point_pheromone_limits(p1, p2)     
          
         
    def _check_point_pheromone_limits(self, p1, p2):
        if self.pheromone_matrix[p1][p2] > self.phero_max : 
            self.pheromone_matrix[p1][p2] = self.phero_max
        elif self.pheromone_matrix[p1][p2] < self.phero_min : 
            self.pheromone_matrix[p1][p2] = self.phero_min

    def _check_pheromone_limits(self):
        for idx1 in range(self.pheromone_size): 
            for idx2 in range(self.pheromone_size) :
                if self.pheromone_matrix[idx1][idx2] > self.phero_max : 
                    self.pheromone_matrix[idx1][idx2] = self.phero_max
                elif self.pheromone_matrix[idx1][idx2] < self.phero_min : 
                     self.pheromone_matrix[idx1][idx2] = self.phero_min  

    def show(self) -> str:
        for idx1 in range(self.pheromone_size): 
            ss=""
            for idx2 in range(self.pheromone_size) :  
                ss+=f" [{round(self.pheromone_matrix[idx1][idx2],4)}] "
            print(ss)
        print(f"Mean pheromone = {round(np.mean(self.pheromone_matrix),4)} \n" +
              f"Min pheromone = {round(np.min(self.pheromone_matrix),4)}\n" +
              f"Max pheromone = {round(np.max(self.pheromone_matrix),4)}\n" + 
              f"STD pheromone = {round(np.std(self.pheromone_matrix),4)}")