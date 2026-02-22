class System:
    def __init__(self, particle, force, integrator, dt):
        self.particle = particle
        self.force = force
        self.integrator = integrator
        self.dt = dt

    def step(self):
        # Support either a single force object or a list/tuple of forces.
        if isinstance(self.force, (list, tuple)):
            total_force = sum(force.compute(self.particle) for force in self.force)
        else:
            total_force = self.force.compute(self.particle)

        self.integrator.step(self.particle, total_force, self.dt)
