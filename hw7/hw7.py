path_to_passwd = '/etc/passwd'
path_to_group = '/etc/group'
path_to_output = 'output.txt'

file = open(path_to_passwd,'r')
passwd = file.readlines()
file.close()

file = open(path_to_group,'r')
group = file.readlines()
file.close()

# 1. bash - count users

shells = []
for i in range(len(passwd)):
	shells.append(passwd[i].split(':')[-1][:-1])
shellset = set(shells)
shells_str = ''
for shell in shellset:
	shells_str+='%s - %d ; ' % (shell,shells.count(shell))

file = open(path_to_output,'w')
file.write(shells_str+'\n')
file.close()

# 2. group - UIDs

groups = []
users = []
for line in group:
	groups.append(line.split(':'))
for line in passwd:
	users.append(line.split(':')[:4])

name_to_uid = {'':''}
gid_to_groupname = dict()
for u in users:
    name_to_uid[u[0]] = u[2]
for g in groups:
    gid_to_groupname[g[2]] = g[0]

group_and_uid = {}
for g in groups:
    group_and_uid[g[0]] = g[3].strip().split(',')
    for i in range(len(group_and_uid[g[0]])):
        group_and_uid[g[0]][i] = name_to_uid[group_and_uid[g[0]][i]]

for u in users:
    if group_and_uid[gid_to_groupname[u[3]]] == ['']:
        group_and_uid[gid_to_groupname[u[3]]] = [u[2]]
    else:
        if u[2] not in group_and_uid[gid_to_groupname[u[3]]]:
            group_and_uid[gid_to_groupname[u[3]]].append(u[2])

group_and_uid_str = ''
for k,v in group_and_uid.items():
	group_and_uid_str+='%s:%s, '%(k,','.join(v))

file = open(path_to_output,'a')
file.write(group_and_uid_str+'\n')
file.close()
