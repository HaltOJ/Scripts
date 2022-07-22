import yaml
import os
from copy import deepcopy

print('put this in a folder with only testdata!')

print('''
data seperator be like: data_1_1.in / data-1-1.in
- or _ or any single letter
''')

data_sep = input()

print('''
data format be like:
subtask IDs can have letters, as long as the subtasks' names are in alphabetical ascending order like their IDs do

0. <subtask>{sep}anything
1. data{sep}<subtask>{sep}anything or anything{sep}<subtask>
2. anything{sep}anything{sep}<subtask>

(as you can see just input the <subtask>'s indicator's position in the seperated sequence, 0-indexed)
'''.format(sep=data_sep))

sub_pos = int(input())

print()

config = {
    'time': '1s',
    'memory': '512m',
    'filename': 'a'
}

for key in config:
    print(key)
    config[key] = input()
config['subtasks'] = list()
config['type'] = 'default'

sample_subtask = {
    'id': 0,
    'score': 10,
    'type': 'min',
    'cases': list()
}

sample_case = {
    'input': '#',
    'output': '#'
}

li = os.listdir()
li.sort()
subtask_ids = dict()
input_exts = {'in'}
output_exts = {'out','ans'}
subtask = deepcopy(sample_subtask)
case=deepcopy(sample_case)

for f in li:
    basename = f[:f.rfind('.')]
    extname = f[f.rfind('.')+1:]
    if extname in input_exts or extname in output_exts:

        subname = basename.split(data_sep)[sub_pos]
        if subname not in subtask_ids:
            subtask_ids[subname]=len(subtask_ids)+1
        sub_id=subtask_ids[subname]

        if subtask['id']!=sub_id:
            if subtask['id']!=0:
                config['subtasks'].append(subtask)
            subtask = deepcopy(sample_subtask)
            subtask['id']=sub_id
            print('score for subtask {name}'.format(name=subname))
            subtask['score']=int(input())
            case=deepcopy(sample_case)

        if extname in input_exts:
            case['input']=f
        else:
            assert extname in output_exts
            case['output']=f

        if case['input']!='#' and case['output']!='#':
            subtask['cases'].append(case)
            case=deepcopy(sample_case)

if subtask['id']!=0:
    config['subtasks'].append(subtask)

with open('config.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)
