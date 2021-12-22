class Section:
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, op):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.op = op

    def size(self):
        return (self.xmax - self.xmin + 1) * (self.ymax - self.ymin + 1) * (self.zmax - self.zmin + 1)

    def intersect(self, other):
        if self.xmin <= other.xmax and other.xmin <= self.xmax:
            if self.ymin <= other.ymax and other.ymin <= self.ymax:
                if self.zmin <= other.zmax and other.zmin <= self.zmax:
                    return Section(max(self.xmin, other.xmin), min(self.xmax, other.xmax),
                        max(self.ymin, other.ymin), min(self.ymax, other.ymax),
                        max(self.zmin, other.zmin), min(self.zmax, other.zmax), 'on')

        return None

sections = []

with open('input.txt') as f:
    for line in f:
        (op, rs) = line.strip().split(' ')
        (xr, yr, zr) = rs.split(',')

        xr = xr.split('=')[1]
        xmin, xmax = [int(v) for v in xr.split('..')]

        yr = yr.split('=')[1]
        ymin, ymax = [int(v) for v in yr.split('..')]

        zr = zr.split('=')[1]
        zmin, zmax = [int(v) for v in zr.split('..')]

        section = Section(xmin, xmax, ymin, ymax, zmin, zmax, op)
        sections.append(section)

def process(items):
    if len(items) == 0:
        return 0

    s1 = items[0]

    if s1.op == 'on':
        ans = s1.size() + process(items[1:])

        inters = []
        for item in items[1:]:
            inter = s1.intersect(item)
            if inter is not None:
                inters.append(inter)

        if len(inters) > 0:
            p = process(inters)
            ans = ans - p
        return ans

    else:
        return process(items[1:])

ans = process(sections)
print(ans)
