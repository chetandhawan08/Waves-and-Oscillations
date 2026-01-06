class EulerIntegrator:
    def step(self, particle, force, dt):
        acceleration = force.compute(particle) / particle.mass
        particle.velocity += acceleration * dt
        particle.position += particle.velocity * dt


class EulerCromerIntegrator:
    def step(self, particle, force, dt):
        acceleration = force.compute(particle) / particle.mass
        particle.velocity += acceleration * dt
        particle.position += particle.velocity * dt
