from component import Component
from component import Distribution
from treenode import treeNode
from math import floor

# Add a component
engine = Component(Distribution(400, 10), Distribution(12, 1.8), 'Engine', comp_type='np')
gearbox = Component(Distribution(410, 20), Distribution(8, 0.8), 'Gearbox', comp_type='np')
hp_pump = Component(Distribution(410, 20), Distribution(8, 0.8), 'HP Pump', comp_type='np')
# diesel_skid = treeNode('Diesel Skid', 'XofY', engine, gearbox, hp_pump, frac=2/3)
diesel_skid = treeNode('Diesel Skid', 'AND', engine, gearbox, hp_pump)
px_array = Component(Distribution(400, 10), Distribution(12, 1.8), 'PXs', comp_type='np')
membrane = Component(Distribution(410, 20), Distribution(8, 0.8), 'Membrane', comp_type='np')
membrane_skid = treeNode('Membrane Skid', 'AND', px_array, membrane)

ro_train = treeNode('RO Train', 'AND', diesel_skid, membrane_skid)

main_counter = 0  # hours
# total_time = 149016  # Full contract
total_time = 1800

while main_counter < total_time:
    for child in diesel_skid.children:
        if child.running == True:
            child.runtime += 1
            child.total_runtime += 1
            if child.runtime >= child.next_failure:
                child.runtime = 0
                child.running = False
                diesel_skid.update_node_status()
                if diesel_skid.running == False:
                    diesel_skid.shutdown_node()
        elif child.running == False:
            child.repairtime += 1
            child.total_repairtime += 1
            if child.repairtime >= child.next_repair_time:
                child.repairtime = 0
                child.running = True
                diesel_skid.update_node_status()
                if diesel_skid.running == True:
                    diesel_skid.startup_node()
        else:
            print('error 1')
        print('running? ', child.running, 'runtime: ', child.runtime)
    print('running? ', diesel_skid.running)
    main_counter += 1




