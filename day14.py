from utils import get_input, ints

class Deer:
    def __init__(self, line):
        self.fly_speed, self.fly_time, self.rest_time = ints(line)

    def distance(self, time):
        q, r = divmod(time, self.fly_time + self.rest_time)
        return (q*self.fly_time + min(r, self.fly_time))*self.fly_speed

def scores(deers, time):
    scores = [0] * len(deers)
    for t in range(time):
        distances = [deer.distance(t + 1) for deer in deers]
        leader_distance = max(distances)
        for i, distance in enumerate(distances):
            scores[i] += int(distance == leader_distance)
    return scores

deers = [Deer(line) for line in get_input(14).splitlines()]
print('1.', max(deer.distance(2503) for deer in deers))
print('2.', max(scores(deers, 2503)))
