from component import Component
from component import Distribution
from math import floor

# Add a component
engine = Component(Distribution(400, 10), Distribution(12, 1.8), 'Engine', comp_type='np')

main_counter = 0  # hours
# total_time = 149016  # Full contract
total_time = 1800

while main_counter < total_time:
    if engine.running:
        engine.total_runtime += 1
        if engine.runtime >= floor(engine.next_failure):
            engine.switch_state()
            engine.runtime = 0
        else:
            engine.runtime += 1
    else:
        engine.total_repairtime += 1
        if engine.repairtime >= floor(engine.next_repair_time):
            engine.switch_state()
            engine.repairtime = 0
        else:
            engine.repairtime += 1
    main_counter += 1

print(engine.get_availability())