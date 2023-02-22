import numpy as np
import pandas as pd
import torch
import torch.nn

if __name__ == "__main__":
    print("Is cuda available?" + str(torch.cuda.is_available()))