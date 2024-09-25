import torch

def _check_backend():
    if torch.backends.mps.is_available():
        print("MPS is available yaayy!!")
    else:
        print("Oops, try another backend?")


if __name__  == "__main__":
    _check_backend()