class System:
    def __init__(self, particle, force, integrator, dt):
        self.particle = particle
        self.force = force
        self.integrator = integrator
        self.dt = dt

    def step(self):
        self.integrator.step(self.particle, self.force, self.dt)
