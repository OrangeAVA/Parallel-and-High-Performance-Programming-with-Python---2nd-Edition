import os, argparse, time
import torch, torch.nn as nn, torch.optim as optim
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader, DistributedSampler

class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 128), nn.ReLU(),
            nn.Linear(128, 10),
        )
    def forward(self, x): return self.net(x)

def setup(rank, world_size):
    dist.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

def main_worker(rank, world_size, epochs=1, batch_size=128, lr=1e-3):
    setup(rank, world_size)
    device = torch.device("cuda", rank) if torch.cuda.is_available() else torch.device("cpu")

    train_data = datasets.FashionMNIST(root="data", train=True, download=True, transform=ToTensor())
    sampler = DistributedSampler(train_data, num_replicas=world_size, rank=rank, shuffle=True)
    loader = DataLoader(train_data, batch_size=batch_size, sampler=sampler)

    model = TinyNet().to(device)
    ddp = DDP(model, device_ids=[rank] if torch.cuda.is_available() else None)

    opt = optim.Adam(ddp.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()

    t0 = time.time()
    ddp.train()
    for epoch in range(epochs):
        sampler.set_epoch(epoch)
        for x,y in loader:
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            out = ddp(x)
            loss = loss_fn(out, y)
            loss.backward()
            opt.step()
        if rank == 0:
            print(f"Epoch {epoch+1}/{epochs} done. Loss={loss.item():.4f}")
    if rank == 0:
        print("Elapsed:", time.time()-t0, "s")
    cleanup()

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--world_size", type=int, default=int(os.environ.get("WORLD_SIZE", "2")))
    parser.add_argument("--epochs", type=int, default=1)
    args = parser.parse_args()

    world_size = args.world_size
    mp.spawn(main_worker, args=(world_size, args.epochs), nprocs=world_size, join=True)

if __name__ == "__main__":
    run()
