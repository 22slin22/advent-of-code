from utils import *

@dataclass(eq=True, frozen=True)
class Blueprint:
    id: int
    o_per_o: int
    o_per_c: int
    o_per_ob: int
    c_per_ob: int
    o_per_g: int
    ob_per_g: int

    def max_o(self):
        return max(self.o_per_o, self.o_per_c, self.o_per_ob, self.o_per_g)

with open('q19.txt') as file:
    bps = [Blueprint(*nats(line)) for line in file]

@cache
def max_geode(bp: Blueprint, time, o, c, ob, opm, cpm, obpm, gpm):
    if time == 1:
        return gpm
    n = 0
    if o >= bp.o_per_o and opm < bp.max_o():
        n = max(n, max_geode(bp, time-1, o+opm-bp.o_per_o, c+cpm, ob+obpm, opm+1, cpm, obpm, gpm))
    if o >= bp.o_per_c and cpm < bp.c_per_ob:
        n = max(n, max_geode(bp, time-1, o+opm-bp.o_per_c, c+cpm, ob+obpm, opm, cpm+1, obpm, gpm))
    if o >= bp.o_per_ob and c >= bp.c_per_ob and obpm < bp.ob_per_g:
        n = max(n, max_geode(bp, time-1, o+opm-bp.o_per_ob, c+cpm-bp.c_per_ob, ob+obpm, opm, cpm, obpm+1, gpm))
    if o >= bp.o_per_g and ob >= bp.ob_per_g:
        n = max(n, max_geode(bp, time-1, o+opm-bp.o_per_g, c+cpm, ob+obpm-bp.ob_per_g, opm, cpm, obpm, gpm+1))
    if o < bp.max_o() or ob < bp.ob_per_g or c < bp.c_per_ob:
        n = max(n, max_geode(bp, time-1, o+opm, c+cpm, ob+obpm, opm, cpm, obpm, gpm))
    return gpm + n

def quality(bp, time):
    q = max_geode(bp, time, 0, 0, 0, 1, 0, 0, 0)
    print(q)
    max_geode.cache_clear()
    return q

# print(sum(quality(bp, 24) * bp.id for bp in bps))

print(prod(quality(bp, 32) for bp in bps[:3]))