from tkinter import *
from tkinter import ttk
import random

from graph import Graph
from pheromone import Pheromone

class TSP : 
    def __init__(self):
        self.set_GUI()
        self.best_ever_solution = []
        self.cost_of_best_ever_solution=None
        self.diameter=6
        self.max_reward=0.0
       

    def run(self):
        self.main_window.mainloop()



    def set_GUI(self) :    
        
        self.main_window = Tk() 
        self.main_window.config(background="#FFFFFF")
        self.width= self.main_window.winfo_screenwidth()               
        self.height= self.main_window.winfo_screenheight()               
        self.main_window.geometry("%dx%d" % (self.width, self.height))
        self.main_window.minsize(self.width, self.height)

        self.draw_frame = Frame(self.main_window) 
        self.draw_frame.grid(row=0, column=0, sticky=N+S)

        self.config_frame = Frame(self.main_window)  
        self.config_frame.grid(row=0, column=1, sticky=N+S)        

        self.result_frame = LabelFrame(self.main_window, text="Results") 
        self.result_frame.grid(row=1, column=0, sticky=W+E)

        self.draw_canvas = Canvas(self.draw_frame, bg="#000000", width=(85 * self.width)/100, height=(85*self.height)/100)
        self.draw_canvas.grid(row=0, column=0)    
        
 
        # Data panel
        self.data_frame = LabelFrame(self.config_frame, text="Data")   
        self.data_frame.grid(row=0 , column=0, pady=5) 

        self.lbl_nb_points = Label(self.data_frame, text="TSP size") 
        self.lbl_nb_points.grid(row=0, column=0,sticky=W)
        self.str_nb_points =Entry(self.data_frame)
        self.str_nb_points.insert(0,"5") 
        self.str_nb_points.grid(row=1, column=0, padx=4)

        self.random_data = Button(self.data_frame, text="Random points", command=self.random_gen_points )
        self.random_data.grid(row=2, column=0, pady=(1,0), sticky=W+E)
     
        # Parameters panel
        self.param_frame = LabelFrame(self.config_frame, text="Parameters")   
        self.param_frame.grid(row=1 , column=0, pady=5, sticky=N+S)
        self.lbl_nb_ant = Label(self.param_frame, text="nb ants") 
        self.lbl_nb_ant.grid(row=0, column=0,sticky=W)
        self.str_nb_ant =Entry(self.param_frame) 
        self.str_nb_ant.insert(0,"10")
        self.str_nb_ant.grid(row=1, column=0, padx=4)

        self.lbl_nb_cycle = Label(self.param_frame, text="nb cycle") 
        self.lbl_nb_cycle.grid(row=2, column=0,sticky=W)
        self.str_nb_cycle =Entry(self.param_frame) 
        self.str_nb_cycle.insert(0,"2")
        self.str_nb_cycle.grid(row=3, column=0, padx=4)

        self.lbl_alpha = Label(self.param_frame, text="Alpha") 
        self.lbl_alpha.grid(row=4, column=0,sticky=W)
        self.str_alpha =Entry(self.param_frame) 
        self.str_alpha.insert(0,"1")
        self.str_alpha.grid(row=5, column=0, padx=4)

        self.lbl_beta = Label(self.param_frame, text="Beta") 
        self.lbl_beta.grid(row=6, column=0,sticky=W)
        self.str_beta =Entry(self.param_frame) 
        self.str_beta.insert(0,"1")
        self.str_beta.grid(row=7, column=0, padx=4, pady=5)


        self.lbl_phero_min = Label(self.param_frame, text="Pheromone Min") 
        self.lbl_phero_min.grid(row=8, column=0,sticky=W)
        self.str_phero_min =Entry(self.param_frame)
        self.str_phero_min.insert(0,"0.01") 
        self.str_phero_min.grid(row=9, column=0, padx=4, pady=5)

        self.lbl_phero_max = Label(self.param_frame, text="Pheromone Max") 
        self.lbl_phero_max.grid(row=10, column=0,sticky=W)
        self.str_phero_max =Entry(self.param_frame) 
        self.str_phero_max.insert(0,"5.0")
        self.str_phero_max.grid(row=11, column=0, padx=4, pady=5)

        self.lbl_evap_rate = Label(self.param_frame, text="Evaporation rate") 
        self.lbl_evap_rate.grid(row=12, column=0,sticky=W)
        self.str_evap_rate =Entry(self.param_frame) 
        self.str_evap_rate.insert(0,"0.01")
        self.str_evap_rate.grid(row=13, column=0, padx=4, pady=5)

        self.lbl_reward = Label(self.param_frame, text="Reward") 
        self.lbl_reward.grid(row=14, column=0,sticky=W)
        reward_option = ["Cycle best", "Colony best", "Both"]
        self.str_reward = ttk.Combobox(self.param_frame, values=reward_option) 
        self.str_reward.current(0)        
        self.str_reward.grid(row=15, column=0, padx=4, pady=5)


        # Algorithms panel
        
        self.solver_frame = LabelFrame(self.config_frame, text="Algorithm")   
        self.solver_frame.grid(row=2 , column=0, pady=5, sticky=W+E)
        self.aco_solver = Button(self.solver_frame, text="ACO", width = 17, command=self.run_aco  )
        self.aco_solver.grid(row=0, column=0, pady=(2,2) )
        self.nearest_solver = Button(self.solver_frame, text="Nearest", width = 17, command=self.run_nearest  )
        self.nearest_solver.grid(row=2, column=0, pady=(2,2) )
        self.random_solver = Button(self.solver_frame, text="Random", width = 17, command=self.run_random)
        self.random_solver.grid(row=3, column=0, pady=(2,2) )
         
  
        # Results panel
        self.lbl_best_result = Label(self.result_frame, text="Best result = ") 
        self.lbl_best_result.grid(row=0, column=0,sticky=W)

        self.best_result = Label(self.result_frame, text="00.00") 
        self.best_result.grid(row=0, column=1,sticky=W)
        self.spaces = Label(self.result_frame, text="     ") 
        self.spaces.grid(row=0, column=2,sticky=W)

        self.lbl_best_cycle_result = Label(self.result_frame, text="Best current cycle result = ") 
        self.lbl_best_cycle_result.grid(row=0, column=3,sticky=W) 
        self.best_cycle_result = Label(self.result_frame, text="00.00") 
        self.best_cycle_result.grid(row=0, column=4,sticky=W) 
        
        
        self.spaces = Label(self.result_frame, text="     ") 
        self.spaces.grid(row=0, column=5,sticky=W)

        self.lbl_n_cycle = Label(self.result_frame, text="#cycle: ") 
        self.lbl_n_cycle.grid(row=0, column=6,sticky=W) 
        self.n_cycle = Label(self.result_frame, text="") 
        self.n_cycle.grid(row=0, column=7,sticky=W) 

        self.spaces = Label(self.result_frame, text="     ") 
        self.spaces.grid(row=0, column=8,sticky=W)

        self.lbl_n_ant = Label(self.result_frame, text="#ant:") 
        self.lbl_n_ant.grid(row=0, column=9,sticky=W) 
        self.n_ant = Label(self.result_frame, text="") 
        self.n_ant.grid(row=0, column=10,sticky=W) 

        self.spaces = Label(self.result_frame, text="     ") 
        self.spaces.grid(row=0, column=11,sticky=W)

        self.lbl_error = Label(self.result_frame, text="", foreground="red") 
        self.lbl_error.grid(row=0, column=12,sticky=W) 
         
 

    def random_gen_points(self ):
        self.draw_canvas.delete("all")
        self.lbl_error.config(text="")
        
        try :
            self.nb_points = int(self.str_nb_points.get())
        except ValueError:
            s=" "
            self.lbl_error.config(text=f"{s*120} Error: The number of points must be an integer type")
            return 
       
        max_x = self.draw_canvas.winfo_reqwidth()
        max_y = self.draw_canvas.winfo_reqheight()
        self.points = []
        current_nb_point=1
        while current_nb_point <=self.nb_points:
            x = random.randint(1, max_x-10)           
            y = random.randint(1, max_y-10)                            
            if (x,y) not in self.points:
                self.points.append((x,y)) 
                current_nb_point+=1
        self._init_gui()
        self.graph = Graph(self.points)
    
    
    def run_random(self):      
        self.best_ever_solution = []
        self.cost_of_best_ever_solution=None
        self.solution=[]
        self.cost=[]
        current_solution = [] 
       
        for step in range(len(self.points)):
            next_point = self._get_next_step_by_random(current_solution)
            current_solution.append(next_point) 
        
        cost_of_current_solution = self._get_cost(current_solution)
        self.solution.append(current_solution) 
        self.cost.append(cost_of_current_solution)
     
        self._update_best_ever_solution()  
        self.draw_best_ever_solution()


    def run_nearest(self):      
        self.best_ever_solution = []
        self.cost_of_best_ever_solution=None
        self.solution=[]
        self.cost=[]
        current_solution = [] 
        for step in range(len(self.points)):
            next_point = self._get_next_step_by_nearest(current_solution)
            current_solution.append(next_point) 
        cost_of_current_solution = self._get_cost(current_solution)
        self.solution.append(current_solution) 
        self.cost.append(cost_of_current_solution)
        self._update_best_ever_solution()  
        self.draw_best_ever_solution()
             
            
     
    def run_aco(self):
        
        self.best_ever_solution = []
        self.cost_of_best_ever_solution=None
        if self._set_aco_params() :
            self.pheromone = Pheromone(self.nb_points, self.phero_min, self.phero_max, self.evap_rate)            

            for current_cycle in range(self.nb_cycle):   
                print(f"#Cycle{current_cycle}")              
                self.solution=[]
                self.cost=[]
                self.n_cycle.config(text=f"{current_cycle+1}")
                self.n_cycle.update_idletasks()
                for current_ant in range(self.nb_ant):
                    #print("##########################################")
                    #print(f"Running the ant {current_ant}")
                    self.n_ant.config(text=f"{current_ant+1}")
                    self.n_ant.update_idletasks()
                    current_solution = [] 
                    for step in range(len(self.points)):
                        next_point = self._get_next_step_by_aco(current_solution)
                        current_solution.append(next_point) 
                    cost_of_current_solution = self._get_cost(current_solution)
                    self.solution.append(current_solution) 
                    self.cost.append(cost_of_current_solution)
                    #self.pheromone.reward(current_solution, cost_of_current_solution)
                
                #print(f"Min cost = {min(self.cost)}  |  Max cost = {max(self.cost)}")
                self._update_best_ever_solution()  
                if self.str_reward == "Cycle best" :
                    self._reward_with_best_cycle_solution() 
                      
                elif self.str_reward == "Colony best"  :
                    self._reward_best_ever_solutions()
                else : 
                    self._reward_with_best_cycle_solution() 
                    self._reward_best_ever_solutions()

                self.pheromone.evaporate()  
            
            self.draw_best_ever_solution()
            self.pheromone.show()
            print(f"Best solution : \n{self.best_ever_solution}")
            print(f"Max reward : \n{self.max_reward}")


            

    def _update_best_ever_solution(self):
        self.best_cycle_result.config(text=f"{round(min(self.cost),2)}")
        if self.cost_of_best_ever_solution == None : 
            self.cost_of_best_ever_solution = self.cost[0] 
            self.best_ever_solution = self.solution[0]
             
        for idx_cost in range(0,len(self.cost)):
            if self.cost[idx_cost] < self.cost_of_best_ever_solution :
                self.cost_of_best_ever_solution = self.cost[idx_cost]
                self.best_ever_solution = self.solution[idx_cost]                            
                
        self.draw_best_ever_solution()
    
    def _get_candidates(self, current_solution):
        if len(current_solution) == 0 : return random.randint(0,len(self.points)-1)
        candidates=[] 
        for candidate in range(self.nb_points):
            if candidate not in current_solution : 
                candidates.append(candidate)
        return candidates

    def _get_next_step_by_nearest(self, current_solution):
        if len(current_solution) == 0 : return random.randint(0,len(self.points)-1)
        candidates = self._get_candidates(current_solution)       
        last_point = current_solution[-1]
        candidates_probs = self._compute_probs_by_distance(last_point, candidates)
        selected_point = self._select_next_point_by_max_prob(candidates, candidates_probs)
        return selected_point
  
    def _get_next_step_by_random(self, current_solution):
        if len(current_solution) == 0 : return random.randint(0,len(self.points)-1)
        candidates = self._get_candidates(current_solution)       
        selected_index = random.randint(0,len(candidates)-1)
        selected_point = candidates[selected_index]
        return selected_point
    

    def _get_next_step_by_aco(self, current_solution):
        if len(current_solution) == 0 : return random.randint(0,len(self.points)-1)
        candidates = self._get_candidates(current_solution)        
        last_point = current_solution[-1]
        candidates_probs = self._compute_probs_by_distance_and_pheromone(last_point, candidates) 
        selected_point = self._select_next_point_by_probs(candidates, candidates_probs)
        return selected_point

    

    def _compute_probs_by_distance(self, last_point, candidates):
        candidates_probs=[]
        for candidate in  candidates :
            candidates_probs.append(1/(self.graph.get_distance(last_point, candidate)))
        return candidates_probs
    
    def _compute_probs_by_pheromone(self, last_point, candidates):
        candidates_probs=[]
        for candidate in  candidates :
            candidates_probs.append(self.pheromone.get_phoromone(last_point, candidate))
        return candidates_probs
    
    def _get_normalized_values(self, values):
        normalized_values =  []
        cumul = sum(values)
        for v in values : 
            normalized_values.append(v/cumul)
        return normalized_values 
    

    def _compute_probs_by_distance_and_pheromone(self, last_point, candidates):
        candidates_probs=[]
        pheromone_values=[]
        heuristic_values=[]
        
        '''
        print("#####################################################################")
        ss=""
        for idx, (x,y) in enumerate(self.points) :
             ss+=f" {idx} : ({x},{y}) - "
        print(ss)

        print(f"last point : {last_point}")

        ss=""
        for idx, candidate in enumerate(candidates) :
            pheromone_values.append(self.pheromone.get_phoromone(last_point, candidate))
            heuristic_values.append(1/(self.graph.get_distance(last_point, candidate))) 
            ss+=f" {candidate} : ({pheromone_values[idx]},{heuristic_values[idx]}) - "
        print(ss)
        '''


        pheromone_values=[]
        heuristic_values=[]
        
        #print("After POW function")  
        #ss=""

        for idx, candidate in  enumerate(candidates) :
            pheromone_values.append(pow(self.pheromone.get_phoromone(last_point, candidate), self.alpha))
            heuristic_values.append(pow(1/(self.graph.get_distance(last_point, candidate)), self.beta)) 
            #ss+=f" {candidate} : ({pheromone_values[idx]},{heuristic_values[idx]}) - "
        #print(ss)

       

        pheromone_values =self._get_normalized_values(pheromone_values)
        heuristic_values = self._get_normalized_values(heuristic_values)

        ''' 
        print("After NORMALIZATION function")
        ss=""
        for idx, candidate in enumerate(candidates) :
            ss+=f" {candidate} : ({pheromone_values[idx]},{heuristic_values[idx]}) - "
        print(ss)
        '''

        for pheromone, heuristic in zip(pheromone_values, heuristic_values):
            candidates_probs.append(pheromone * heuristic)
        
        '''
        print("Final probs")
        ss=""
        for idx, candidate in enumerate(candidates) :
            ss+=f" {candidate} : ({candidates_probs[idx]}) - "
        print(ss)
        '''

        return candidates_probs
    
    def _select_next_point_by_probs(self, candidates, candidates_probs):
        cumul_probs= [] 
        cumul_probs.append(candidates_probs[0]) 
        for idx in range(1,len(candidates_probs)):
            cumul_probs.append(candidates_probs[idx]+cumul_probs[idx-1])

        for idx in range(len(cumul_probs)):
            cumul_probs[idx]=cumul_probs[idx]/cumul_probs[-1]
        
        '''
        print("Final normalized probs")
        ss=""
        for idx, candidate in enumerate(candidates) :
            ss+=f" {candidate} : ({cumul_probs[idx]}) - "
        print(ss)
        '''
        
        
        r = random.random() 
        #print(f"Selected r ={r}")
        selected_index=0
        for idx in range(len(cumul_probs)):
            if r <= cumul_probs[idx] : 
                selected_index=idx 
                break
        #print(f"Selected idx ={selected_index}")

        return candidates[selected_index]


    def _select_next_point_by_max_prob(self, candidates, candidates_probs):
        selected_index = candidates_probs.index(max(candidates_probs))
        return candidates[selected_index]

    def _select_next_point_by_random_selection(self, candidates):
        selected_index = random.randint(0,len(candidates)-1)
        return candidates[selected_index]



    def _get_cost(self, current_solution):
        cost = 0.0
        for idx in range(len(current_solution)-1):
            cost+=self.graph.get_distance(current_solution[idx], current_solution[idx+1])         
        cost+=self.graph.get_distance(current_solution[-1], current_solution[0])
         
        return cost


    def _reward_with_best_cycle_solution(self):
        
        min_cost = self.cost[0]
        min_cost_idx = 0
        for idx_cost in range(1,len(self.cost)):
            if self.cost[idx_cost] < min_cost :
                min_cost_idx=idx_cost
                min_cost = self.cost[idx_cost]
        if (1/min_cost) > self.max_reward: 
            self.max_reward = 1/min_cost 
        self.pheromone.reward(self.solution[min_cost_idx], min_cost) 
        
    def _reward_best_ever_solutions(self):   
        self.pheromone.reward(self.best_ever_solution, self.cost_of_best_ever_solution) 


    def _set_aco_params(self):
        self.lbl_error.config(text="")
        try :
            self.nb_ant = int(self.str_nb_ant.get())
            self.nb_cycle = int(self.str_nb_cycle.get())
            self.alpha = int(self.str_alpha.get())
            self.beta = int(self.str_beta.get())
            self.phero_min = float(self.str_phero_min.get())
            self.phero_max = float(self.str_phero_max.get())
            self.evap_rate = float(self.str_evap_rate.get())
            

        except ValueError:
            s=" "
            self.lbl_error.config(text=f"{s*120} Error: All ACO parameters must be of integer type")
            return False
        
        return True
    



    def draw_best_ever_solution(self):
        self.draw_canvas.delete("all")
        self.best_result.config(text=f"{round(self.cost_of_best_ever_solution,2)}")
        coords=[]
        is_first=True
        for p in self.best_ever_solution :
            (x,y) = self.points[p]
            coords.append(x) 
            coords.append(y)
            color = "snow"             
            if is_first : 
                color ="green yellow"                
                is_first = False             
            self.draw_canvas.create_oval(x,y,x+self.diameter,y+self.diameter, fill=color) 
        
        is_first=True
        for idx in range(len(self.best_ever_solution)-1) :
            (x1,y1) = self.points[self.best_ever_solution[idx]]
            (x2,y2) = self.points[self.best_ever_solution[idx+1]]
            color = "cyan2"             
            if is_first : 
                color ="red2"                
                is_first = False
            self.draw_canvas.create_line(x1,y1,x2,y2, fill=color, width=2)
        (x1,y1) = self.points[self.best_ever_solution[-1]]
        (x2,y2) = self.points[self.best_ever_solution[0]]
        self.draw_canvas.create_line(x1,y1,x2,y2, fill=color, width=2)
        self.draw_canvas.update_idletasks()

    def _init_gui(self):
        self.draw_canvas.delete("all")
        self.best_result.config(text=f"00.00")
        self.best_cycle_result.config(text=f"00.00")        
        self.n_cycle.config(text=f"")
        self.n_ant.config(text=f"")
        self.lbl_error.config(text=f"")

        for (x,y) in self.points :             
            self.draw_canvas.create_oval(x,y,x+self.diameter,y+self.diameter, fill="#FFFFFF")

        self.draw_canvas.update_idletasks()
        self.best_result.update_idletasks()
        self.best_cycle_result.update_idletasks()
        self.n_cycle.update_idletasks()
        self.n_ant.update_idletasks()
