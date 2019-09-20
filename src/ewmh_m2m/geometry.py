from dataclasses import dataclass


@dataclass(frozen=True)
class Geometry:
    w: float
    h: float
    x: float
    y: float

    def build_relative(self, container):
        return Geometry(
            w=self.w / container.w,
            h=self.h / container.h,
            x=(self.x - container.x) / container.w,
            y=(self.y - container.y) / container.h
        )

    def build_absolute(self, container):
        return Geometry(
            w=self.w * container.w,
            h=self.h * container.h,
            x=container.x + self.x * container.w,
            y=container.y + self.y * container.h
        )

    def get_containing(self, containers):
        container_xs = list({g.x for g in containers})
        container_ys = list({g.y for g in containers})
        container_x = sorted([x for x in container_xs if x < self.x + self.w / 2])[-1]
        container_y = sorted([y for y in container_ys if y <= self.y + self.h / 2])[-1]

        return [s for s in containers if s.x == container_x and s.y == container_y][0]
