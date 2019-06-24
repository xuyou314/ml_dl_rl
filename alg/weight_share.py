import torch.nn as nn
import numpy as np
from torch.optim import Adam
import torch
class Feedfoward_2_layer(nn.Module):
    def __init__(self):
        super(Feedfoward_2_layer,self).__init__()
        self.l1 = nn.Linear(6, 6)
        self.l2 = nn.Linear(6, 6)
        self.l1.weight=self.l2.weight
        self.l1.bias=self.l2.bias
    def forward(self,x):
        return self.l2(self.l1(x))
if __name__=="__main__":
    x=np.random.rand(100,6)
    weight1=np.random.rand(6,6)+5
    bias=np.random.rand(1,6)-10
    y1=x.dot(weight1)+bias
    y_true=y1.dot(weight1)+bias
    n_steps=50000
    model=Feedfoward_2_layer()
    opt=Adam(model.parameters())
    crit=nn.MSELoss()

    x=torch.Tensor(x)
    y_true=torch.Tensor(y_true)
    for i in range(n_steps):
        opt.zero_grad()
        yout=model(x)
        loss=crit(yout,y_true)
        loss.backward()
        opt.step()
        if(loss.item()<=0.001):
            break
        if(i%200==199):
            print("current loss", loss)
    print("true weight",weight1)
    print("true bias",bias)
    print("weight", list(model.parameters())[0])
    print("bias", list(model.parameters())[1])
