from component import Component
from component import Distribution

# engine_piston = Component('Engine Piston')

# print(engine_piston.name)

# mttf = Distribution(2, .2)
# # mttf.create_plot()

# mttr = Distribution(2, 1, 'Gamma')
# # mttr.create_plot()

# print(mttf.get_from_distribution())

engine = Component(Distribution(2, 1, 'Gamma'), Distribution(1, 0.8), 'Engine', comp_type='p', capacity=500)

# engine.mttf.create_plot()
# engine.mttr.create_plot()

# print(engine.running)
# engine.switch_state()
# print(engine.running)
print(engine.capacity)