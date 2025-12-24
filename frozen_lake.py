import numpy as np
import random as rand
class Map:
    #Required attribute
    def __init__(self,matrix_size,hole_probability,rand_first_agent_location : bool,slip_probability=1/3):
        #Matrix
        self.matrix = np.zeros((matrix_size,matrix_size))
        #Agent
        self.agent = [0,0]
        #hole_probability
        self.h_prob = hole_probability
        #slip_probability
        self.slip_prob = slip_probability
        #Custom_first_agent_location?
        self.rand_agent_loc = rand_first_agent_location
#################Public Method####################
    #Initializing map
    def init_map(self):
        self._init_matrix()
        self._init_agent()
    #get agent location
    def get_agent_loc(self):
        return self.agent[:]
    #move agent location
    def move_agent(self,command):
        r = np.random.choice([0,1,2],p=[self.slip_prob,1-self.slip_prob*2,self.slip_prob])
        if command == "up":
            if r==0:
                self._move_agent("left")
            elif r==1:
                self._move_agent("up")
            elif r==2:
                self._move_agent("right")
        elif command == "down":
            if r==0:
                self._move_agent("right")
            elif r==1:
                self._move_agent("down")
            elif r==2:
                self._move_agent("left")
        elif command == "left":
            if r==0:
                self._move_agent("down")
            elif r==1:
                self._move_agent("left")
            elif r==2:
                self._move_agent("up")
        elif command == "right":
            if r==0:
                self._move_agent("up")
            elif r==1:
                self._move_agent("right")
            elif r==2:
                self._move_agent("down")
            
################Private Method##################
    #Initializing matrix
    def _init_matrix(self):
        #0 is hole, 1 is ice
        self.matrix[:] = np.random.choice([0,1],size=self.matrix.shape,p=[self.h_prob,1-self.h_prob])
        while not self._is_valid_map() :
            self.matrix[:] = np.random.choice([0,1],size=self.matrix.shape,p=[self.h_prob,1-self.h_prob])
    #Initializing agent
    def _init_agent(self):
        if self.rand_agent_loc:
            self.agent[0] = np.random.randint(0,self.matrix.size())
            self.agent[1] = np.random.randint(0,self.matrix.size())
            while self.matrix[self.agent[0],self.agent[1]] == 0:
                self.agent[0] = np.random.randint(0,self.matrix.size())
                self.agent[1] = np.random.randint(0,self.matrix.size())
        else:
            self.agent = [0,0] 
    #TODO : Finish _is_valid_map
    def _is_valid_map(self)->bool:
      pass
    def _move_agent(self,where):
        if where=="up":
            self.agent[0] += 1
        elif where=="down":
            self.agent[0] -= 1
        elif where=="left":
            self.agent[1] -= 1
        elif where=="right":
            self.agent[1] += 1

#TODO
#One game controller
#Training controller
