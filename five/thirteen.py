import random


class PacketSampler:
    
    def __init__(self, k):
        self.k = k
        self.n = 0
        self.subset = []
        
    def receive_packet(self, p):
        if len(self.subset) < self.k:
            self.subset.append(p)
        else:
            replace_prob = float(self.k) / (self.n + 1)
            if random.random() < replace_prob:
                replace_ind = random.randint(0, self.k - 1)
                self.subset[replace_ind] = p
        self.n += 1

        
class PacketSamplerWrong:
    
    def __init__(self, k):
        self.k = k
        self.n = 0
        self.subset = []
        
    def receive_packet(self, p):
        if len(self.subset) < self.k:
            self.subset.append(p)
        else:
            replace_prob = random.random()
            if random.random() < replace_prob:
                replace_ind = random.randint(0, self.k - 1)
                self.subset[replace_ind] = p
        self.n += 1


def get_packet_subset(n, packet_sampler):
    for i in range(n):
        packet_sampler.receive_packet(i)
    return packet_sampler.subset


def get_simulated_distribution(n, k, sampler_name, num_trials):
    if sampler_name == 'right':
        Sampler = PacketSampler
    elif sampler_name == 'wrong':
        Sampler = PacketSamplerWrong
    else:
        raise ValueError('Unrecognized sampler name.')
    
    packet_counter = {p: 0 for p in range(n)}
    for trial_ind in range(num_trials):
        subset = get_packet_subset(n, Sampler(k))
        for p in subset:
            packet_counter[p] += 1
    
    return packet_counter